
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Book
from .forms import BookForm



class BookListView(ListView):
    model=Book
#    paginate_by = 20
    template_name='dbook/book_list.html'

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

