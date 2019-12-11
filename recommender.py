import csv
filename = "shorter.tsv"

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
                    "plays": row[3]
                })
            else:
                last_user = row[0]
                users.append({
                    "id": row[0],
                    "artists": [{
                        "id": row[1],
                        "name": row[2],
                        "plays": row[3]
                    }]
                })
        print(users)
        print(len(users))


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

load_data(filename)

# def generate(data):
