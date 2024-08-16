from django.conf import settings
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os

from django.shortcuts import render, get_object_or_404
from blog.models import Article
from form_blocks.forms import SubscriptionForm
from social_networks.models import SocialMediaProfile

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES.get('file')
        if image:
            path = default_storage.save(os.path.join('uploads', image.name), image)
            return JsonResponse({'location': f'{settings.MEDIA_URL}{path}'})
    return JsonResponse({'error': 'Error al subir la imagen'}, status=400)


# Create your views here.

def show_posts(request):
    quill_posts = Article.objects.all().order_by('-id')
    return render(request, 'content/show_posts.html', {'quill_posts': quill_posts})

def home(request):
    quill_posts = Article.objects.all().order_by('-id')
    social_profiles = SocialMediaProfile.objects.all()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Correo enviado con éxito.'})
            return render(request, 'content/detail.html', {
                'form': form,
                'success_message': 'Correo enviado con éxito.'
            })
    else:
        form = SubscriptionForm()

    return render(request, 'content/home.html', {'quill_posts': quill_posts, 'form': form, 'success': True, 'social_profiles': social_profiles})


def quillpost_detail(request, quillpost_id):
    quillpost = get_object_or_404(Article, pk=quillpost_id)
    quill_content_html = quillpost.content
    quill_posts = Article.objects.all().order_by('id')
    social_profiles = SocialMediaProfile.objects.all()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Correo enviado con éxito.'})
            return render(request, 'content/detail.html', {
                'quill_content_html': quill_content_html,
                'quillpost': quillpost,
                'quill_posts': quill_posts,
                'form': form,
                'success_message': 'Correo enviado con éxito.'
            })
    else:
        form = SubscriptionForm()

    return render(request, 'content/detail.html', {
        'quill_content_html': quill_content_html,
        'quillpost': quillpost,
        'quill_posts': quill_posts,
        'form': form,
        'success_message': '',  # Inicializar mensaje vacío
        'social_profiles': social_profiles,
    })