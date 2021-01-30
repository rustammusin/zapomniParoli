from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')



def blog(request):
    return render(request, 'blog/single-blog.html')



def blog(request):
    return render(request, "blog/blog.html")



def elements(request):
    return render(request, "blog/elements.html")


def contact(request):
    return render(request, "blog/contact.html")

    
def menu(request):
    return render(request, "blog/menu.html")