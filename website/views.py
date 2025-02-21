from django.shortcuts import render

def index_view(request):
    return render(request,'New Folder/index.html')

def about_view(request):
    return render(request,'New Folder/about.html')

def contact_view(request):
    return render(request,'New Folder/contact.html')
