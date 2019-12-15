import csv_reader
import recommender
import grouper
import json
import argparse

parser = argparse.ArgumentParser(description='Calculate artist recommendations')
parser.add_argument('-u', dest='n_users', type=int, default=5,
    help='Number of neighbors calculated when generating recommendations')
parser.add_argument('-r', dest='n_recommendations', type=int, default=5,
    help='Number of recommendations calculated per user')
parser.add_argument('-a', dest='algorithm',
    help='Algorithm used, "jaccard" or "pearson"', default='jaccard')
parser.add_argument('-i', dest='ids', nargs='*')
parser.add_argument('-p', dest='profiles', nargs='*')
args = parser.parse_args()

data = csv_reader.load_data("tools/shortest.tsv")
csv_reader.load_profiles('tools/profile.tsv', data)
group = []
if args.profiles is not None:
    profiles = grouper.get_group(data, args.profiles[0], args.profiles[1], int(args.profiles[2]), int(args.profiles[3]))
    group = profiles.keys()
elif args.ids is not None:
    group = args.ids



recommendations = recommender.generate(data, group, {
    "n_similar_users": args.n_users,
    "n_recommendations": args.n_recommendations,
    "sim_type": args.algorithm
})

borda = recommender.borda_count(recommendations)
group_rec = sorted(list(borda.values()), key = lambda x : x['rank'], reverse = True)

print(json.dumps(group_rec, indent=4))
