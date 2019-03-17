from django.core.mail import send_mail
from django.views import View
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     GenericAPIView, ListAPIView,
                                     RetrieveAPIView, UpdateAPIView)
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import (Action_num, Base_info, Certificate, Edu_info, Job_info,
                     Job_want, Message, Project_info, Stack, Tech, Visite_num, Self_intro)
from .my_filters import Stander_filter
from .my_pagination import Stander_pagination
from .serializers import (Action_num_serializer, Base_info_serializer,
                          Certificate_serializer, Edu_info_serializer,
                          Job_info_serializer, Job_want_serializer,
                          Message_serializer, Project_info_serializer,
                          Stack_serializer, Tech_serializer,
                          Visite_num_serializer, Self_intro_serializer)
                          
# Create your views here.

# 官方demo。
# 方法0：viewsets


class Base_info_viewset(viewsets.ReadOnlyModelViewSet):
    '''
    '''
    queryset = Base_info.objects.all()
    serializer_class = Base_info_serializer

# 方法一：APIView或者django View
# 需要自己写http方法函数及里面的逻辑。


class Edu_info_view(APIView):
    '''
    '''

    def get(self, request, format=None):
        edu_info_list = Edu_info.objects.all()
        edu_info_serializer = Edu_info_serializer(edu_info_list, many=True)
        # print(edu_info_serializer.data,request.user)
        return Response(edu_info_serializer.data)

# 方法二：GenericAPIView + ListModelMixin
# 所以可以在http方法函数中return self.list()，不用自己再写逻辑。
# ModelMixin里有写好的对应逻辑方法，如list()，create()等，
# GenericAPIView中有queryset，serializer_class,get_queryset()等


class Job_info_view(ListModelMixin, GenericAPIView):
    '''
    '''
    queryset = Job_info.objects.all()
    serializer_class = Job_info_serializer

    def get(self, request, *agrs, **kwargs):
        return self.list(request, *agrs, **kwargs)

# 方法三：*APIView
# *APIView继承了GenericAPIVIVE和对应的ModelMixin，且里面已写有对应的如上所示的http方法函数，所以可以再省略。


class Job_want_view(ListAPIView, CreateAPIView, DestroyAPIView):
    # queryset = Job_want.objects.all()
    serializer_class = Job_want_serializer

    def get_queryset(self):
        job_want_list = Job_want.objects.all()
        return job_want_list

    # pagination_class = Stander_pagination   # 自定义分页，也可以再settings里全局配置
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('job_name','salary')]
    # filter_fields = '__all__'
    # filterset_fields = ('job_name','salary')
    # filterset_fields = '__all__'  # filter 与 filterset 好像一样的，filterset可能是最新版本的。
    # filter_backends = (OrderingFilter,)
    filterset_class = Stander_filter    # 自定义过滤器
    search_fields = ['job_name', 'salary']
    # ordering_fields = ('salary',)


# 方法四：viewset。可以有若干结合，如viewsetMixin + *APIView，GenericViewSet + *ModelMixin等，万变不离其宗。
# 本质是viewsetMinx重写了as_view方法，使url处理更简单
# 处理url有两种方法：1. 使用as_view({'get':'list'})，发现一个小问题，若继承了CreateModelMixin，在as_view()里只写{"get":"list"}也会默认使用post方法，其他的同理；
# 2.使用更简单的router注册。


class Project_info_view(viewsets.ViewSetMixin, ListAPIView, CreateAPIView, RetrieveAPIView):
    queryset = Project_info.objects.all()
    serializer_class = Project_info_serializer

# class Project_info_view(viewsets.GenericViewSet,ListModelMixin):
#     queryset = Project_info.objects.all()
#     serializer_class = Project_info_serializer

    # def get(self, request, *args, **kwargs):      # 不用再写，需要在url中配置或使用router自动识别
    #     return self.list(request, *args, **kwargs)


class Certificate_view(viewsets.GenericViewSet, ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = Certificate_serializer


class Stack_view(viewsets.GenericViewSet, ListModelMixin):
    queryset = Stack.objects.all()
    serializer_class = Stack_serializer


class Tech_view(viewsets.GenericViewSet, ListModelMixin):
    queryset = Tech.objects.all()
    serializer_class = Tech_serializer


class Message_view(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = Message_serializer

    def get(self, request, *agrs, **kwargs):
        return self.list(request, *agrs, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = Message_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            title = data['title']
            content = data['content']
            contect = data['contect']
            send_mail(
                '在线反馈',
                'title:' + title + '\n' + 'content:' + content + '\n' + 'contect:' + contect,
                'admin@innocosme.com',
                ['myxing163@163.com']
            )
            return Response(1)
        return Response(0)

# 方法五：方法四的最强升级版，更全面的ModelViewset。也就是官方在开始给的例子，如同方法0。


class Action_num_view(viewsets.ModelViewSet):
    queryset = Action_num.objects.all()
    serializer_class = Action_num_serializer


class Visite_num_view(viewsets.ModelViewSet):
    queryset = Visite_num.objects.all()
    serializer_class = Visite_num_serializer

class Self_intro_view(viewsets.ReadOnlyModelViewSet):
    queryset = Self_intro.objects.all()
    serializer_class = Self_intro_serializer
