from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # YOUR PATTERNS
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger-UI : 개발자가 개발할 때 사용
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc : 기획자나 비개발자분들이 결과물 확인 시 사용
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    # REST API
    path('api/v1/video/', include('videos.urls'))
]

# docker-compose up