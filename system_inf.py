import os
# import psutil
import datetime
import schedule
import json
import socket

# Status:


def get_name_of_device():
    return socket.gethostname()


def get_output_address():
    '''path = "C:\\Users\\Oleg\\rtsp-simple-server\\rtsp-simple-server.yml"    # CHANGE! There will be another path
    yml_file = open(path)
    yml_file_text = yml_file.read().split('\n')

    line = ''     # line "source: rtsp://original-url"
    for i in range(len(yml_file_text)-1):
        if 'proxied' in yml_file_text[i]:
            if 'source:' in yml_file_text[i+1]:     # if the next line is a comment
                line = yml_file_text[i+1]
                break
            elif 'source:' in yml_file_text[i+2]:   # if the next line is the address itself
                line = yml_file_text[i+2]
                break
    if line == '':     # didn't find an output address
        return ''
    else:
        begin = line.find(':')
        return line[begin+2:]  # there is always a space before the address'''

    return "rtsp://original-url"


def get_device_time():
    '''command = ' date "+%H:%M:%S   %d/%m/%y"'
    result = str(os.popen(command).read()).strip()
    return result'''
    return "10:17:16 23/03/22"


def get_running_time():
    '''command = "awk '{print $1}' /proc/uptime"
    result = int(float(str(os.popen(command).read()).strip()))    # in seconds
    day = result//(3600*24)
    hour = (result-day*3600*24)//3600
    minute = (result-day*3600*24-hour*3600)//60
    sec = result-day*3600*24-hour*3600-minute*60
    if day < 10:
        day = '0'+str(day)
    return str(day)+':'+str(time(hour, minute, sec))'''
    return '00:01:07:48'


def get_cpu_usage():

    # return int(round(psutil.cpu_percent()))
    return 20


def get_cpu_temperature():

    '''command = "cat /sys/class/thermal/thermal_zone0/temp"
    return int(os.popen(command).read())//1000'''

    return 29


def get_memory_usage():
    '''command = 'vmstat -s'
    result = str(os.popen(command).read()).strip().split()
    total = round(float(result[0])/1024, 1)
    used = round(float(result[4])/1024, 1)
    return str(used) + 'M/' + str(total) + 'M'''

    return '1460.3M/3956.1M'


# DHCP status:

def get_ip():
    '''result = str(os.popen("ip a").read()).split()
    ip_mask = ''
    for i in range(len(result)):
        if result[i] == 'inet' and '127.0.0.1' not in result[i+1] and '172.17.0.1' not in result[i+1]:
            ip_mask = result[i+1]
            break
    ip = ip_mask[:ip_mask.find('/')]
    return ip'''

    return '172.18.146.30'


def get_netmask():
    '''result = str(os.popen("ip a").read()).split()
    ip_mask = ''
    for i in range(len(result)):
        if result[i] == 'inet' and '127.0.0.1' not in result[i + 1] and '172.17.0.1' not in result[i + 1]:
            ip_mask = result[i + 1]
            break
    num1 = int(ip_mask[ip_mask.find('/') + 1:])  # the number of '1'
    mask_1_0 = ''   # mask like '111..100..0'
    for i in range(num1):
        mask_1_0 += '1'
    for i in range(32 - num1):
        mask_1_0 += '0'
    netmask = ''    # netmask like 255.255.255.0
    for i in range(4):
        netmask = netmask + str(int(mask_1_0[8 * i:8 * i + 8], base=2)) + '.'

    return netmask[:len(netmask)-1]     # without the last '.'''

    return  '255.255.255.0'


def get_default_gateway():
    '''command = "echo $(/sbin/ip route | awk '/default/ { print $3 }')"
    result = str(os.popen(command).read()).strip()
    return result'''

    return '172.18.146.1'


# ssh jetson@172.18.146.30

'''print('device time:', get_device_time())
print('running time:', get_running_time())
print('cpu usage in percents:', get_cpu_usage())
print('cpu temperature =', get_cpu_temperature())
print('memory usage:', get_memory_usage())
print('ip:', get_ip())
print('netmask:', get_netmask())
print('default gateway:', get_default_gateway())'''
