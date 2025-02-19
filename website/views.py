from django.shortcuts import render

def index_view(request):
    return render(request,'New Folder/index.html')

def about_view(request):
    return render(request,'New Folder/about.html')

def contact_view(request):
    return render(request,'New Folder/contact.html')

def blog_view(request):
    return render(request,'blog/blog.html')

def page_404_view(request):
    return render(request,'pages/404.html')

def feature_view(request):
    return render(request,'pages/feature.html')

def product_view(request):
    return render(request,'pages/product.html')

def team_view(request):
    return render(request,'pages/team.html')

def testimonial_view(request):
    return render(request,'pages/testimonial.html')