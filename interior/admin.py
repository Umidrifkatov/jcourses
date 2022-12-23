from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Category, CategoryAdmin)




class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','img',)
    list_editable =('img',)
admin.site.register(Author, AuthorAdmin)


class CourseImageInline(admin.StackedInline):
    model = CourseImage
    extra = 0

class PostCourseImageInline(admin.StackedInline):
    model = PostCourseImage
    extra = 0

class CourseAdmin(admin.ModelAdmin):
    list_display = ('shorttitle', 'startdate','author', 'category', 'ended', 'recomended')
    list_editable = ('recomended','ended',)
    inlines = [
        CourseImageInline, PostCourseImageInline,
    ]
admin.site.register(Course, CourseAdmin)