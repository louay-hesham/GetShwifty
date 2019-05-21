#I used http://patorjk.com/software/taag/ for the wuba luba dub dub

import time
import requests
import os
from bs4 import BeautifulSoup


class TvShow(object):
    def __init__(self, name, show_properties, bittorrent_client):
        self.name = name
        self.link = show_properties['link']
        self.season = show_properties['beginning_season']
        self.episode = show_properties['beginning_episode']
        self.extra = show_properties['extra']
        self.bittorrent_client = bittorrent_client

    def __get_episode_name(self):
        return 'E' + ('0' if self.episode < 10 else '') + str(self.episode)

    def __get_season_name(self):
        return 'S' + ('0' if self.season < 10 else '') + str(self.season)

    def __has_episode(self, links):
        for link in links:
            if self.__get_episode_name() in link:
                return True
        return False

    def __has_season(self, links):
        for link in links:
            if self.__get_season_name() in link:
                return True
        return False

    def get_next_episodes_links(self, extra='', download=False):

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
        links = [i['href'] for i in soup.find_all('a')]

        filtered_links = []
        while self.__has_season(links):
            while self.__has_episode(links):
                intermediate_filtered_list = [link for link in links if 'magnet' in link and self.extra in link and self.__get_season_name() in link and self.__get_episode_name() in link]
                if len(intermediate_filtered_list) > 0:
                    filtered_links.append(intermediate_filtered_list[0])
                self.episode += 1
            self.episode = 1
            self.season += 1


        if filtered_links == []:
            print(self.name + ': Not Here yet')
            return []
        else:
            print('''
     __       __            __                        __                  __                        _______             __              _______             __
    /  |  _  /  |          /  |                      /  |                /  |                      /       \\           /  |            /       \\           /  |
    $$ | / \\ $$ | __    __ $$ |____    ______        $$ |       __    __ $$ |____    ______        $$$$$$$  | __    __ $$ |____        $$$$$$$  | __    __ $$ |____
    $$ |/$  \\$$ |/  |  /  |$$      \\  /      \\       $$ |      /  |  /  |$$      \\  /      \\       $$ |  $$ |/  |  /  |$$      \\       $$ |  $$ |/  |  /  |$$      \
    $$ /$$$  $$ |$$ |  $$ |$$$$$$$  | $$$$$$  |      $$ |      $$ |  $$ |$$$$$$$  | $$$$$$  |      $$ |  $$ |$$ |  $$ |$$$$$$$  |      $$ |  $$ |$$ |  $$ |$$$$$$$  |
    $$ $$/$$ $$ |$$ |  $$ |$$ |  $$ | /    $$ |      $$ |      $$ |  $$ |$$ |  $$ | /    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |
    $$$$/  $$$$ |$$ \\__$$ |$$ |__$$ |/$$$$$$$ |      $$ |_____ $$ \\__$$ |$$ |__$$ |/$$$$$$$ |      $$ |__$$ |$$ \\__$$ |$$ |__$$ |      $$ |__$$ |$$ \\__$$ |$$ |__$$ |
    $$$/    $$$ |$$    $$/ $$    $$/ $$    $$ |      $$       |$$    $$/ $$    $$/ $$    $$ |      $$    $$/ $$    $$/ $$    $$/       $$    $$/ $$    $$/ $$    $$/
    $$/      $$/  $$$$$$/  $$$$$$$/   $$$$$$$/       $$$$$$$$/  $$$$$$/  $$$$$$$/   $$$$$$$/       $$$$$$$/   $$$$$$/  $$$$$$$/        $$$$$$$/   $$$$$$/  $$$$$$$/


    ''')
            self.filtered_links = filtered_links
            if download:
                self.download_all()
            return filtered_links

    def download_all(self):
        for link in self.filtered_links:
            os.system(self.bittorrent_client + " " + link)
