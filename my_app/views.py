from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import *
import requests



# 1-usul ko'rinish
# class IndexPageView(ListView):
# 	model = News
# 	template_name = 'index.html'
class UzbPageView(ListView):
	model = News
	template_name = 'uzb.html'

class AboutPageView(DetailView):
	model = News
	template_name = 'post_detail.html'

def indexPageView(request):
	yangilik = News.objects.all()
	context = {
	"yangiliklar":yangilik,

	}
	return render(request,'index.html',context)

# class CatePageView(TemplateView):
# 	template_name = 'category.html'

def catePageView(request, category_id):
	category_uchun = Category.objects.get(pk = category_id)
	yangilik = News.objects.filter(category_id = category_uchun)
	context = {
	"category_uchun": category_uchun,
	"yangilik": yangilik
	}
	return render(request, 'category.html', context)


# Create your views here.
