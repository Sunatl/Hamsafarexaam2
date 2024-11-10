from django.contrib import admin
from .models import *

@admin.register(CompanionRequest)
class Co(admin.ModelAdmin):
    list_display = ("user","start_location","end_location")
    search_fields =  ("user__username","start_location","end_location")
    list_filter =  ("user","start_location","end_location")
    
@admin.register(User)
class Us(admin.ModelAdmin):
    list_display = ("fullname","phone","username")
    search_fields =  ("fullname","phone","username")
    list_filter =  ("fullname","phone","username")

@admin.register(Trip)
class Tr(admin.ModelAdmin):
    list_display = ("user","start_location","end_location")
    search_fields =  ("user__username","start_location","end_location")
    list_filter =  ("user","start_location","end_location")
