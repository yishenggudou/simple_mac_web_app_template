rm -vrf ./.eggs/* build/* dist/*
python setup.py clean py2app
dmgbuild -s settings.py 'weread_mac' dist/weread_mac_installer.dmg
open dist/
