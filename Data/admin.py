# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("id", "title")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    filter_horizontal=("itinerary", "suggestion")

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title")