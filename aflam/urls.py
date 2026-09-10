"""
URL configuration for aflam project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from modrator import views

urlpatterns = [
    # 0. Auth Login direct path fix
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 1. Admin & Core
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('adminHome/', views.adminHome, name='adminHome'),
    path('settings/', views.settings_page, name='settings_page'),

    # 2. Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('signup/', views.signup, name='signup'),

    # 3. Categories & Types
    path('newCategory/', views.newCategory, name='newCategory'),
    path('categoryList/', views.categoryList, name='categoryList'),
    path('deleteCategory/<int:id>/', views.deleteCategory, name='deleteCategory'),
    
    path('newVideoType/', views.newVideoType, name='newVideoType'),
    path('videoTypeList/', views.typeList, name='typeList'),
    path('deleteVideoType/<int:id>/', views.deleteVideoType, name='deleteVideoType'),

    # 4. Series
    path('series/', views.series, name='series'),
    path('seriesList/', views.seriesList, name='seriesList'),
    path('newSeries/', views.newSeries, name='newSeries'),
    path('add-series/', views.add_series, name='add_series'),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    path('series/<int:series_id>/watch/', views.series_watch, name='series_watch'),
    path('editSeries/<int:series_id>/', views.editSeries, name='editSeries'),
    path('deleteSeries/<int:id>/', views.deleteSeries, name='deleteSeries'),

    # 5. Movies & Videos
    path('movies/', views.movies_list, name='movies_list'),
    path('newVideoItem/', views.newVideoItem, name='newVideoItem'),
    path('videosList/', views.videosList, name='videosList'),
    path('videos/<int:id>/', views.videoDetails, name='videoDetails'),
    path('deleteVideoItem/<int:id>/', views.deleteVideoItem, name='deleteVideoItem'),

    # 6. Search
    path('search/', views.search, name='search'),
    path('search/series/', views.search_series, name='search_series'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)