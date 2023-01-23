from django.contrib import admin
from .models import Blog, Comment


class CommentInLine(admin.StackedInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [CommentInLine, ]


admin.site.register(Blog, BlogAdmin)
# Register your models here.
