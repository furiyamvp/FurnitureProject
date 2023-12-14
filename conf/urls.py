from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pages.urls", namespace="pages")),
    path('contact/', include("pages.urls", namespace="contact")),
    path('blog/', include("pages.urls", namespace="blog")),
    path('about/', include("pages.urls", namespace="about")),
    path('products/', include("pages.urls", namespace="products"))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

