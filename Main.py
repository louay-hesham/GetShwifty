from TvShow import TvShow

# Specify your bittorrent client
bittorrent_client='deluge'

# Specify your shows details
# Beginning_season and beginning_episode define the exact episode that the search starts from.
# It should download all the episodes in all seasons after that episodes.
# If you enter 1,1 respectively, it will download the entire series.

# The code opens magnet links into your favourite bittorrent client.
# This has been tested using Deluge. Other bittorrent clients may require some modifications in the code.
# Only works on Unix for now. Windows uses a different set of commands to start an application.
# Support for Windows may or may not come in the future (I hate coding on Windows).
# I recommend use eztv.io for all your torrent links, you may try other websites if they have the same general layout.

shows = {
    "The Flash": {
        "link": "https://eztv.io/shows/1058/the-flash-2014/",
        "beginning_season": 6,
        "beginning_episode": 1,
        "extra": "x265"
    },
    "Rick and Morty": {
        "link": "https://eztv.io/shows/1017/rick-and-morty/",
        "beginning_season": 4,
        "beginning_episode": 1,
        "extra": ""
    },
    "The Big Bang Theory": {
        "link": "https://eztv.io/shows/23/the-big-bang-theory/",
        "beginning_season": 13,
        "beginning_episode": 1,
        "extra": "x265"
    },
    "Better Call Saul": {
        "link": "https://eztv.io/shows/1191/better-call-saul/",
        "beginning_season": 5,
        "beginning_episode": 1,
        "extra": "720p"
    },
    "Mr Robot": {
        "link": "https://eztv.io/shows/1250/mr-robot/",
        "beginning_season": 4,
        "beginning_episode": 1,
        "extra": "720p"
    }
}

for show_title, show_properties in shows.items():
    show = TvShow(show_title, show_properties, bittorrent_client)
    x = show.get_next_episodes_links(download=True)
    for i in x:
        print(i)
