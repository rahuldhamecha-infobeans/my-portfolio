from django.contrib import admin
from portfolio.services.models import Service
from portfolio.models import Portfolio, PortfolioCategory, Testimonial, Subscriber, Contact


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'service_description','service_image_tag']
    search_fields = ['service_name', 'service_description']
    ordering = ['service_name']
    list_per_page = 10


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name','category','portfolio_image']
    list_per_page = 10
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    
@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name','position','content']
    ordering = ['id']
    list_per_page = 10
    

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email','is_subscribe']
    list_filter = ['is_subscribe']
    list_per_page = 10
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','created_date']
    list_per_page = 10
    # list_filter = ['']
    # fields = ['']
    # inlines = []
    # raw_id_fields = ['']
    # readonly_fields = ['']
    # search_fields = ['']
    # ordering = ['']
    