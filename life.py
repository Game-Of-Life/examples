#game of life
#this program is a python command line implementation of conway's game of life
#this will only serve as a proof-of-concept and should be kept separate from the 'source' repository
#enjoy
def flip(a,b,list):
	#changes the state of a cell
	c = list[a,b]
	list[a,b] = 1 - c
	return 0
def delta(a,b):
	#compares a and b
	#if delta(a,b) = 1 then for all c != b, delta(a,c) = 0
	#this allows for a mathematical expression of 'this or that' as delta(x,this) + delta(x,that)
	c = 0
	if (a == b):
		c = 1
	else:
		pass
	return c
def frame(a,b,list):
	#sums the neighbors of [a,b] in the list 'list'
	c = 0
	for u in (-1,0,1):
		for v in (-1,0,1):
			c = list[a+u,b+v] + c
	c = c - list[a,b]
	#undoes the inclusion of list[a,b] in the sum
	return c
def iter(old,span):
#executes one iteration of the rules of Conway's Game of Life
	new = {}
	for i in range(span-1):
		for j in range(span-1):
			new[i+1,j+1] = delta(frame(i+1,j+1,old),2) * old[i+1,j+1] + delta(frame(i+1,j+1,old),3)
			#stores the state of the cell at the next iteration in new
	for i in range(span-1):
		for j in range(span-1):
			old[i+1,j+1] = new[i+1,j+1]
	return 0
def init(eggs,spam):
	for i in range(spam+1):
		for j in range(spam+1):
			eggs[i,j] = 0
	#initializes as null
	return 0
def display(list,span):
	for i in range(span-1):
		s = ""
		for j in range(span-1):
			s = s + str(life[i+1,j+1])
		print s
life = {}
init(life,50)
print 'Define initial conditions'
#allows user to input a custom starting colony
print 'put dashes, spaces, or underscores between different coordinates'
print 'An example would be: 13 11 34 15 32 5 1 11'
s = raw_input('')
s.replace('-',' ')
s.replace('_',' ')
slist = s.split(' ')
for i in range(0,len(slist),2):
	flip(int(slist[i]),int(slist[i+1]),life)
print 'How many iterations?'
h = int(raw_input(''))
for i in range(h):
	display(life,50)
	iter(life,50)
