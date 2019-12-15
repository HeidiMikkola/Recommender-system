import csv_reader
import recommender
import grouper


data = csv_reader.load_data("tools/shortened.tsv")
csv_reader.load_groups('tools/profile.tsv', data)
recommendations = recommender.generate(data, ['00035a0368fd249d286f683e816fbdc97cbfa7d9'], {
    "n_similar_users": 5,
    "sim_type": "jaccard"
})
group = grouper.get_group(data, 'Germany', 'f', 20, 30)
print(group)

print(recommendations)