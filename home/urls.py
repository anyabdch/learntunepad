from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.tester, name='test'),
    path('', views.landing, name='home'),
    path('g/', views.gridLayout, name='grid layout'),
    path('g/<str:data>', views.gridLayout, name='grid layout'),
    path('c/<str:data>', views.sidebarLayout, name='sidebar layout'),
    path('e/<str:data>', views.embed, name='video layout'),
    path('search', views.searchResults, name='search results'),
    path('filtered', views.filtersSet, name='set filters'),
    path('filtered/<int:loaded>', views.filtersSet, name='set filters'),
    path('proxy/<int:data>', views.proxy, name='proxy'),
    path('proxy', views.proxy, name='proxy'),
    path('populate', views.filterPopulate, name='populate'),
    path('restore', views.restore, name='restore'),
    path('order/<str:data>', views.order, name='sort')
]