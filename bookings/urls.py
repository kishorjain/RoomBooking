from django.urls import path
from .views import BookingHomeView,ConfirmBookingView
from .views import RoomCheckView# Import the new class view
from .views.admin_actions import add_room,edit_room_rate

urlpatterns = [
    path('', BookingHomeView.as_view(), name='booking_home'),
    path('check-availability/', RoomCheckView.as_view(), name='checkroom'),
    path('confirm/', ConfirmBookingView.as_view(), name='confirm_booking'),
    path('room/add/', add_room, name='add_room'),
    path('room/<int:room_id>/edit-rate/', edit_room_rate, name='edit_room_rate'),

    
]
