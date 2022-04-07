#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author : Zhang Xin
@Contact: xinzhang_hp@163.com
"""
from .example_model import ResNet18


def build_model(cfg):
    model = ResNet18(cfg.MODEL.NUM_CLASSES)
    return model
