import csv_reader
import recommender
import grouper
import json

data = csv_reader.load_data("tools/shortest.tsv")
csv_reader.load_profiles('tools/profile.tsv', data)
group = grouper.get_group(data, 'United States', 'f', 0, 100)

recommendations = recommender.generate(data, group.keys(), {
    "n_similar_users": 5,
    "n_recommendations": 5,
    "sim_type": "jaccard"
})

# print(recommendations)
borda = recommender.borda_count(recommendations)
group_rec = sorted(list(borda.values()), key = lambda x : x['rank'], reverse = True)

print(json.dumps(group_rec, indent=4))
