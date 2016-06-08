import random
resultList, total_heads, total_tails, count = [], 0, 0, 0
for i in xrange(5000):
    flip = random.randint(0,1)
    if (flip == 0):
        print("Thowing a coin, you flipped heads, got " + str(total_heads) + " head(s) and " + str(total_tails) + " tail(s) so far")
        total_heads += 1
        count += 1
        resultList.append("Heads")
    else:
        print("Throwing a coin, you flipped tails, got " + str(total_heads) + " head(s) and " + str(total_tails) + " tail(s) so far")
        total_tails += 1
        count += 1
        resultList.append("Tails")
