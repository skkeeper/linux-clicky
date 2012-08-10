#!/usr/bin/python
# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 2 -*-
# Author: Fábio André Damas <skkeeper at gmail dot com>

from re import compile as regex_compile


def detect_keyboards():
  file_handle = open('/proc/bus/input/devices', 'r')
  keyboards = []
  regex = regex_compile("event\d{0,3}")
  for line in file_handle.readlines():
    if 'Handlers' in line:
      if 'kbd' in line:
        keyboards.append('/dev/input/' + regex.findall(line)[0])
      continue
  file_handle.close()
  return keyboards


if __name__ == '__main__':
  print detect_keyboards()
