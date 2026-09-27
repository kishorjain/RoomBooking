from django.db import models
from django.contrib.auth.models import User  # Django's built-in user system

class Room(models.Model):
    roomID=models.CharField(max_length=30, unique=True)
    price= models.DecimalField(max_digits=8, decimal_places=2)
    ROOM_CATEGORIES = [
        ('SINGLE', 'Single Room'),
        ('DELUXE', 'Deluxe Room'),
        ('SUITE', 'Luxury Suite'),
        ('CONF', 'Conference Hall'),
    ]
    category = models.CharField(max_length=50, choices=ROOM_CATEGORIES, default='DELUXE')
    capacity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.category}-{self.capacity}"
    
class Booking(models.Model):
    RoomStatus=[
        ('AVAILABLE','Available'),
        ('BOOKED','Booked'),
    ]
    userID=models.ForeignKey(User,on_delete=models.CASCADE)
    roomID=models.ForeignKey(Room,on_delete=models.CASCADE)
    status= models.CharField(max_length=10, choices=RoomStatus, default='AVAILABLE')
    checkIn=models.DateTimeField()
    checkOut=models.DateTimeField()
    createdAt=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Booking by {self.userID.username} for {self.roomID.roomID} current status {self.get_status_display()}"
    
        
    
    



