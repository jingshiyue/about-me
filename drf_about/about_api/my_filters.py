from django_filters import rest_framework as filters
from . models import Job_want
class Stander_filter(filters.FilterSet):
    salary_gte = filters.NumberFilter(label='薪水大于等于',field_name = 'salary',lookup_expr='gte')
    class Meta:
        model = Job_want
        fields =['salary_gte',]