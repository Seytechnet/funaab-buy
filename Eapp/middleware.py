from django.shortcuts import redirect
from django.urls import reverse

class Custom404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Check if response is a 404 error
        if response.status_code == 404:
            return redirect(reverse('Eapp:index'))  # Redirect to 'Eapp:index'
        return response
