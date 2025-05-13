from django.urls import path, include
from DjangoEcommerceApp import views  # views dosyasından gerekli import işlemi
from DjangoEcommerceApp import AdminViews  # AdminViews dosyasından gerekli import işlemi
from django.conf.urls.static import static
from DjangoEcommerce import settings  # settings.py dosyasına erişim için gerekli import

urlpatterns = [
    # Admin dashboard'a yönlendirme (DjangoEcommerceApp/adminurls.py içindeki URL'leri include et)
    path('admindashboard/', include("DjangoEcommerceApp.adminurls")),

    # Admin login ve home sayfaları için URL'ler
    path('admin/login/', views.adminLogin, name='admin_login'),  # Admin login sayfası
    path('admin/home/', views.adminHome, name='admin_home'),  # Admin home sayfası

    # Diğer URL'ler burada yer alabilir
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
