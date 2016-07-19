import numpy as np 
from matplotlib import pyplot as plt 



def shouldStop(): # defines stopping iteration criteria
	if itercounter == MaxIterCount:
		return True
	else :
		# check if there is any change in the previous and current means
		for i in range(K):
			if mu[i] != previous_mu[i]:
				return False

		return True

# assign the cluster centroids as the mean of sliced distribution

def initialize_centroids():
	for i in range(K):
		previous_mu[i] = (
				round(np.mean(x1[i*N/K:(i+1)*N/K])),
				round(np.mean(y1[i*N/K:(i+1)*N/K]))
			)

	
def assign():
	point_specific_list = [[] for i in range(K)]
	for x,y in zip(x1,y1):
		mindist = 999999
		idx=0
		for i, each in enumerate(previous_mu):
			tempdist = np.linalg.norm(np.array([x,y]) - np.array(each))
			if tempdist < mindist:
				mindist = tempdist
				idx = i;
		point_specific_list[idx].append((x,y))

	# print point_specific_list[0]
	for i in range(K):
		# update current mu with mean of point specific lists
		tmp = np.mean(point_specific_list[i], axis=0)
		# print tmp
		mu[i] = (round(tmp[0]), round(tmp[1]))	

	return point_specific_list

def generateRandom(TopMaxValX, TopMaxValY, N):
	x1 = np.random.randint(TopMaxValX,size=N)
	y1 = np.random.randint(TopMaxValY,size=N)
	co = zip(x1, y1)
	return co, x1, y1


K =2 # set number of clusters
mu = [(0,0) for i in range(K)] # define initial relative means

previous_mu = [(-1,-1) for i in range(K)] # define initial relative means

MaxIterCount = 1000;	

itercounter = 0;

N=50

co, x1, y1 = generateRandom(TopMaxValX=500, TopMaxValY=1000, N=100)
initialize_centroids()


# plt.scatter(x1, y1)
# plt.show()

print previous_mu

while not shouldStop():
	psl = assign()
	itercounter+=1
 
if itercounter == MaxIterCount:
	print "MAx count reached", itercounter 

print len(psl)
plt.plot(psl[0],'ro')
plt.plot(psl[1],'bo')
# plt.plot(psl[2],'go')
plt.show()



