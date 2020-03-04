from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from ..models import Book


def update(request, book_id):
    template_name = 'update.html'

    if request.method == 'GET':
        bt = Book.objects.values(
            'id',
            'title',
            'author',
            'publisher',
            'finished_date'
        ).get(id=book_id)
        return render(request, template_name, bt)
    elif request.method == 'POST':
        update_bt = Book.objects.get(id=book_id)
        update_bt.title = request.POST['title']
        update_bt.author = request.POST['author']
        update_bt.publisher = request.POST['publisher']
        update_bt.finished_date = request.POST['finished_date']
        update_bt.updated_at = timezone.now()

        try:
            update_bt.save()
        except Exception:
            messages.error(request, f'更新に失敗しました')
            redirect('haw:top')

        return redirect('haw:top')
