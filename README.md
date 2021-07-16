# cruNch3r.py
Mass scan for check live host
---

## Help
```
┌──(root💀h4rithd)-[/opt/cruNch3r] 🐍 v 0.1
└─# python3 cruNch3r.py -h                                                                                                                                                                                130 ⨯
usage: python3 cruNch3r.py -uL [URLList]

---------------------------------------------------------
--------- | Mass scan for check live host | -------------
---------------------------------------------------------
                     __     _     _____
  ___ _ __ _   _  /\ \ \___| |__ |___ / _ __
 / __| '__| | | |/  \/ / __| '_ \  |_ \| '__|
| (__| |  | |_| / /\  / (__| | | |___) | |
 \___|_|   \__,_\_\ \/ \___|_| |_|____/|_|
                                        V 0.1
          ---------------------|by h4rith.com
---------------------------------------------------------

[!] Required arguments:
  -u , --urllist    Target URLs file
  -to , --timeout   Set timeout (Default is 3)

---------------- Script from h4rithd.com ----------------
```
---

## Install
```
git clone https://github.com/h4rithd/cruNch3r.git
pip install signal,argparse,textwrap,threading,beautifulsoup4,prettytable,alive-progress
cd cruNch3r
python3 cruNch3r.py -h 
```
---

## Test run
```
┌──(root💀h4rithd)-[/opt/cruNch3r] 🐍 v 0.1
└─# python3 cruNch3r.py -u urls
on 0:  ------- Done | https://admin.friendzoneportal.red
on 1:  ------- Done | https://administrator1.friendzone.red
on 2:  ------- Done | https://files.friendzoneportal.red
on 3:  ------- Done | https://friendzoneportal.red
on 4:  ------- Done | https://friendzone.red
on 5:  ------- Done | https://hr.friendzone.red
on 6:  ------- Done | https://imports.friendzoneportal.red
on 7:  ------- Done | https://uploads.friendzone.red
on 8:  ------- Done | https://vpn.friendzoneportal.red
|▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉| 9/9 [100%] in 7.6s (1.18/s)


-----------| cruNch3r v0.1 :: by h4rithd.com |-----------
+---------------------------------------+--------+-------------------------------------------+
| URL                                   | Status | Title                                     |
+---------------------------------------+--------+-------------------------------------------+
| https://admin.friendzoneportal.red    |  200   | Admin Page                                |
| https://administrator1.friendzone.red |  200   | FriendZone Corp Administrator login page  |
| https://friendzone.red                |  200   | FriendZone escape software                |
| https://friendzoneportal.red          |  200   | Watching you !                            |
| https://uploads.friendzone.red        |  200   | FriendZone Escape software upload manager |
| https://files.friendzoneportal.red    |  404   | 404 Not Found                             |
| https://hr.friendzone.red             |  404   | 404 Not Found                             |
| https://imports.friendzoneportal.red  |  404   | 404 Not Found                             |
| https://vpn.friendzoneportal.red      |  404   | 404 Not Found                             |
+---------------------------------------+--------+-------------------------------------------+
```
