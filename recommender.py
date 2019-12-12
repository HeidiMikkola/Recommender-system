import csv
import pearson

def load_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        users = []
        last_user = ''
        for row in csv_reader:
            if row[0] == last_user:
                users[len(users)-1]['artists'].append({
                    "id": row[1],
                    "name": row[2],
                    "plays": int(row[3])
                })
            else:
                last_user = row[0]
                users.append({
                    "id": row[0],
                    "artists": [{
                        "id": row[1],
                        "name": row[2],
                        "plays": int(row[3])
                    }]
                })
        return users

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

data = load_data("tools/shortest.tsv")
recommendations = generate(data, {
    "n_similar_users": 5
})

print(recommendations)

