from django.contrib import admin
from django.urls import path
from .views import addbook,viewbooks,edit_book

urlpatterns = [
    path('add/', addbook),
    path('view/',viewbooks),
    path('edit/<int:id>/', edit_book),
]