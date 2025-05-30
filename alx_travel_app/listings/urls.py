from django.urls import path
from . import views

urlpatterns = [
    # Listings
    path('', views.ListingListCreateView.as_view(), name='listing-list-create'),
    path('<int:pk>/', views.ListingDetailView.as_view(), name='listing-detail'),

    # Bookings
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
]
