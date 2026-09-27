from bookings.models import Room
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect,render,get_object_or_404

def is_admin(user):
    return user.is_authenticated and user.is_staff
    
@user_passes_test(is_admin,login_url='account_login')
def add_room(request):
    if request.method=="POST":
        room_name=request.post('room_name')
        room_price=request.post('room_price')
        category=request.post('category')
        capacity=request.post('capacity')
        desc=request.post('desc')
        
        Room.objects.create(
                roomID=room_name,
                price=room_price,
                category=room_category,
                capacity=room_capacity,
                description=room_desc
        )
        messages.success(request, f"Room '{room_name}' added successfully!")
        return redirect('booking_home')
    return render(request, 'bookings/room_form.html')

    # ⚙️ 2. UPDATE ROOM RATE FUNCTION
@user_passes_test(is_admin, login_url='account_login')
def edit_room_rate(request, room_id):
    room_instance = get_object_or_404(room_id)
    if request.method == "POST":
        # Overwrite the old price with the new one from the input box
        room_instance.price = request.POST.get('price')
        room_instance.save() # Commit changes to the database row
        
        messages.success(request, f"Price for '{room_instance.roomID}' updated successfully!")
        return redirect('booking_home')

    # Send the room data to the HTML page so the admin can see the current price
    return render(request, 'bookings/room_form.html', {'room': room_instance})

