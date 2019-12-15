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
    for neighbor in user['neighbors']:
        
        for artist_key, artist in data[neighbor]['artists'].items():
            if artist_key not in user['artists']:
                unseen[artist_key] = artist
    return unseen

# # Make a 
# def predict():



def generate(data, options):
    neighbors(data, options["n_similar_users"], "jaccard")
    print("NAABURIT")
    test_user = data[list(data.keys())[0]]
    print(test_user)

    

    # print(data)



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
    "n_similar_users": 5
})

# print(recommendations)

