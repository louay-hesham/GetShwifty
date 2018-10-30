#I used http://patorjk.com/software/taag/ for the wuba luba dub dub

import time
import requests
import os
from bs4 import BeautifulSoup


class TvShow(object):
    def __init__(self, name, link, season, episode):
        self.name = name
        self.link = link
        self.season = season
        self.episode = episode

    def __get_episode_name(self):
        return 'S' + ('0' if self.season < 10 else '') + str(self.season) + 'E' + ('0' if self.episode < 10 else '') + str(self.episode)

    def get_next_episode_links(self):
        
        request = requests.get(self.link)
        if request.status_code != 200:
            raise BaseException('Connection Error, Retrying')

        while request.status_code != 200:
            time.sleep(5)
            request = requests.get(self.link)
            if request.status_code != 200:
                raise BaseException('Connection Error, Retrying')
            
        html = request.content
        soup = BeautifulSoup(html, 'html.parser')
        links = [i['href'] for i in soup.find_all('a') if self.__get_episode_name() in i['href']]
        if links == []:
            print('Not Here yet')
            return
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

            self.links = links
            return links

    def open_episode(self, i):
        os.startfile(self.links[(i - 1) * 2])
