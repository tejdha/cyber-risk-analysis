from django.urls import path
from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'logsss', LogViewSet, basename='logsss')

urlpatterns=[
    path('logs/',get_logs),
    path('logs/create/',create_logs),
    path('logs/<int:hp>/',get_log),
    path('logs/<int:hp>/update/',update_log),
    path('logs/<int:hp>/delete/',delete_log),
    path('login/',login_view),
    path('logout/',logout_view),
    path('logsss/', include(router.urls)),
    path('logs/summary/',log_summary_view),
    path('logs/recent/',recent_logs_view),
    # path('home/',home),

]