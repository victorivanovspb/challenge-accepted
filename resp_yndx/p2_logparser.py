# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import heapq
import sys
import re


def invert_int_value(v):
    if type(v) is int:
        return -1 * v
    raise TypeError("inverted value is not integer")


def is_not_ip(ip):
    aa = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip)
    return False if aa else True


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file", dest="filename", help=u"input file", required=True)
    parser.add_argument("--ip-check", dest="ip_check", help=u"IPv4 check turn on", action='store_true')
    args = parser.parse_args()

    ip_check = args.ip_check if (args.ip_check != None) else False

    try:
        f = open(args.filename, "r")
    except IOError:
        sys.exit(1)

    # Каждый считываемый IP-адрес добавляется в словарь с инкрементом своего счётчика.
    ip_map = {}
    for line in f:
        ip = line.split(" ")[0]
        if ip_check and is_not_ip(ip):
            continue
        c = ip_map.get(ip)
        c = 1 if (c == None) else (c + 1)
        ip_map[ip] = c

    # Все значения словаря переносятся в кучу (где сортируются по убыванию).
    # А так как нужны наибольшие значения, то инвертируем их значения,
    # для того, чтобы их легко было получить с конца кучи.
    ip_heap = []
    for ip in ip_map:
        heapq.heappush(ip_heap, (invert_int_value(ip_map[ip]), ip))

    for i in range(10):
        try:
            el = heapq.heappop(ip_heap)
            print str(invert_int_value(el[0])) + " " + el[1]
        except IndexError:
            break
