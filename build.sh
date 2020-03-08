#!/usr/bin/env bash
rm -vrf ./.eggs/* build/* dist/*
python pre_build.py $1
python setup.py clean py2app
mv  dist/app.app dist/$1.app
cmd="dmgbuild -s settings.py $1 dist/$1-install.dmg"
echo ${cmd}
$cmd
open dist/
echo "./dist/${1}.app/Contents/MacOS/app"