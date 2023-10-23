from django.contrib import admin
from django.db.models import Count
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  def comment_count(self, obj):
     return obj.comment_count
  comment_count.admin_order_field = 'comment_count'

  def get_queryset(self, request):
     queryset = super().get_queryset(request)
     queryset = queryset.annotate(comment_count=Count("comments"))
     return queryset
  list_display = ('title', 'slug', 'author', 'comment_count', 'publish', 'status')
  list_filter = ('status', 'created', 'publish', 'author')
  search_fields = ('title', 'body')
  prepopulated_fields = {'slug': ('title',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'post', 'created', 'active')
  list_filter = ('active', 'created', 'updated')
  search_fields = ('name', 'email', 'body')