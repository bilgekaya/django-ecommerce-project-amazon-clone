from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from DjangoEcommerceApp import views, AdminViews
from DjangoEcommerce import settings

urlpatterns = [
    # Admin dashboard için alt URL'ler
    path('admindashboard/', include("DjangoEcommerceApp.adminurls")),

    # Admin giriş ve ana sayfa
    path('admin/login/', views.adminLogin, name='admin_login'),
    path('admin/home/', views.adminHome, name='admin_home'),

    # Burada diğer URL'ler eklenebilir
]

# Medya ve statik dosya ayarları (sadece geliştirme ortamı için uygun)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
