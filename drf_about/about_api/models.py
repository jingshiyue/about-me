from datetime import date

from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.


class Base_info(models.Model):
    name = models.CharField('姓名', max_length=3)
    age = models.CharField('年龄',max_length = 10)
    sex = models.CharField('性别', max_length=10, default='男')
    birth = models.DateField('生日', default=date.today())
    img = models.ImageField('照片', upload_to='img/', blank=True)
    mobile_phone = models.CharField('手机号码', max_length=11)
    email = models.EmailField('邮箱')
    mysite = models.CharField('个人主页', max_length=100)
    address = models.CharField('地址', max_length=20)
    self_desc = models.TextField('自我介绍')
    pub_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'A基本信息'


class Base_info_admin(admin.ModelAdmin):
    list_display = ['name', 'age', 'sex', 'mobile_phone', 'email', 'address']


admin.site.register(Base_info, Base_info_admin)


class Edu_info(models.Model):
    university = models.CharField(max_length=10)
    major = models.CharField(max_length=10)
    degree  = models.CharField(max_length = 10,blank = True)
    date_begin = models.DateField(default=date.today())
    date_end = models.DateField(default=date.today())
    rank = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.university

    class Meta:
        verbose_name_plural = 'B教育信息'
        ordering = ['rank']


class Edu_info_admin(admin.ModelAdmin):
    list_display = ['university', 'major','degree','date_begin','date_end','rank']


admin.site.register(Edu_info, Edu_info_admin)


class Job_info(models.Model):
    company = models.CharField(max_length=20)
    position_name = models.CharField(max_length=10, default='')
    position_desc = models.TextField()
    why_leave = models.TextField(default = '')
    date_begin = models.DateField(default=date.today())
    date_end = models.DateField(default=date.today())
    rank = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = 'C工作信息'
        ordering = ['rank']


class Job_info_admin(admin.ModelAdmin):
    list_display = ['company', 'position_desc','why_leave','date_begin','date_end','rank']


admin.site.register(Job_info, Job_info_admin)


class Job_want(models.Model):
    job_name = models.CharField(max_length=100)
    salary = models.SmallIntegerField()
    now_status = models.CharField(max_length=10)

    def __str__(self):
        return self.job_name

    class Meta:
        verbose_name_plural = 'D求职意向'


class Job_want_admin(admin.ModelAdmin):
    list_display = ['job_name', 'salary', 'now_status']


admin.site.register(Job_want, Job_want_admin)


class Project_info(models.Model):
    pro_name = models.CharField(max_length=20)
    pro_url = models.URLField()
    desc = models.TextField()
    technology_stack = models.CharField(max_length=50)
    pro_time = models.DateField(default=date.today())
    rank = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.pro_name

    class Meta:
        verbose_name_plural = 'E项目信息'
        ordering = ['rank']


class Project_info_admin(admin.ModelAdmin):
    list_display = ['pro_name', 'pro_url',
                    'technology_stack', 'pro_time', 'rank']


admin.site.register(Project_info, Project_info_admin)


class Stack(models.Model):
    name = models.CharField(max_length=10)
    rank = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'F-stack'
        ordering = ['rank']


class Stack_admin(admin.ModelAdmin):
    list_display = ['name', 'rank']


admin.site.register(Stack, Stack_admin)


class Tech(models.Model):
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE, default='',related_name='techs')
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    DEGREE_CHOICES = (('C','了解'),('B', '掌握'), ('A', '熟练'))
    degress = models.CharField(
        max_length=10, choices=DEGREE_CHOICES, default='掌握')
    degress_precentage = models.SmallIntegerField()
    rank = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'g-tech'
        ordering = ['rank']


class Tech_admin(admin.ModelAdmin):
    list_display = ['name', 'desc', 'degress',
                    'stack', 'degress_precentage', 'rank']


admin.site.register(Tech, Tech_admin)


class Certificate(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
    desc = models.CharField(max_length=20)
    rank = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'H证书'
        ordering = ['rank']


class Certificate_admin(admin.ModelAdmin):
    list_display = ['name', 'date', 'desc', 'rank']


admin.site.register(Certificate, Certificate_admin)


class Message(models.Model):
    title = models.CharField(max_length=30,blank = True)
    content = models.TextField()
    contect = models.CharField(max_length=30,blank = True)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = 'I-信息'
        ordering = ['add_time']


class Message_admin(admin.ModelAdmin):
    list_display = ["title",'content', 'contect', 'add_time']


admin.site.register(Message, Message_admin)

class Action_num(models.Model):
    like_me_num = models.PositiveSmallIntegerField(blank = True,null = True)
    not_like_num = models.PositiveSmallIntegerField(blank = True,null = True)
    like_or_not_num = models.PositiveSmallIntegerField(blank = True,null = True)

    def __str__(self):
        return str(self.like_me_num)
    class Meta:
        verbose_name_plural = 'J-num'


class Action_num_amdin(admin.ModelAdmin):
    list_display = ('like_me_num','not_like_num','like_or_not_num')

admin.site.register(Action_num,Action_num_amdin)


class Visite_num(models.Model):
    visite_num = models.SmallIntegerField(default = 0)
    def __str__(self):
        return str(self.visite_num)
    class Meta:
        verbose_name_plural = 'K-visite_num'

class Visite_num_admin(admin.ModelAdmin):
    list_display = ('visite_num',)

admin.site.register(Visite_num,Visite_num_admin)

class Self_intro(models.Model):
    title = models.CharField(max_length = 10,default = '自我评价')
    self_intro = models.TextField()
    
    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name_plural = ('L-自我评价')

class Self_intro_admin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Self_intro,Self_intro_admin)

    