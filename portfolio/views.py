from django.shortcuts import render
from django.views.generic import View, TemplateView
from portfolio.services.models import Service
from portfolio.models import Portfolio, Testimonial, Subscriber, Contact
from blogs.models import Category,Blog
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, resolve
from portfolio.contact_form import ContactForm
from django.core.mail import send_mail


class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.get_services()
        context['portfolio'] = self.get_portfolios()
        context['blog_categories'] = self.get_blogs_categories()
        context['recent_blogs'] = self.get_blogs()
        context['testimonials'] = self.get_testimonials()
        return context

    def get_services(self):
        services = Service.objects.order_by('id')[:6]
        return services

    def get_portfolios(self):
        portfolios = Portfolio.objects.order_by('name')
        categories = set()
        for portfolio in portfolios:
            categories.add(portfolio.category.name)

        return {'portfolios': portfolios, 'portfolio_categories': categories}

    def get_blogs_categories(self,limit=4):
        categories = []
        category = Category.objects.order_by('name')
        for cat in category:
            if len(cat.blog_set.all()) > 0:
                categories.append(cat)

        if len(categories) > 4:
            categories = categories[:limit]

        return categories

    def get_testimonials(self):
        testimonials = Testimonial.objects.order_by('-id')
        return testimonials

    def get_blogs(self):
        blogs = Blog.objects.filter(status=True).order_by('id')

        if len(blogs) > 3:
            blogs = blogs[:3]

        return blogs



class ContactView(TemplateView):
    template_name = 'portfolio/contact_us.html'
    contact_form = ContactForm()
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = self.contact_form
        context['contact_sent'] = False

        if 'contact_sent' in self.request.session and self.request.session['contact_sent']:
            context['contact_sent'] = True
            self.request.session['contact_sent'] = False

        return context

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            email = request.POST.get('email')
            name = request.POST.get('name')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            contact = Contact(email=email,name=name,subject=subject,message=message)
            contact.save()

            send_mail(
                "Enquiry Sent Name : {} and Email : {}".format(name,email),
                "Subject : {} \n Message : {}".format(subject,message),
                "rahul.dhamecha@infobeans.com",
                [email],
                fail_silently=False,
            )

            request.session['contact_sent'] = True
        return HttpResponseRedirect(reverse('portfolio:contact'))

class SubscribeView(View):

    def get(self, request, **args):
        context = {
            'test' : 'Test Demo'
        }
        return render(request,'portfolio/subscribe.html',context)

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            email = request.POST.get('email')
            is_subscribe = True

            subscribe = Subscriber.objects.get(email=email)

            if not subscribe:
                subscribe = Subscriber(email=email)

            subscribe.is_subscribe = is_subscribe
            subscribe.save()

            request.session['subscribe'] = True
            request.session['subscribe_email'] = subscribe.email
        return HttpResponseRedirect(reverse('portfolio:subscribe'))

class SubscribeView(View):

    def get(self, request, **args):
        context = {
            'test' : 'Test Demo'
        }
        return render(request,'portfolio/subscribe.html',context)

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            email = request.POST.get('email')
            is_subscribe = True

            subscribe = Subscriber.objects.get(email=email)

            if not subscribe:
                subscribe = Subscriber(email=email)

            subscribe.is_subscribe = is_subscribe
            subscribe.save()

            request.session['subscribe'] = True
            request.session['subscribe_email'] = subscribe.email
        return HttpResponseRedirect(reverse('portfolio:subscribe'))

class UnsubscribeView(View):

    def get(self, request, **args):
        if 'subscribe_email' not in request.session and not request.session['subscribe_email']:
            return HttpResponseRedirect(reverse('portfolio:index'))

        context = {
            'test' : 'Test Demo'
        }
        return render(request,'portfolio/unsubscribe.html',context)

    def post(self,request,*args,**kwargs):
        if 'subscribe_email' not in request.session and not request.session['subscribe_email']:
            return HttpResponseRedirect(reverse('portfolio:index'))

        if request.method == 'POST':
            email = request.POST.get('email')
            is_subscribe = False

            subscribe = Subscriber.objects.get(email=email)

            if not subscribe:
                subscribe = Subscriber(email=email)

            subscribe.is_subscribe = is_subscribe
            subscribe.save()

            request.session['subscribe'] = is_subscribe
            request.session['subscribe_email'] = subscribe.email
        return HttpResponseRedirect(reverse('portfolio:unsubcribe'))