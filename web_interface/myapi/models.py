from django.db import models


class SystemInf(models.Model):

    # Device name:
    name_of_device = models.CharField(max_length=25, default=' ')

    # Status:
    output_address = models.CharField(max_length=25, default=' ')
    device_time = models.CharField(max_length=25)
    running_time = models.CharField(max_length=15)
    cpu_usage = models.IntegerField()
    cpu_temperature = models.IntegerField()
    memory_usage = models.CharField(max_length=20)

    # DHCP Status:
    ip = models.CharField(max_length=15)
    netmask = models.CharField(max_length=15)
    default_gateway = models.CharField(max_length=15)