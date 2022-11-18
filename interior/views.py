from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Course, Category

def main(request):
    return render(request, 'index.html')



# def detail(request, pk):
#     return render(request, 'detail.html')



class CourseDetailPage(DetailView):
    model = Course
    template_name = 'detail.html'
    context_object_name = 'course'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
            



# class ProductDetailPage(DetailView):
#     model = Product
#     template_name = 'pages/product-detail.html'
#     context_object_name = 'product'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = ParentCategory.objects.all()
#         return context