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
ua_js=r"""
Object.defineProperty(window.navigator, 'userAgent', {get: function () {return "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}});
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
    
    print("finished to evaluate_js!..")

DIR = os.path.abspath(os.path.dirname(__file__))
"""
This example demonstrates how to create a webview window.
"""
icon_path = os.path.join(DIR, 'icons/b.icns')




if __name__ == '__main__':
    # Create a standard webview window
    window = webview.create_window('B站@dafengstudio@gmail.com', 'https://m.bilibili.com/channel/13.html',
     width=786,
     height=1024,
    )
    window.loaded += on_loaded
    #webview.start(evaluate_js,window,debug=True,)
    webview.start(debug=True, )