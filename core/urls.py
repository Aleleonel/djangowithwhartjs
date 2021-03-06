from django.urls import path
from core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),
    path('api/products/', v.products, name='products'),
    path('api/categories/', v.categories, name='categories'),
]