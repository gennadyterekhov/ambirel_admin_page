from django.urls import path, include
from . import views

app_name = 'opencart'
urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_category_check/', views.create_category_check, name='create_category_check'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('edit_category_check/', views.edit_category_check, name='edit_category_check'),
    path('products/', views.products, name='products'),
    path('attributes/', views.attributes, name='attributes'),
    path('filters/', views.filters, name='filters'),
    path('options/', views.options, name='options'),
]
