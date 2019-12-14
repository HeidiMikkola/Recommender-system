import pearson
import csv_reader

def farthest_close_neighbor(user):
    farthest = 100
    index = -1
    for i, neighbor in enumerate(user["neighbors"]):
        if neighbor["similarity"] < farthest:
            farthest = neighbor["similarity"]
            index = i
    return [farthest, index]


# naive method for getting n amount of closest neighbors
def neighbors(data, n):
    for user_key in data:
        user = data[user_key]
        user["neighbors"] = []

        for other_key in data:
            other = data[other_key]
            if user_key == other_key:
                continue
            farthest, index = farthest_close_neighbor(user)
            similarity = pearson.pearson(user, other)

            if len(user["neighbors"]) < n or similarity > farthest:
                user["neighbors"].append({
                    "id": other_key,
                    "similarity": similarity
                })
            if len(user["neighbors"]) > n:
                user["neighbors"].pop(index)

# Get the items the users have not seen, but their neighbors have 
# def unseen_items():


# # Make a 
# def predict():



def generate(data, options):
    neighbors(data, options["n_similar_users"])
    print("NAABURIT")
    test_user = data[data.keys()[0]]
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
# print(data)
recommendations = generate(data, {
    "n_similar_users": 5
})

# print(recommendations)

