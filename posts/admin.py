from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 3

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(Post, PostAdmin)