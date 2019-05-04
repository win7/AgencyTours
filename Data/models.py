# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models.pluginmodel import CMSPlugin
from cms.models import *
from cms.models.fields import PlaceholderField
from cms.models.fields import PageField
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from filer.fields.image import FilerImageField

# Create your models here.

@python_2_unicode_compatible
class Itinerary(models.Model):
    title = models.CharField("Title", unique=True, max_length=100)
    description = models.CharField("Description", max_length=500)

    class Meta:
        ordering = ('title', )
        verbose_name = ('Itinerary')
        verbose_name_plural = ('Itineraries')
    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Suggestion(models.Model):
    title = models.CharField("Title", unique=True, max_length=100)
    description = models.CharField("Description", max_length=500)

    class Meta:
        ordering = ('title', )
        verbose_name = ('Suggestion')
        verbose_name_plural = ('Suggestions')
    def __str__(self):
        return self.title
        
@python_2_unicode_compatible
class Slide(CMSPlugin):
    title = models.CharField("Title", max_length=100)
    subtitle = models.CharField("Sub title", max_length=100)
    description = models.TextField("Description", max_length=200)
    image = FilerImageField(verbose_name=('Image'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')

    class Meta:
        ordering = ('title', )
        verbose_name = ('Slide')
        verbose_name_plural = ('Slides')
    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Header(CMSPlugin):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description", max_length=200)
    image = FilerImageField(verbose_name=('Image'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')

    class Meta:
        ordering = ('title', )
        verbose_name = ('Header')
        verbose_name_plural = ('Headers')
    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Title(CMSPlugin):
    title = models.CharField("Title", max_length=100)
    title2 = models.CharField("Title", max_length=100) #ojo
    description = models.TextField("Description", max_length=200)
    
    class Meta:
        ordering = ('title', )
        verbose_name = ('Title')
        verbose_name_plural = ('Titles')
    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Service(CMSPlugin):
    title = models.CharField("Title", max_length=100, unique=False)
    sub_title = models.CharField("Sub Title", max_length=500)
    description = models.TextField("Description", max_length=1000)
    location = models.CharField("Location", max_length=100)
    latitude = models.FloatField("Latitude", default=0)
    longitude = models.FloatField("Longitude", default=0)
    price = models.FloatField("Price", default=0)
    day = models.IntegerField("N° Days", default=1)
    night = models.IntegerField("N° Nights", default=1)
    max_people = models.IntegerField("Max. People", default=0)
    ranking = models.BooleanField("Ranking", default=False)
    publish = models.BooleanField("Publish", default=False)
    image1 = FilerImageField(verbose_name=('Image1'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')
    image2 = FilerImageField(verbose_name=('Image2'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')
    image3 = FilerImageField(verbose_name=('Image3'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')
    itinerary = models.ManyToManyField(Itinerary, verbose_name="Itinerary")
    suggestion = models.ManyToManyField(Suggestion, verbose_name="Suggestion")
    #include
    page = PageField(
        verbose_name=('Internal URL'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=('Wraps the image in a link to an internal (page) URL.'),
    )
    # descuento
    class Meta:
        ordering = ('title', )
        verbose_name = ('Service')
        verbose_name_plural = ('Services')

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class News(CMSPlugin):
    title = models.CharField("Title", max_length=100)
    sub_title = models.TextField("Sub Title", max_length=500)
    description = models.TextField("Description", max_length=1000)
    date = models.DateField("Date", auto_now=False)
    owner = models.CharField("Owner", max_length=100)
    url = models.URLField("URL", max_length=50)
    image = FilerImageField(verbose_name=('Image'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')
    video = models.FileField("Video", upload_to='news', blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name = ('News')
        verbose_name_plural = ('News')

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Link(CMSPlugin):
    title = models.CharField("Title", max_length=100)
    sub_title = models.TextField("Sub Title", max_length=500)
    description = models.TextField("Description", max_length=1000)
    price = models.FloatField("Price", default=0)
    url = models.URLField("URL", max_length=50)
    image = FilerImageField(verbose_name=('Image'), blank=True, null=True, on_delete=models.SET_NULL,related_name='+')
    video = models.FileField("Video", upload_to='news', blank=True, null=True)

    class Meta:
        ordering = ('title', )
        verbose_name = ('Link')
        verbose_name_plural = ('Links')
    def __str__(self):
        return self.title
