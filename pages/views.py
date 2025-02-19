from django.shortcuts import render

def page_404_view(request):
    return render(request,'page/404.html')

def feature_view(request):
    return render(request,'page/feature.html')

def product_view(request):
    return render(request,'page/product.html')

def team_view(request):
    return render(request,'page/team.html')

def testimonial_view(request):
    return render(request,'page/testimonial.html')