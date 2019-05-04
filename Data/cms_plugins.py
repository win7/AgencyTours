from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from Data.models import *

MODULE_NAME = "Go Plugin"

@plugin_pool.register_plugin
class SlidePlugin(CMSPluginBase):
    model = Slide
    name = _("Slide")
    render_template = "slide_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(SlidePlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class HeaderPlugin(CMSPluginBase):
    model = Header
    name = _("Header")
    render_template = "header_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(HeaderPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class TitlePlugin(CMSPluginBase):
    model = Title
    name = _("Title")
    render_template = "title_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(TitlePlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class BestServicePlugin(CMSPluginBase):
    model = Service
    name = _("Best Service")
    render_template = "best_service_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(BestServicePlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ServiceGridPlugin(CMSPluginBase):
    model = Service
    name = _("Service Grid")
    render_template = "service_grid_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        # context.update({'instance':instance})
        # context['instance'] = instance
        context = super(ServiceGridPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class ServiceListPlugin(CMSPluginBase):
    model = Service
    name = _("Service List")
    render_template = "service_list_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(ServiceListPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class LinksPlugin(CMSPluginBase):
    model = Link
    name = _("Link")
    render_template = "link_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(LinksPlugin, self).render(context, instance, placeholder)
        return context

@plugin_pool.register_plugin
class NewsPlugin(CMSPluginBase):
    model = News
    name = _("News")
    render_template = "news_plugin.html"
    module = MODULE_NAME
    cache = False

    def render(self, context, instance, placeholder):
        context = super(NewsPlugin, self).render(context, instance, placeholder)
        return context