def heapify(hp,i):
	n=len(hp)
	while i<=(n//2):
		cur=hp[i]
		left=hp[2*i] if 2*i < n else None
		right=hp[(2*i)+1]  if 2*i+1 < n else None

		if (cur<left and left>right):
			hp[i],hp[(2*i)]=hp[(2*i)],hp[i]
			#print "left",hp[i]
			i=2*i
			
		elif cur<right and right>left:
			hp[i],hp[(2*i)+1]=hp[(2*i)+1],hp[i]
			#print "right",hp[i]
			i=2*i+1
		
		else:
			break
			
def buildheap(hp):
	n=len(hp)
	for j in range(((n//2)),0,-1):
		heapify(hp,j)
		
def insert(hp,e):
	hp.append(e)
	buildheap(hp)

def delete(hp):
	hp[1]=hp[-1]
	hp.pop()
	heapify(hp,1)	