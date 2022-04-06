# from django.shortcuts import render

from rest_framework import viewsets

from .serializers import SystemInfSerializer
from .models import SystemInf


class SystemInfViewSet(viewsets.ModelViewSet):
    queryset = SystemInf.objects.all().order_by('ip')
    serializer_class = SystemInfSerializer
