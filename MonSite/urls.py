
from django.contrib import admin
from django.urls import include, path
from .views import index

urlpatterns = [
    path('home/',index,name= 'home'),
    path('blog/', include('Blog.urls') ),
    path('admin/', admin.site.urls),
]
