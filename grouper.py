
def get_group(data, country, sex, age1, age2):
    group = {}
    for id, user in data.items():
        try:
            if country == user["country"] and sex == user["sex"] and age1 <= user["age"] and age2 >= user["age"]:
                group[id] = user
        except:
            # Some user have no profile data, ignore them
            pass
    return group
