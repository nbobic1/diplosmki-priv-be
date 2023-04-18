from rest_framework.pagination import LimitOffsetPagination


class HundredSetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 100