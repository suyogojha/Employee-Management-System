


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from APP import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('json/', views.employee_json, name='employee_json'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
