rm -vrf ./.eggs/* build/* dist/*
python pre_build.py $1
python setup.py clean py2app
#ln -s dist/$1.app dist/app.app
cmd="dmgbuild -s settings.py app dist/$1-install.dmg"
echo ${cmd}
$cmd
open dist/
