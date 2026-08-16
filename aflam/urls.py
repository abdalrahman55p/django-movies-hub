"""
URL configuration for aflam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import modrator.views
from django.urls import path
from modrator import views
from django.shortcuts import redirect





    
    
urlpatterns = [

   path('settings/', views.settings_page, name='settings_page'),


    
    path('search/', views.search, name='search'),


    
    path('admin/', admin.site.urls),

     path('', modrator.views.home, name='home'),

    path('adminHome/', modrator.views.adminHome, name='adminHome'),

    path('accounts/', include('django.contrib.auth.urls')),

     path('signup/', modrator.views.signup, name='signup'),

     path('accounts/', include('allauth.urls')),

     path('movies/', modrator.views.movies_list, name='movies_list'),

     path('search/', modrator.views.search, name='search'),


     
      path('admin/', modrator.views.adminHome, name='adminHome'),

      
    
    
    



      path('newCategory/', modrator.views.newCategory, name='newCategory'),
      path('categoryList/', modrator.views.categoryList, name='categoryList'),
      path('deleteCategory/<int:id>', modrator.views.deleteCategory, name='deleteCategory'),


        

      path('newSeries/', modrator.views.newSeries, name='newSeries'),
      path('seriesList/', modrator.views.seriesList, name='seriesList'),



      


      
    
     path('editSeries/<int:id>/', modrator.views.editSeries, name='editSeries'),


    

      path('newVideoType/', modrator.views.newVideoType, name='newVideoType'),
      path('deleteVideoType/<int:id>', modrator.views.deleteVideoType, name='deleteVideoType'),
      path('videoTypeList/', modrator.views.typeList, name='videoTypeList'),



     path('newVideoItem/', modrator.views.newVideoItem, name='newVideoItem'),
      path('deleteVideoItem/<int:id>', modrator.views.deleteVideoItem, name='deleteVideoItem'),
      path('videosList/', views.videosList, name='videosList'),
      path('videosList/<int:id>', modrator.views.videoDetails, name='videoDetails'),
      #path('deleteVideoItem/', modrator.views.newVideoItem, name='newVideoItem'),


    
   
    path('series/', views.series, name='series'),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    path('add-series/', views.add_series, name='add_series'),
    path('series/<int:series_id>/watch/', views.series_watch, name='series_watch'),
    
    # صحح اسم الـ parameter ليطابق view
    path('deleteSeries/<int:series_id>/', views.deleteSeries, name='deleteSeries'),


   path('deleteVideo/<int:video_id>/', views.deleteVideo, name='deleteVideo'),

    
    path('series/', views.series_list, name='series'),
    path('search/series/', views.search_series, name='search_series'),




    
    






]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    


    # أثناء التطوير (localhost)
    urlpatterns += [
     path('', lambda request: redirect('/admin/')),  # يفتح لوحة التحكم مباشرة
    ]

    

    # في بيئة الإنتاج (Production)
    urlpatterns += [
        path('', lambda request: redirect('/admin/')),  # يحوّل للموقع الحقيقي
    ]

