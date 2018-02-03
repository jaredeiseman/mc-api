from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from api import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='Mamas Connect API')

router = routers.DefaultRouter()
router.register(r'test', views.TestModelViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url('admin/', admin.site.urls),
    url(r'^$', schema_view),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.jwt')),
]