
def canReach(x,y):
	while x>= 1 and y>=1:
		if x > y:
			x -= y
		else:
			y -=x
		if x==1 and y==1:
			return True
	return False


def zombieClusters(zombies):
    clusterIdx = 0
    zombieClusterIdxs = [0] * len(zombies)
    for zombieIdx in xrange(len(zombies)):
        if zombieClusterIdxs[zombieIdx] != 0:
            continue

        clusterIdx += 1
        connectedZombies = [zombieIdx]
        while connectedZombies:
            zi = connectedZombies.pop()

            if zombieClusterIdxs[zi] != 0:
                continue

            zombieClusterIdxs[zi] = clusterIdx

            for zi2 in xrange(len(zombies)):
                if zi != zi2 and zombies[zi][zi2]:
                    connectedZombies.append(zi2)

    return clusterIdx
print zombieClusters([[1100],[1110],[0110],[0001]])

