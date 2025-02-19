from pages.views import *
from django.urls import path

app_name= 'pages'

urlpatterns = [
    path('404',page_404_view,name='404'),
    path('feature',feature_view,name='feature'),
    path('product',product_view,name='product'),
    path('team',team_view,name='team'),
    path('testimonial',testimonial_view,name='testimonial'),
]