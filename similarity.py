def pearson(user1, user2):
    common = joint(user1, user2)
    if len(common) == 0:
        return 0
    mean1 = mean(user1)
    mean2 = mean(user2)

    sums = calculateSums(common, mean1, mean2)
    try:
        return sums[0] / ( (sums[1]**0.5) * (sums[2]**0.5) )
    except:
        return 0

def joint(user1, user2):
    common = []
    for i in user1["artists"]:
        if i in user2["artists"]:
            common.append([user1['artists'][i], user2['artists'][i]])
    return common


def calculateSums(common, user1mean, user2mean):
    sum = 0
    sumUser1 = 0
    sumUser2 = 0
    for i in common:
        sum1 = (i[0]['plays'] - user1mean )
        sum2 = (i[1]['plays'] - user2mean )
        sum = sum + (sum1 * sum2)
        sumUser1 = sumUser1 + (sum1**2)
        sumUser2 = sumUser2 + (sum2**2)
    return [sum, sumUser1, sumUser2]

def mean(user):
    sum = 0
    for key, val in user["artists"].items():
        sum = sum + val["plays"]

    return sum/len(user["artists"])

def jaccard(user1, user2):
    common = len(joint(user1, user2))
    return common / (len(user1["artists"]) + len(user2["artists"]) - common)
    

