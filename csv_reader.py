import csv

def load_data(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        users = {}
        for row in csv_reader:
            if row[0] in users.keys():
                users[row[0]]['artists'].append({
                    "id": row[1],
                    "name": row[2],
                    "plays": int(row[3])
                })
            else:
                users[row[0]] = {
                    'artists': [{
                        "id": row[1],
                        "name": row[2],
                        "plays": int(row[3])
                    }]
                }

        return users

def load_groups():
    