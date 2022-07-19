from django.urls import path
from .views import indexPageView, AboutPageView, UzbPageView, catePageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', indexPageView, name = 'index'),
    path('uzb/', UzbPageView.as_view(), name = 'uzb'),
    path('category/<int:category_id>/', catePageView,  name = 'category'),
    # path('about/',AboutPageView.as_view(), name = 'post_detail')
    path('post_detail/<int:pk>/',AboutPageView.as_view(), name = 'post_detail')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)