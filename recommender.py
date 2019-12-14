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
    for user in data:
        user["neighbors"] = []
        
        for other in data:
            if user["id"] == other["id"]:
                continue
            farthest, index = farthest_close_neighbor(user)
            similarity = pearson.pearson(user, other)

            if len(user["neighbors"]) < n or similarity > farthest:
                user["neighbors"].append({
                    "id": other["id"],
                    "similarity": similarity
                })
            if len(user["neighbors"]) > n:
                user["neighbors"].pop(index)



def generate(data, options):
    neighbors(data, options["n_similar_users"])
    for i in range(10):
        print("NAABURIT")
        print(data[i]["id"], data[i]["neighbors"])

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
recommendations = generate(data, {
    "n_similar_users": 5
})

print(recommendations)

