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
        prediction_value = 0
        try:
            prediction_value = similarity.mean(user) +  ( upper_sum / lower_sum )
        except:
            pass
        prediction = {
            'prediction': prediction_value
        }
        prediction.update(val[0])
        predict.append(prediction)
    return predict


# Generates recommendations for given user ids, sorts them by relevancy
# options: 
#   n_similar_users: int, how many closest neighbors are calculated
#   sim_type: 'pearson' | 'jaccard', which similarity algorithm is used
#   n_recommendations: int, how many best recommandations are returned
def generate(data, users, options):
    neighbors(data, options["n_similar_users"], options["sim_type"])
    recommendations = {}
    for user_id in users:
        user = data[user_id]
        pred = list(filter(lambda x : x['prediction'] > 0, predictions(data, user, unseen_items(data, user))))
        pred.sort(key = lambda x : x['prediction'], reverse = True)
        recommendations[user_id] = pred[:options["n_recommendations"]]
    return recommendations


def borda_count(users):
    ranks = {}
    # assume the recommendations are already sorted
    for user_id, recommendations in users.items():
        for i, artist in enumerate(recommendations):
            if artist['id'] in ranks:
                ranks[artist['id']]['rank'] += len(recommendations) - i
            else:
                ranks[artist['id']] = {
                    'name': artist['name'],
                    'id': artist['id'],
                    'rank': len(recommendations) - i
                }

    return ranks
