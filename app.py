#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
# @timger http://weibo.com/zhanghaibo

import webview
import os

DIR = os.path.abspath(os.path.dirname(__file__))
"""
This example demonstrates how to create a webview window.
"""
icon_path = os.path.join(DIR, 'icons/b.icns')
if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window('B站', 'https://www.bilibili.com/',
     width=1024,
     height=800,
    )
    webview.start(debug=True,)