from category.models import Category

def category_links(request):
    links = Category.objects.all()
    print(dict(links=links))
    return dict(links=links)