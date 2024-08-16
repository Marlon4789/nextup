# form_blocks/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.db import IntegrityError
from .forms import SubscriptionForm

def subscription_form(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                response_data = {'success': True, 'message': 'Correo enviado con éxito.'}
            except IntegrityError:
                response_data = {'success': False, 'message': 'Este correo ya está suscrito.'}
        else:
            response_data = {'success': False, 'message': 'Error en el formulario.'}
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse(response_data)
        
    form = SubscriptionForm()
    return render(request, 'content_forms/subscription/subscribe.html', {'form': form})
