# -*- coding:UTF-8 -*-


'''
Created on 2013-8-7

@author: caifenghua
'''

import codecs
import json
import datetime
import time
import math
import random
import creditutils.str_util as str_utils


def filter_unique_item(items):
    dst_items = []
    for item in items:
        item_same = None
        for item_in in dst_items:
            if item == item_in:
                item_same = item
                break

        if item_same != None:
            print(item_same)
        else:
            dst_items.append(item)

    return dst_items


def decode_to_unicode(string):
    import chardet
    result = chardet.detect(string)
    return codecs.decode(string, result['encoding'])


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def measure_time(func, *args, **dicts):
    begin = time.time()

    func(*args, **dicts)

    end = time.time()
    time_info = str_utils.get_time_info(begin, end)

    # 输出总用时
    print('===Finished. Total time: {}==='.format(time_info))


class _Bridge:
    pass

# 增加一个中间转换类，然后将该中间转换类的实例作参数进行传递，便于直接调用已实现的参数命令。
def get_dict_obj(data_map):
    obj = _Bridge()
    for name, value in data_map.items():
        setattr(obj, name, value)

    return obj


def get_random_index(items):
    length = len(items)
    index = int(random.uniform(0, length))
    if index >= length:
        index = length - 1

    return index


def get_random_item(items):
    return items[get_random_index(items)]


def get_str_time():
    t = time.time()
    t_array = time.localtime(t)
    t_str = time.strftime('%Y-%m-%d %H:%M:%S', t_array)
    t_ms = math.floor(math.modf(t)[0]*1000)
    t_str_with_ms = f'{t_str}:{t_ms:03d}'
    return t_str_with_ms


# 打印信息后面增加时间信息
def print_t(info):
    print(f'{info} {get_str_time()}')


if __name__ == '__main__':
    #     string = '我们的祖国像花园'
    #     result = chardet.detect(string)
    #     print(result)
    #
    #     decode_to_unicode(string)

    print('to the end')
