from blogs.models import Blog, Category
from portfolio.subscriber_form import SubscribeForm


def get_blogs_categories(request, limit=4):
    categories = []
    category = Category.objects.order_by('name')
    for cat in category:
        if len(cat.blog_set.all()) > 0:
            categories.append(cat)

    if len(categories) > 4:
        categories = categories[:limit]

    return categories


def footer_data(request):
    blog_categories = get_blogs_categories(request, 5)
    subscribe_form = SubscribeForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
    elif request.method == 'GET':
        subscribe_form = SubscribeForm(request.GET)

    data = {'footer_categories': blog_categories, 'subscribe_form': subscribe_form}
    return data
