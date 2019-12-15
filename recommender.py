import similarity
import csv_reader

# get the farthest neighbor pf the user and its index,
# so that we can easily replace it with a closer one
def farthest_close_neighbor(user):
    farthest = 100
    index = -1
    for n_key, neighbor in user["neighbors"].items():
        if neighbor["similarity"] < farthest:
            farthest = neighbor["similarity"]
            index = n_key
    return [farthest, index]


# naive method for getting n amount of closest neighbors
def neighbors(data, n, simtype):
    for user_key in data:
        user = data[user_key]
        user["neighbors"] = {}

        for other_key in data:
            other = data[other_key]
            if user_key == other_key:
                continue
            farthest, index = farthest_close_neighbor(user)
            sim = None
            if simtype == "pearson":
                sim = similarity.pearson(user, other)
            else:
                sim = similarity.jaccard(user, other)
            if len(user["neighbors"]) < n or sim > farthest:
                user["neighbors"][other_key] = {
                    "id": other_key,
                    "similarity": sim
                }
            if len(user["neighbors"]) > n:
                user["neighbors"].pop(index)

# Get the items the users have not seen, but their neighbors have 
def unseen_items(data, user):
    unseen = {}
    for n_key, neighbor in user['neighbors'].items():
        for artist_key, artist in data[n_key]['artists'].items():
            if artist_key not in user['artists']:
                if artist_key in unseen:
                    unseen[artist_key].append(neighbor)
                else:
                    unseen[artist_key] = [artist, [neighbor]]
    return unseen

# Get predictions for a user based on the neighbors
def predictions(data, user, unseen):
    predict = []
    for artist_key, val in unseen.items():
        upper_sum = 0
        lower_sum = 0
        for neighbor in val[1]:
            neighbor_artist = data[neighbor['id']]['artists'][artist_key]
            upper_sum += neighbor['similarity'] * ( neighbor_artist['plays'] - similarity.mean(data[neighbor['id']]) )
            lower_sum += neighbor['similarity']
        prediction = {
            'prediction': similarity.mean(user) +  ( upper_sum / lower_sum )
        }
        prediction.update(val[0])
        predict.append(prediction)
    return predict


def generate(data, options):
    neighbors(data, options["n_similar_users"], options["sim_type"])
    test_user = data['00035a0368fd249d286f683e816fbdc97cbfa7d9']
    unseen = unseen_items(data, test_user)

    pred = predictions(data, test_user, unseen)
    print(pred)


# data in the form
# [
#     {
#         user_id: 12345
#         artists: [
#             {
#                 listens: 12
#                 name: 'artist1'
#             },
#             {
#                 listens: 43
#                 name: 'artist2'
#             },
#         ]
#     }
# ]

data = csv_reader.load_data("tools/shortest.tsv")
csv_reader.load_groups('tools/profile.tsv', data)
recommendations = generate(data, {
    "n_similar_users": 5,
    "sim_type": "jaccard"
})

# print(recommendations)

