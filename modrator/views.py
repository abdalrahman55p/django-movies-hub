from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

from .models import VideoItem, Category, VideoType, Series, Movie, SiteSettings
from .forms import CategoryForm, VideoTypeForm, SeriesForm, VideoItemForm


# 1. دالة الصلاحيات المشددة (التحقق من حساب الأدمن + حماية الحساب)
def admin_or_super_only(user):
    # يلزم أن يكون المستخدم مسجلاً لدخوله وأن يمتلك صلاحيات Superuser أو Staff
    return user.is_authenticated and (user.is_superuser or user.is_staff)


# دالة فحص جهاز المستخدم (مستندة للعنوان المحلي لجهازك)
def restrict_to_local_device(request):
    client_ip = request.META.get('REMOTE_ADDR')
    # يمنع الوصول إذا لم يكن الطلب قادماً من جهازك محلياً
    if client_ip not in ['127.0.0.1', 'localhost', '::1']:
        raise PermissionDenied("غير مسموح بالدخول أو إجراء عمليات التعديل من هذا الجهاز.")


# 2. الإعدادات والصفحة الرئيسية
@user_passes_test(admin_or_super_only)
def settings_page(request):
    restrict_to_local_device(request)
    settings = SiteSettings.objects.first() or SiteSettings.objects.create()
    if request.method == "POST":
        settings.site_name = request.POST.get("site_name")
        settings.site_url = request.POST.get("site_url")
        settings.contact_email = request.POST.get("contact_email")
        settings.phone = request.POST.get("phone")
        settings.dark_mode = request.POST.get("dark_mode")
        settings.site_description = request.POST.get("site_description")
        if 'logo' in request.FILES:
            settings.logo = request.FILES['logo']
        settings.save()
        messages.success(request, "✅ تم حفظ الإعدادات بنجاح")
        return redirect('settings_page')
    return render(request, 'AdminPanel/settings.html', {"settings": settings})


def home(request):
    return redirect('adminHome')


@user_passes_test(admin_or_super_only)
def adminHome(request):
    restrict_to_local_device(request)
    return render(request, 'AdminPanel/base.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# 3. إدارة التصنيفات (Category)
@user_passes_test(admin_or_super_only)
def newCategory(request):
    restrict_to_local_device(request)
    if request.method == 'POST':
        title = request.POST.get('title')
        Category.objects.create(title=title)
        return redirect('newCategory')
    form = CategoryForm()
    return render(request, 'AdminPanel/new-category.html', {'form': form})


def categoryList(request):
    categores = Category.objects.all()
    return render(request, 'AdminPanel/category-list.html', {'categores': categores})


@user_passes_test(admin_or_super_only)
def deleteCategory(request, id):
    restrict_to_local_device(request)
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categoryList')


# 4. إدارة أنواع الفيديوهات (VideoType)
@user_passes_test(admin_or_super_only)
def newVideoType(request):
    restrict_to_local_device(request)
    if request.method == 'POST':
        title = request.POST.get('title')
        VideoType.objects.create(title=title)
        return redirect('newVideoType')
    form = VideoTypeForm()
    return render(request, 'AdminPanel/newType.html', {'form': form})


def typeList(request):
    Types = VideoType.objects.all()
    return render(request, 'AdminPanel/typeList.html', {'Types': Types})


@user_passes_test(admin_or_super_only)
def deleteVideoType(request, id):
    restrict_to_local_device(request)
    videoType = get_object_or_404(VideoType, id=id)
    videoType.delete()
    return redirect('videoTypeList')


# 5. إدارة الفيديوهات (VideoItem)
def videosList(request):
    videos = VideoItem.objects.all()
    return render(request, 'AdminPanel/videosList.html', {'videos': videos})


@user_passes_test(admin_or_super_only)
def newVideoItem(request):
    restrict_to_local_device(request)
    if request.method == 'POST':
        form = VideoItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إضافة الفيديو بنجاح.")
            return redirect('videosList')
        else:
            print("Errors in newVideoItem:", form.errors)
            messages.error(request, f"خطأ في حفظ الفيديو: {form.errors}")
    else:
        form = VideoItemForm()
    return render(request, 'AdminPanel/newVideo.html', {'form': form})


def videoDetails(request, id):
    video = get_object_or_404(VideoItem, id=id)
    
    url = getattr(video, 'trailer_url', None) or getattr(video, 'video_url', None) or getattr(video, 'url', None)
    
    embed_url = None
    if url:
        if 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[1].split('?')[0]
            embed_url = f"https://www.youtube.com/embed/{video_id}"
        elif 'watch?v=' in url:
            video_id = url.split('watch?v=')[1].split('&')[0]
            embed_url = f"https://www.youtube.com/embed/{video_id}"
        elif 'embed/' in url:
            embed_url = url
        else:
            embed_url = url

    context = {
        'video': video,
        'embed_url': embed_url
    }
    return render(request, 'AdminPanel/videoDetails.html', context)


@user_passes_test(admin_or_super_only)
def deleteVideoItem(request, id):
    restrict_to_local_device(request)
    videoItem = get_object_or_404(VideoItem, id=id)
    videoItem.delete()
    return redirect('videosList')


@user_passes_test(admin_or_super_only)
def deleteVideo(request, video_id):
    restrict_to_local_device(request)
    video = get_object_or_404(VideoItem, id=video_id)
    video.delete()
    messages.success(request, "✅ تم حذف الفيديو بنجاح.")
    return redirect('videosList')


# 6. إدارة المسلسلات (Series)
@user_passes_test(admin_or_super_only)
def newSeries(request):
    restrict_to_local_device(request)
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إضافة المسلسل بنجاح.")
            return redirect('seriesList')
        else:
            print("Errors in newSeries:", form.errors)
            messages.error(request, f"خطأ في حفظ البيانات: {form.errors}")
    else:
        form = SeriesForm()
    return render(request, 'AdminPanel/newSeries.html', {'form': form})


def seriesList(request):
    search_query = request.GET.get('title', '')
    if search_query:
        series_list = Series.objects.filter(title__icontains=search_query)
    else:
        series_list = Series.objects.all()
    return render(request, 'AdminPanel/seriesList.html', {'Series': series_list, 'series_list': series_list, 'search_query': search_query})


@user_passes_test(admin_or_super_only)
def editSeries(request, id):
    restrict_to_local_device(request)
    series = get_object_or_404(Series, id=id)
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES, instance=series)
        if form.is_valid():
            form.save()
            messages.success(request, 'Series updated successfully!')
            return redirect('seriesList')
        else:
            print("Errors in editSeries:", form.errors)
            messages.error(request, f"خطأ في التعديل: {form.errors}")
    else:
        form = SeriesForm(instance=series)
    return render(request, 'AdminPanel/editSeries.html', {'form': form})


def series(request):
    series_list = Series.objects.all()
    return render(request, 'AdminPanel/series.html', {'series_list': series_list})


def series_detail(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    return render(request, 'AdminPanel/series_detail.html', {'series': series})


@user_passes_test(admin_or_super_only)
def add_series(request):
    restrict_to_local_device(request)
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إضافة المسلسل بنجاح.")
            return redirect('seriesList')
        else:
            print("Errors in add_series:", form.errors)
            messages.error(request, f"خطأ في حفظ البيانات: {form.errors}")
    else:
        form = SeriesForm()
    return render(request, 'AdminPanel/add_series.html', {'form': form})


def series_watch(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    return render(request, 'AdminPanel/series_watch.html', {'series': series})


@user_passes_test(admin_or_super_only)
def deleteSeries(request, id):
    restrict_to_local_device(request)
    series = get_object_or_404(Series, id=id)
    series.delete()
    messages.success(request, "✅ تم حذف المسلسل بنجاح.")
    return redirect('seriesList')


# 7. الأفلام والبحث (Movies & Search)
def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', {'movies': movies})


@user_passes_test(admin_or_super_only)
def add_movie(request):
    restrict_to_local_device(request)
    return render(request, 'add_movie.html')


def search(request):
    q = request.GET.get('q', '')
    videos = VideoItem.objects.filter(title__icontains=q)
    return render(request, 'AdminPanel/search_results.html', {'videos': videos, 'query': q})


def search_series(request):
    query = request.GET.get('q', '').strip()
    series_list = Series.objects.filter(title__icontains=query) if query else []
    return render(request, 'AdminPanel/search_series.html', {'series_list': series_list, 'query': query})