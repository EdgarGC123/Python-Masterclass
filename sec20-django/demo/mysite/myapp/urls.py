from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name="index"),
    # path('products/', views.products, name="products")# products is removed from my app views. 
    #book/1 detail views
    path('book/<int:book_id>/', views.detail, name='detail'),
    path('add/', views.add_book, name="add_book"),
    path('update/<int:id>/',views.update,name='update'),
] 
