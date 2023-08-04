from django.contrib import admin
from blogs.models import Blog,Category
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','user','status','date']
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    readonly_fields = ['title','user','date','content','categories','status','blog_image']
    # search_fields = ['']
    # ordering = ['']
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category_user']
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    
    
