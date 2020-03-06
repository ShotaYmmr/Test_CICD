from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone
from ..models import Book


def create(request):
    template_name = 'create.html'

    if not request.POST:
        return render(request, template_name)
    else:
        tb = Book(
            title=request.POST['title'],
            author=request.POST['author'],
            publisher=request.POST['publisher'],
            finished_date=request.POST['finished_date'],
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        try:
            tb.save()
        except Exception:
            messages.error(request, f'登録に失敗しました')
            redirect('haw:top')

        return redirect('haw:top')
