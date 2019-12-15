import csv

def load_data(filename):
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        users = {}
        for row in csv_reader:
            if row[0] in users.keys():
                users[row[0]]['artists'][row[1]] = {
                    "id": row[1],
                    "name": row[2],
                    "plays": int(row[3])
                }
            else:
                users[row[0]] = {
                    'artists': {
                        row[1]:  {
                            "id": row[1],
                            "name": row[2],
                            "plays": int(row[3])
                        }
                    }
                }

        return users

def load_groups(filename, users):
    with open(filename, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            if row[0] in users:
                users[row[0]]['sex'] = row[1]
                users[row[0]]['age'] = row[2]
                users[row[0]]['country'] = row[3]
