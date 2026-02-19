from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from . import models, forms


class BookCitationsView(View):
    def get(self, request):
        return HttpResponse('«Вы никогда не переплывете океан, если не отчалите от берега», — Христофор Колумб')


class SearchBookView(View):
    def get(self, request):
        query = request.GET.get('s', '')
        if query:
            book = models.Book.objects.filter(title__icontains=query)
        else:
            book = models.Book.objects.none()
        
        return render(
            request,
            'book.html',
            {
                'book': book
            }
        )


class BookDetailView(DetailView):
    model = models.Book
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    pk_url_kwarg = 'id'


class BookListView(ListView):
    model = models.Book
    template_name = 'book.html'
    context_object_name = 'book'
    paginate_by = 2
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['paginator'].get_page(self.request.GET.get('page'))
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = context['page_obj']
        return context


class UpdateBookView(UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'update_book.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('books:book_user')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_id'] = self.object
        return context


class CreateBookView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'create_book.html'
    success_url = reverse_lazy('books:book_user')


class DeleteBookView(DeleteView):
    model = models.Book
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('books:book_user')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)