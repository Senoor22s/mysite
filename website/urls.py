from website.views import *
from django.urls import path

app_name= 'website'

urlpatterns = [
    path('',index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
    path('blog',blog_view,name='blog'),
    path('404',page_404_view,name='404'),
    path('feature',feature_view,name='feature'),
    path('product',product_view,name='product'),
    path('team',team_view,name='team'),
    path('testimonial',testimonial_view,name='testimonial'),
]