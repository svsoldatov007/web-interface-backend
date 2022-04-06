import time
import schedule
from system_inf import *
import requests


def get_attribute(object, name):    # возвращает значение поля <name> для <object> в бд с помощью среза строки
    begin = object.find('"' + name + '":') + 3 + len(name)
    if object[begin] == '"':
        begin += 1     # строка пишется в кавычках, число - без
    end = begin+1
    while object[end] != '"' and object[end] != ',':
        end += 1
    return object[begin:end]


def update_inf():
    # удаляем всё предыдущее
    response = str(requests.get('http://127.0.0.1:8000/SystemInfs/').content).split('},')
    print(response)
    if response != ["b'[]'"]:   # if there are some objects in the database
        for old_inf in response:
            requests.delete('http://127.0.0.1:8000/SystemInfs/'+str(get_attribute(old_inf, "id")))

    # постим актуальную инфу
    requests.post('http://127.0.0.1:8000/SystemInfs/', data={
        "name_of_device": get_name_of_device(),
        "output_address": get_output_address(),
        "device_time": get_device_time(),
        "running_time": get_running_time(),
        "cpu_usage": get_cpu_usage(),
        "cpu_temperature": get_cpu_temperature(),
        "memory_usage": get_memory_usage(),
        "ip": get_ip(),
        "netmask": get_netmask(),
        "default_gateway": get_default_gateway()
    })


if __name__ == "__main__":
    schedule.every(60).seconds.do(update_inf)
    while True:
        schedule.run_pending()
        time.sleep(1)
