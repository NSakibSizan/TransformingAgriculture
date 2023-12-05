from django.urls import path
from crop_predictor import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'crop_predictor'

urlpatterns = [
    path('', views.crop_prediction, name='crop_prediction'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
