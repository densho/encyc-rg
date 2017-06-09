# -*- coding: utf-8 -*-
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import api
from . import views

urlpatterns = [
    url(r'^debug/', views.debug, name='rg-debug'),
    
    url(r"^api/1.0/browse/categories/(?P<category>[\w\W]+)/$", api.category, name='rg-api-category'),
    url(r"^api/1.0/browse/categories/$", api.categories, name='rg-api-categories'),
    url(r"^api/1.0/browse/(?P<fieldname>[\w\W]+)/(?P<value>[\w\W]+)/$", api.browse_field_value, name='rg-api-browse-fieldvalue'),
    url(r"^api/1.0/browse/(?P<fieldname>[\w\W]+)/$", api.browse_field, name='rg-api-browse-field'),
    url(r"^api/1.0/browse/$", api.browse, name='rg-api-browse'),
    url(r"^api/1.0/articles/(?P<url_title>[\w\W]+)/$", api.article, name='rg-api-article'),
    url(r"^api/1.0/authors/(?P<url_title>[\w\W]+)/$", api.author, name='rg-api-author'),
    url(r"^api/1.0/sources/(?P<url_title>[\w\W]+)/$", api.source, name='rg-api-source'),
    
    url(r"^api/1.0/articles/$", api.articles, name='rg-api-articles'),
    url(r"^api/1.0/authors/$", api.authors, name='rg-api-authors'),
    url(r"^api/1.0/sources/$", api.sources, name='rg-api-sources'),
    url(r"^api/1.0/search/$", api.search.as_view(), name='rg-api-search'),
    
    url(r"^articles/(?P<url_title>[\w\W]+)/$", views.article, name='rg-article'),
    url(r"^authors/(?P<url_title>[\w\W]+)/$", views.author, name='rg-author'),
    url(r"^categories/(?P<url_title>[\w\W]+)/$", views.category, name='rg-category'),
    url(r"^sources/(?P<url_title>[\w\W]+)/$", views.source, name='rg-source'),
    
    url(r"^articles/$", views.articles, name='rg-articles'),
    url(r"^authors/$", views.authors, name='rg-authors'),
    url(r"^categories/$", views.categories, name='rg-categories'),
    url(r"^sources/$", views.sources, name='rg-sources'),
    
    url(r'^api/1.0/$', api.index, name='rg-api-index'),
    url(r'^$', views.Index.as_view(), name='rg-index'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

handler400 = views.Error400.as_view()
handler403 = views.Error403.as_view()
handler404 = views.Error404.as_view()
handler500 = views.Error500.as_view()
