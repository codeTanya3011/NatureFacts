from django.shortcuts import render, redirect
from django.views.generic.base import View

from .form import CommentsForm
from .models import Publication, Likes


class PublicationView(View):
    def get(self, request):
        publication = Publication.objects.all()
        return render(request, 'project/project_django.html', {'publication_list': publication})


class SingleEntry(View):
    def get(self, request, pk):
        single = Publication.objects.get(id=pk)
        return render(request, 'project/single_entry.html', {'single': single})


class AddComment(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_user = get_user_ip(request)
        try:
            Likes.objects.get(ip=ip_user, posts_id=pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_user
            new_like.posts_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class DeleteLike(View):
    def get(self, request, pk):
        ip_user = get_user_ip(request)
        try:
            like = Likes.objects.get(ip=ip_user)
            like.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')