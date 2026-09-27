from django.views.generic import TemplateView
from bookings.models import Room

class BookingHomeView(TemplateView):
    template_name = 'bookings/booking_home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_categories'] = Room.ROOM_CATEGORIES
        return context
