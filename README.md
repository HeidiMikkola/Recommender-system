# Recommender-system

Course work for recommender systems course
Makes group recommendations from last.fm dataset, found [here](http://ocelma.net/MusicRecommendationDataset/lastfm-360K.html)

Examples:

```bash
# Manually list ids
python3 main.py -i 000294c1f0d9b40067487457ca31f0caab81d44a 0003906ab668111f2cd332962cb09f8e3b795c6c 0005937bb7e8b1992d94b493519e216317f71685 -f artists.tsv

# Create group using profile file, group here consists 20-30 women from germany 
python3 main.py -p Germany f 20 30 -f artists.tsv -pf profile.tsv 

# Get help
python3 main.py --help
```