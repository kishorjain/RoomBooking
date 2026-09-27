from django.views import View
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_datetime
from django.contrib import messages
from bookings.models import Room, Booking

class RoomCheckView(View):
    def post(self, request, *args, **kwargs):
        category = request.POST.get('room_category', '').strip()
        check_in_str = request.POST.get('check_in', '').strip()
        check_out_str = request.POST.get('check_out', '').strip()

        if not category or not check_in_str or not check_out_str:
            messages.error(request, "Please select a room category and fill out both dates.")
            return redirect('booking_home')

        check_in = parse_datetime(check_in_str)
        check_out = parse_datetime(check_out_str)

        if not check_in or not check_out:
            messages.error(request, "Invalid date values. Please select dates using the calendar picker.")
            return redirect('booking_home')

        # Find rooms matching our chosen category code string field
        rooms_in_category = Room.objects.filter(category=category)

        # 🔑 UPDATE THIS ENTITY QUERY BLOCK TO MATCH YOUR DATABASE CAMELCASE COLUMNS
        booked_room_ids = Booking.objects.filter(
            roomID__category=category,
            checkIn__lt=check_out,    # Changed check_in to checkIn
            checkOut__gt=check_in     # Changed check_out to checkOut
        ).values_list('roomID_id', flat=True) # Changed room_id to roomID_id based on your database schemas

        # Keep open rooms untouched
        available_rooms = rooms_in_category.exclude(id__in=booked_room_ids)

        context = {
            'room_categories': Room.ROOM_CATEGORIES,
            'category_display': dict(Room.ROOM_CATEGORIES).get(category),
            'check_in': check_in,
            'check_out': check_out,
            'available_rooms': available_rooms,
        }
        return render(request, 'bookings/room_results.html', context)
