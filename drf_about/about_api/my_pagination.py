from rest_framework.pagination import PageNumberPagination


class Stander_pagination(PageNumberPagination):
    page_size = 2  # 每页的数量
    page_query_param = 'p'  # 第几页，?p=2

    page_size_query_param = 'page_size'  # 自定义每页的数量，?p=2&page_size=5
    max_page_size = 10
