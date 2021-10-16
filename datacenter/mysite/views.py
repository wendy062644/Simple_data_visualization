from django.shortcuts import render
from django.http import HttpResponse
from .scrapers import CDC
from .water import water

from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'

def home(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    return render(request, 'about/about.html')

def spidercovid(request):
 
    CDCinfor = CDC(request.POST.get("test"))
 
    context = {
        "disease": CDCinfor.scrape()
    }
 
    return render(request, "spidercovid-19/spidercovid-19.html", context)

def spiderwater(request):
 
    waterinfor = water(request.POST.get("water"))
 
    infor = {
        "dam": waterinfor.scrape()
    }
    return render(request, "spiderwater/spiderwater.html", infor)

def profile(request):
    return render(request, "profile/profile.html")

def test(request):
    return render(request, "test.html")

def test123(request):
    print("前端資料: ", request.POST)
    print("file:", request.FILES)

    for item in request.FILES:
        obj = request.FILES.get(item)      # 獲取要寫入的檔案
        filename = obj.name            # 獲取檔名
        f = open(filename, 'wb')
        for line in obj.chunks():      # 分塊寫入
            f.write(line)
        f.close()

    return render(request, "test123.html")

def work(request):
    return render(request, "work/work.html")

def share(request):
    return render(request, "share/share.html")

def work(request):
    return render(request, "work/work.html")

def article1(request):
    return render(request, "share/article1.html")
