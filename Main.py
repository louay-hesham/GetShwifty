from TvShow import TvShow

RM = TvShow('Rick and Morty', 'http://eztv.ag/search/rick-and-morty', 3, 3)
x = RM.get_next_episode_links()
for i in x:
    print(i)

