from rest_framework import serializers

from .models import SystemInf


class SystemInfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SystemInf
        fields = ['id',  'name_of_device', 'output_address', 'device_time', 'running_time', 'cpu_usage', 'cpu_temperature', 'memory_usage',
                  'ip', 'netmask', 'default_gateway']
