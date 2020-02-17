#!/usr/bin/env python
# -*- coding: utf-8 -*-
# yishenggudou@gmail.com
# @timger http://weibo.com/zhanghaibo
import yaml, codecs, os, jinja2

DIR = os.path.abspath(os.path.dirname(__file__))


def get_config(app_name):
    fpath = os.path.join(DIR, 'apps.yaml')
    with codecs.open(fpath, 'rb+', 'utf8') as fr:
        _ = yaml.load(fr)
    o = _[app_name]
    o['app_name'] = app_name
    return o


def render(app_name, tmpl_path):
    jinja_env = jinja2.Environment(
        # block_start_string='((*',
        # block_end_string='*))',
        variable_start_string='%%',
        variable_end_string='%%',
        # comment_start_string='((=',
        # comment_end_string='=))',
        loader=jinja2.FileSystemLoader(os.path.abspath(DIR))
    )
    context = get_config(app_name)
    template = jinja_env.get_template(tmpl_path)
    _ = template.render(**context)
    real_path = os.path.join(DIR, tmpl_path.replace(".jinja2", ""))
    with codecs.open(real_path, 'wb+', 'utf8') as  fw:
        fw.write(_)


def fix_setup(app_name):
    render(app_name,'setup.py.jinja2')


def fix_setting(app_name):
    render(app_name, 'settings.py.jinja2')


def fix_app(app_name):
    render(app_name, 'app.py.jinja2')


def main():
    import sys
    app_name = sys.argv[1]
    print(app_name)
    fix_setup(app_name)
    fix_setting(app_name)
    fix_app(app_name)


if __name__ == '__main__':
    main()
