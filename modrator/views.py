from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from modrator.models import Series
from django.shortcuts import render
from .models import Movie, Series
from .models import Series
from django.contrib import admin
from .models import VideoItem
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.decorators import user_passes_test

# دالة لتحديد صلاحيات الأدمن
def admin_only(user):
    return user.is_staff or user.is_superuser



@user_passes_test(admin_only)
def settings_page(request):
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


def admin_only(user):
    return user.is_staff or user.is_superuser









def search(request):
    query = request.GET.get("q") 
    movies = []
    series = []

    if query:
        movies = Movie.objects.filter(title__icontains=query)  
        series = Series.objects.filter(title__icontains=query)  

    context = {
        "query": query,
        "movies": movies,
        "series": series,
    }
    return render(request, "search_results.html", context)


def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies_list.html', {'movies': movies})

def movies_list(request):
    return render(request, 'movies_list.html')

@login_required
def add_movie(request):
    return render(request, 'add_movie.html')




# Create your views here.
def adminHome(request):
    return render(request, 'AdminPanel/base.html')

def newCategory(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Category.objects.create(title=title)
        return redirect('newCategory')
    
    form = CategoryForm()
    context = {'form': form}
    return render(request, 'AdminPanel/new-category.html', context)



def categoryList(request):
    categores = Category.objects.all()
    context = {'categores': categores}
    return render(request, 'AdminPanel/category-list.html', context)

def newVideoType(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        VideoType.objects.create(title=title)
        return redirect('newVideoType')
    
    form = VideoTypeForm()
    context = {'form': form} 
    return render(request, 'AdminPanel/newType.html', context)

def typeList(request):
    Types = VideoType.objects.all()
    context = {'Types': Types}
    return render(request, 'AdminPanel/typeList.html', context)

@user_passes_test(admin_only)
def newSeries(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('newSeries')
    
        
    form = SeriesForm()
    context = {'form': form} 
    return render(request, 'AdminPanel/newSeries.html', context)

def seriesList(request):
    allSeries = Series.objects.all()
    context = {'Series': allSeries}
    return render(request, 'AdminPanel/seriesList.html', context)

@user_passes_test(admin_only)
def newVideoItem(request):
    if request.method == 'POST':
        form = VideoItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('videosList')
    
    else:
        form = VideoItemForm()
    context = {'form': form} 
    return render(request, 'AdminPanel/newVideo.html', context)


    
@user_passes_test(admin_only)
def deleteCategory(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categoryList')

@user_passes_test(admin_only)
def deleteSeries(request, id):
    series = get_object_or_404(Series, id=id)
    
    
    VideoItem.objects.filter(series=series).delete()
    
    
    series.delete()
    
    return redirect('seriesList')


@user_passes_test(admin_only)
def deleteVideoType(request, id):
    videoType = VideoType.objects.get(id=id)
    videoType.delete()
    return redirect('videoTypeList')



def videosList(request):
    videos = VideoItem.objects.all()
    context = {'videos': videos}
    return render(request, 'AdminPanel/videosList.html', context)

@user_passes_test(admin_only)
def deleteVideoItem(request, id):
    videoItem = VideoItem.objects.get(id=id)
    videoItem.delete()
    return redirect('videosList')


def videoDetails(request, id):
    video = VideoItem.objects.get(id=id)
    context = {'video': video}
    return render(request, 'AdminPanel/videoDetails.html', context)



def seriesList(request):
    search_query = request.GET.get('title', '')
    if search_query:
        series_list = Series.objects.filter(title__icontains=search_query)
    else:
        series_list = Series.objects.all()
        
    context = {
        'series_list': series_list,
        'search_query': search_query
    }
    return render(request, 'AdminPanel/seriesList.html', context)







def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})





def home(request):
    return render(request, 'AdminPanel/base.html') 



















def editSeries(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES, instance=series)
        if form.is_valid():
            form.save()
            messages.success(request, 'Series updated successfully!')
            return redirect('seriesList')
    else:
        form = SeriesForm(instance=series)
    return render(request, 'AdminPanel/editSeries.html', {'form': form})



def series(request):
    series_list = Series.objects.all()
    return render(request, 'AdminPanel/series.html', {'series_list': series_list})




def series_detail(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    return render(request, 'AdminPanel/series_detail.html', {'series': series})



def add_series(request):
    if request.method == 'POST':
        form = SeriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_series')  # بعد الحفظ يرجع لقائمة المسلسلات
    else:
        form = SeriesForm()

    return render(request, 'AdminPanel/add_series.html', {'form': form})




def series_watch(request, series_id):

    series = get_object_or_404(Series, id=series_id)
    return render(request, 'AdminPanel/series_watch.html', {'series': series})



def deleteSeries(request, id):
    series = get_object_or_404(Series, id=id)
    series.delete()
    # بعد الحذف، رجّعه على قائمة المسلسلات بدل صفحة التفاصيل
    return redirect('seriesList')

def search(request):
    q = request.GET.get('q', '')
    videos = VideoItem.objects.filter(title__icontains=q)
    context = {
        'videos': videos,
        'query': q
    }
    return render(request, 'AdminPanel/search_results.html', context)





def series_list(request):
    query = request.GET.get('q', '')  # نستقبل نص البحث
    if query:
        # البحث في العنوان فقط، ممكن تضيف description كمان
        series_list = Series.objects.filter(title__icontains=query)
        if not series_list.exists():
            error_message = f"No series found for '{query}'"
        else:
            error_message = None
    else:
        series_list = Series.objects.all()
        error_message = None

    context = {
        'series_list': series_list,
        'error_message': error_message,
        'query': query
    }
    return render(request, 'series_list.html', context)



def search_series(request):
    query = request.GET.get('q', '').strip()

    if query:
        # نبحث عن كل المسلسلات اللي تحتوي على النص المكتوب (بدون حساسية لحالة الحروف)
        series_list = Series.objects.filter(title__icontains=query)

        if series_list.exists():
            # لو لقينا نتائج، نعرضها في القالب
            return render(request, 'AdminPanel/search_series.html', {
                'series_list': series_list,
                'query': query
            })
        else:
            # لو مفيش نتائج
            return render(request, 'AdminPanel/search_series.html', {
                'series_list': [],
                'query': query
            })
    else:
        # لو المستخدم ضغط بحث بدون ما يكتب حاجة
        return render(request, 'AdminPanel/search_series.html', {
            'series_list': [],
            'query': ''
        })




@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def deleteSeries(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    series.delete()
    messages.success(request, "✅ تم حذف المسلسل بنجاح.")
    return redirect('seriesList')


@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def deleteVideo(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    messages.success(request, "✅ تم حذف الفيديو بنجاح.")
    return redirect('videosList')

