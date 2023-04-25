from django.urls import path
from .views import AdvertList, AdvertDetail


urlpatterns = [
    path('', AdvertList.as_view(), name='advert-list'),
    path('<slug:category>/<slug:slug>/', AdvertDetail.as_view(), name='advert-detail')
]