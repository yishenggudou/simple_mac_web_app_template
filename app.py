#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
# @timger http://weibo.com/zhanghaibo

import webview
import os
fix_js = r"""
setTimeout(
    function(){
         function fix(){
            var script = document.createElement('script');
            script.setAttribute('type', 'text/javascript');
            script.setAttribute('src', '//apps-1251771654.cos.ap-chengdu.myqcloud.com/weread/app.js');
            script.onload = function() {
              console.log("Script loaded and ready");
            };
            document.body.appendChild(script)
        }
        window.onload =fix;
        fix();
        console.log("exec finished!")
    }
,2000);
console.log("load finished!")
"""

def evaluate_js(window):
    result = window.evaluate_js(fix_js )
    print(result)

def on_loaded():
    print('DOM is ready')
    window = webview.windows[0]
    print("in onload event....",window,window.loaded)
    window.loaded -= on_loaded
    print("....",window.loaded)
    rst = window.evaluate_js(fix_js)
    print("rst",rst)
    print("finished to evaluate_js!..")

DIR = os.path.abspath(os.path.dirname(__file__))
"""
This example demonstrates how to create a webview window.
"""
icon_path = os.path.join(DIR, 'icons/yinxiang.icns')
if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window('印象笔记', 'https://app.yinxiang.com/Home.action',
     width=600,
     height=800,
    )
    window.loaded += on_loaded
    #webview.start(evaluate_js,window,debug=True,)
    webview.start(debug=True,)