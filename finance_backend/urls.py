from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Finance Backend API Running 🚀")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/records/', include('records.urls')),
    path('api/users/', include('users.urls')),  # ✅ ADD THIS LINE
]