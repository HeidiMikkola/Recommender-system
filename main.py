import csv_reader
import recommender
import grouper


data = csv_reader.load_data("tools/shortest.tsv")
csv_reader.load_profiles('tools/profile.tsv', data)
group = grouper.get_group(data, 'Germany', 'f', 20, 30)
# print(group)
# ['00035a0368fd249d286f683e816fbdc97cbfa7d9']
recommendations = recommender.generate(data, group.keys(), {
    "n_similar_users": 5,
    "sim_type": "jaccard"
})

print(recommendations)