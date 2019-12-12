
def pearson(user1, user2):
    # user1 = {
    #     "user_id": 1,
    #     "artists": [
    #         {
    #             "name": "asd",
    #             "listens": 78
    #         },
    #         {
    #             "name": "ewq",
    #             "listens": 50
    #         },
    #         {
    #             "name": "dfg",
    #             "listens": 23
    #         },
    #     ]
    # }
    # user2 = {
    #     "user_id": 3,
    #     "artists": [
    #         {
    #             "name": "asd",
    #             "listens": 78
    #         },
    #         {
    #             "name": "dfg",
    #             "listens": 23
    #         }
    #     ]
    # }
    mean1 = mean(user1)
    mean2 = mean(user2)

    common = joint(user1, user2)

    sums = calculateSums(common, mean1, mean2)
    try:
        return sums[0] / ( (sums[1]**0.5) * (sums[2]**0.5) )
    except:
        return 0

def joint(user1, user2):
    common = []
    for i in user1["artists"]:
        for j in user2["artists"]:
            if i["name"] == j["name"]:
                common.append([i, j])
    return common


def calculateSums(common, user1mean, user2mean):
    sum = 0
    sumUser1 = 0
    sumUser2 = 0
    for i in common:
        sum1 = (i[0]['listens'] - user1mean )
        sum2 = (i[1]['listens'] - user2mean )
        sum = sum + (sum1 * sum2)
        sumUser1 = sumUser1 + (sum1**2)
        sumUser2 = sumUser2 + (sum2**2)
    return [sum, sumUser1, sumUser2]

def mean(user):
    sum = 0
    for i in user["artists"]:
        sum = sum + i["listens"]

    return sum/len(user["artists"])



