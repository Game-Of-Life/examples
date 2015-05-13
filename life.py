#game of life
#this program is a python command line implementation of conway's game of life
#this will only serve as a proof-of-concept and should be kept separate from the 'source' repository
#enjoy
flip = lambda x,y,z: 1-z[x,y]
delta = lambda x,y: 1 if x == y else 0
def frame(a,b,list):
	#sums the neighbors of [a,b]
	c = 0
	for i in (-1,0,1):
		for j in (-1,0,1):
			c = list[a+i,b+j] + c
	c = c - list[a,b]
	return c
def iter(old,span):
#executes one iteration of the rules of Conway's Game of Life
	new = {}
	for i in range(span):
		for j in range(span):
			#computes the next generation cell by cell
			new[i+1,j+1] = delta(frame(i+1,j+1,old),2) * old[i+1,j+1] + delta(frame(i+1,j+1,old),3)
			#stores the state of the cell at the next iteration in new
	for i in range(span):
		for j in range(span):
			old[i+1,j+1] = new[i+1,j+1]
	return 0
def init(list,span):
	for i in range(span+2):
		#the two extra rows and columbs make a border around the grid
		#this avoids the problem of frame() trying to call the value of an out-of-range key
		for j in range(span+2):
			list[i,j] = 0
	#initializes as null
	return 0
def display(list,span):
	for i in range(span):
		s = ''
		for j in range(span):
			s = s + str(life[i+1,j+1])
		print s
		#makes and prints a string that represents one row on the grid
life = {}
print 'Enter the size of the grid'
g = int(raw_input(''))
init(life,g)
print 'Define initial conditions'
#allows user to input a custom starting colony
print 'Put dashes, spaces, or underscores between numbers'
print 'An example would be: 13 11 34 15 32 5 1 11'
s = raw_input('')
s.replace('-',' ')
s.replace('_',' ')
slist = s.split(' ')
for i in range(0,len(slist),2):
	m = int(slist[i+1])
	n = int(slist[i])
	life[m,n] = flip(m,n,life)
	#changes the state of the (ith,ith+1th) cell
	#repeating the same coordinate an even # of times does not change its state
	#repeating the same coordinate an odd # of times does change its state
print 'How many iterations?'
h = int(raw_input(''))
for i in range(h):
	display(life,g)
	iter(life,g)
#prints the grid before iterating it
#this results in an extra iteration, but said generation is never printed
#this also quickly fills the console with 1's and 0's
