from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Course, Category

def main(request):
    return render(request, 'index.html')


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'detail.html'
    context_object_name = 'course'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
            

class CategoryListPage(ListView):
    model = Category
    template_name = 'categorylist.html'
    # paginate_by = 100  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context