from django.shortcuts import render
from django.views.generic import TemplateView


class UsersHomeView(TemplateView):
    template_name = 'users/users_home.html'
    
    # 1. Handles regular page loads (GET)
    def get(self, request, *args, **kwargs):
        # Read a search query from the URL (e.g., ?search=conference)
        search_query = request.GET.get('search', '')
        
        context = {
            'username': 'Kishor',
            'search_query': search_query,
        }
        return render(request, self.template_name, context)

    # 2. Handles form submissions (POST)
    def post(self, request, *args, **kwargs):
        # Extract values from the form input fields using their 'name' attributes
        submitted_name = request.POST.get('input_username', '')
        submitted_role = request.POST.get('input_role', '')

        context = {
            # Update the page display dynamically with the POSTed data
            'username': submitted_name if submitted_name else 'Kishor',
            'user_role': submitted_role,
            'message': 'Profile updated successfully!'
        }
        return render(request, self.template_name, context)