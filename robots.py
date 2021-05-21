"""
        API count exceeded - Increase Quota with Membership
        If you encounter an error (API count exceeded - Increase Quota with Membership)   you need a VPN

        creat by Amir Hossein Tadas & TAHA

        instagram = Taha_t_80
"""
import requests
import sys
import time
from colorama import Fore
import os
search = ['robots.txt',
          'search/',
          'admin/',
          'login/',
          'sitemap.xml',
          'sitemap2.xml',
          'config.php',
          'wp-login.php',
          'log.txt',
          'update.php',
          'INSTALL.pgsql.txt',
          'user/login/',
          'INSTALL.txt',
          'profiles/',
          'scripts/',
          'LICENSE.txt',
          'CHANGELOG.txt',
          'themes/',
          'inculdes/',
          'misc/',
          'user/logout/',
          'user/register/',
          'cron.php',
          'filter/tips/',
          'comment/reply/',
          'xmlrpc.php',
          'modules/',
          'install.php',
          'MAINTAINERS.txt',
          'user/password/',
          'node/add/',
          'INSTALL.sqlite.txt',
          'UPGRADE.txt',
          'INSTALL.mysql.txt']


def __start__():
    try:
        print(Fore.RED+" [!] Plase Enter WebSite Address ")
        print(Fore.RED+"\n [!] for exampel : test.com\n")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"tahat80"+Fore.BLUE+"/"+Fore.WHITE+"Robots_Scanner"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+">> ")
        if 'http' in url:
            pass
        elif 'http' != url:
            url = ('http://'+url)

        for i in search:
            time.sleep(0.1)

            ur = (url+"/"+i)
            reqs = requests.get(ur)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(Fore.GREEN+" [+] " + ur)
            else:
                print(Fore.RED+" [-] "+ur)
        try:
            input(Fore.RED+" [!] "+Fore.GREEN +
                  "Back To Again (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("")


if __name__ == '__main__':
    while True:
        try:
            os.system('cls')
        except:
            os.system('clear')

        __start__()
