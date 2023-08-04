from django.views.generic import View, TemplateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from authentication.forms import UserForm, UserProfileForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from authentication.models import UserProfile
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'accounts/index.html'
    user_form = UserForm()
    profile_form = UserProfileForm()

    def get_user_initial_data(self,request):
        user_id = request.user.username
        user = User.objects.get(username=user_id)
        if request.method == 'POST':
            user_id = request.POST.get('id')
            user = User.objects.get(id=user_id)

        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'user' : user.id
        }
        try:
            user_profile = UserProfile.objects.get(user=user.id)
            initial_data['social_link'] = user_profile.social_link
            initial_data['profile_pic'] = user_profile.profile_pic
        except:
            initial_data['social_link'] = ''
            initial_data['profile_pic'] = ''

        return initial_data

    def get(self, request, **args):
        initial_data = self.get_user_initial_data(request)
        self.user_form = UserForm(request.POST or None,initial=initial_data)
        self.profile_form = UserProfileForm(request.POST or None,initial=initial_data)

        if 'profile_update' in request.session and request.session['profile_update']:
            messages.success(request, 'Profile Updated Successfully.')

        request.session['profile_update'] = False

        context = {
            'user_form': self.user_form,
            'profile_form': self.profile_form
        }
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['user_form'] = self.user_form
        # context['profile_form'] = self.profile_form
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            initial_data = self.get_user_initial_data(request)
            self.profile_form = UserProfileForm(data=request.POST, initial=initial_data)
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            social_link = request.POST.get('social_link')
            user_id = request.POST.get('id')

            user = User.objects.get(pk=user_id)

            if user:
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                if len(password) > 0:
                    user.set_password(password)

                user.save()

                user_profile = UserProfile.objects.get(user=user_id)
                user_profile.social_link = social_link

                if 'profile_pic' in request.FILES:
                    if not request.FILES['profile_pic']:
                        print('Profile Pic Empty')
                    else:
                        user_profile.profile_pic = request.FILES['profile_pic']

                user_profile.save()
                update_session_auth_hash(request, user)
                request.session["profile_update"] = True
            else:
                print("User  Not Found!")

        return HttpResponseRedirect(reverse('auth:my_account'))
