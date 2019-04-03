from django.urls import path, include
from rest_framework import routers
from . import views, gdbConn

router = routers.DefaultRouter()

# 注册到router.urls中
router.register(r'users', views.UserViewSet)    # 通过/api/users访问
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('start', gdbConn.start),      # 转到 gdbConn.py 中的 start 函数
    path('continue', gdbConn.contin),
]
