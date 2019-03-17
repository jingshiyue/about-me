"""drf_about URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, urls

from about_api import views
from rest_framework.documentation import include_docs_urls
router = routers.DefaultRouter()

router.register(r'base_info', views.Base_info_viewset)
router.register(r'pro_info', views.Project_info_view)
router.register(r'certificate_info', views.Certificate_view)
router.register(r'stack_info', views.Stack_view)
router.register(r'tech_info', views.Tech_view)
# router.register(r'message_info', views.Message_view)
router.register(r'action_num', views.Action_num_view)
router.register(r'visite_num', views.Visite_num_view)
router.register(r'self_intro',views.Self_intro_view)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/edu_info/', views.Edu_info_view.as_view(), name='edu_info'),
    path('api/job_info/', views.Job_info_view.as_view(), name='job_info'),
    path('api/job_want/', views.Job_want_view.as_view(), name='job_want'),
    # path('certificate/', views.Certificate_view.as_view(), name='certificate'),
    # path('pro_info/', views.Project_info_view.as_view({'post':'create'}), name='pro_info'),
    path('api/message_info/', views.Message_view.as_view(), name='messagge_info'),
    path(r'api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='about'))
]
