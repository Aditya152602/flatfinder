from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listing_list, name='listing_list'),
    path('listings/map/', views.listing_map, name='listing_map'),
    path('listings/add/', views.add_listing, name='add_listing'),
    path('listings/my/', views.my_listings, name='my_listings'),
    path('listings/saved/', views.saved_listings, name='saved_listings'),
    path('listings/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('listings/<int:pk>/save/', views.save_listing, name='save_listing'),
    path('listings/<int:pk>/contact/', views.contact_owner, name='contact_owner'),
    path('listings/<int:pk>/delete/', views.delete_listing, name='delete_listing'),
]
