#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Zhang Xin
@Contact: xinzhang_hp@163.com
"""

from torch import nn


def conv3x3(in_planes, out_planes, stride=1):
    return nn.Conv2d(in_planes, out_planes, kernel_size=3, stride=stride, padding=1, bias=False)
