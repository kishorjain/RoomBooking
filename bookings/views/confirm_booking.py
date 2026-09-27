from django.views import View
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_datetime
from django.contrib import messages
from bookings.models import Room, Booking

class ConfirmBookingView(View):
    def post(self, request, *args, **kwargs):
        # 1. Ensure the customer is logged in before booking
        if not request.user.is_authenticated:
            messages.error(request, "You must log in to finalize a room reservation.")
            return redirect('account_login')

        # 2. Extract stashed parameters out of the results form hidden inputs
        room_id = request.POST.get('room_id')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')

        # 3. Parse strings back into Python datetime objects
        check_in = parse_datetime(check_in_str)
        check_out = parse_datetime(check_out_str)

        try:
            # 4. Fetch the selected target Room object instance
            room_instance = Room.objects.get(id=room_id)

            # 5. 🔑 INSERT THE RECORD INTO THE DATABASE TABLE
            # Mapping directly to your database table's specific camelCase field names
            Booking.objects.create(
                userID=request.user,          # Pass the active User session object
                roomID=room_instance,        # Pass the associated Room object
                checkIn=check_in,            # Pass parsed check-in date
                checkOut=check_out           # Pass parsed check-out date
            )

            messages.success(request, f"Success! Your reservation for '{room_instance.name}' is officially confirmed.")
            return redirect('booking_home')

        except Room.DoesNotExist:
            messages.error(request, "The requested room entry was not found in our database system.")
            return redirect('booking_home')
