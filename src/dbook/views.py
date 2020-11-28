
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Book
from .forms import BookForm
from dbase.models import Genre



class BookListView(ListView):
    model=Book
#    paginate_by = 20
    template_name='dbook/book_list.html'

class BookGView(ListView):
    model=Book
    template_name='dbook/book_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        g_id = self.request.GET.get('genre')
        g = Genre.objects.get(pk=g_id)
        g_book = g.books.all()
        context['object_list'] = g_book
        return super().get_context_data(**context)

class BookDetailView(DetailView):
    model=Book
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get(self.pk_url_kwarg)
        book =  Book.objects.get(pk=pk)
        context['form'] = BookForm(instance=book)
        return context
    
class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/book'
    model=Book
    fields='__all__'
    template_name = 'dbook/book_create.html'
    success_url = '/book'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    redirect_field_name = '/book'
    model=Book
    success_url = '/book'

def delete(self, request, *args, **kwargs):
    """
    Call the delete() method on the fetched object and then redirect to the
    success URL.
    """
    self.object = self.get_object()
    success_url = self.get_success_url()
    
    self.object.image.storage.delete()
    self.object.delete()

    return HttpResponseRedirect(success_url)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/book'
    model=Book
    fields = '__all__'
    success_url = '/book'
    template_name = 'dbook/book_create.html'

