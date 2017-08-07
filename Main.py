#!/usr/bin/python
#A script to get you torrents of rick and morty S03E02 as soon as the torrent is here
#I used http://patorjk.com/software/taag/ for the wuba luba dub dub
#It should give direct links to the torrents
import time
import requests
import os
from bs4 import BeautifulSoup

while True:
    request = requests.get('http://eztv.ag/search/rick-and-morty')
    if request.status_code != 200:
        raise BaseException('connection Error, Retrying')
        continue
    html = request.content
    soup = BeautifulSoup(html, 'html.parser')
    links = [i['href'] for i in soup.find_all('a') if 'S03E03' in i['href']]
    if links == []:
        print('Not Here yet')
    else:
        print('''
 __       __            __                        __                  __                        _______             __              _______             __
/  |  _  /  |          /  |                      /  |                /  |                      /       \           /  |            /       \           /  |
$$ | / \ $$ | __    __ $$ |____    ______        $$ |       __    __ $$ |____    ______        $$$$$$$  | __    __ $$ |____        $$$$$$$  | __    __ $$ |____
$$ |/$  \$$ |/  |  /  |$$      \  /      \       $$ |      /  |  /  |$$      \  /      \       $$ |  $$ |/  |  /  |$$      \       $$ |  $$ |/  |  /  |$$      \
$$ /$$$  $$ |$$ |  $$ |$$$$$$$  | $$$$$$  |      $$ |      $$ |  $$ |$$$$$$$  | $$$$$$  |      $$ |  $$ |$$ |  $$ |$$$$$$$  |      $$ |  $$ |$$ |  $$ |$$$$$$$  |
$$ $$/$$ $$ |$$ |  $$ |$$ |  $$ | /    $$ |      $$ |      $$ |  $$ |$$ |  $$ | /    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |
$$$$/  $$$$ |$$ \__$$ |$$ |__$$ |/$$$$$$$ |      $$ |_____ $$ \__$$ |$$ |__$$ |/$$$$$$$ |      $$ |__$$ |$$ \__$$ |$$ |__$$ |      $$ |__$$ |$$ \__$$ |$$ |__$$ |
$$$/    $$$ |$$    $$/ $$    $$/ $$    $$ |      $$       |$$    $$/ $$    $$/ $$    $$ |      $$    $$/ $$    $$/ $$    $$/       $$    $$/ $$    $$/ $$    $$/
$$/      $$/  $$$$$$/  $$$$$$$/   $$$$$$$/       $$$$$$$$/  $$$$$$/  $$$$$$$/   $$$$$$$/       $$$$$$$/   $$$$$$/  $$$$$$$/        $$$$$$$/   $$$$$$/  $$$$$$$/
                                                                                                                                                          
                                                                              
''')
  
        for i in links:
            if 'http' in i:
               print(i)
            else:
                os.startfile(i)
        break
    time.sleep(5)

