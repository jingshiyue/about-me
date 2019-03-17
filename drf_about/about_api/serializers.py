from . models import Base_info, Edu_info, Job_info, Job_want, Project_info, Stack, Tech, Certificate, Message, Action_num, Visite_num, Self_intro
from rest_framework import serializers
from rest_framework import throttling   #？


class Test(serializers.Serializer):
    '''
    方式1：
    对比，form.Form
    '''
    pass


class Test2(serializers.ModelSerializer):
    '''
    方式二：
    对比，form.ModelForm
    '''


class Base_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Base_info
        fields = '__all__'


class Edu_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Edu_info
        fields = "__all__"


class Job_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Job_info
        fields = '__all__'


class Job_want_serializer(serializers.ModelSerializer):
    class Meta:
        model = Job_want
        fields = "__all__"


class Project_info_serializer(serializers.ModelSerializer):
    class Meta:
        model = Project_info
        fields = '__all__'


class Certificate_serializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class Tech_serializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = "__all__"


class Stack_serializer(serializers.ModelSerializer):
    techs = Tech_serializer(many=True)

    class Meta:
        model = Stack
        fields = "__all__"


class Message_serializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class Action_num_serializer(serializers.ModelSerializer):
    class Meta:
        model = Action_num
        fields = '__all__'


class Visite_num_serializer(serializers.ModelSerializer):
    class Meta:
        model = Visite_num
        fields = '__all__'


class Self_intro_serializer(serializers.ModelSerializer):
    class Meta:
        model = Self_intro
        fields = ('self_intro',)
