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
	c = 0
	if (a == b):
		c = 1
	else:
		pass
	return c
def frame(a,b,list):
	#sums the neighbors of (a,b)
	c = 0
	for u in (-1,0,1):
		for v in (-1,0,1):
			c = list[a+u,b+v] + c
	c = c - list[a,b]
	return c
def iter(old,new,span,pan):
	for i in range(span-1):
		s = ''
		t = ''
		for j in range(span-1):
			s = s + str(old[i+1,j+1])
			t = t + str(new[i+1,j+1])
			new[i+1,j+1] = delta(frame(i+1,j+1,old),2) * old[i+1,j+1] + delta(frame(i+1,j+1,old),3)
			#stores the state of the cell at the next iteration in new
		print s
		#if (pan == 1):
		#	'log.txt'.write(s + '\n')
		#	'log.txt'.write(t + '\n')
		#else:
		#	pass
	for i in range(span-1):
		for j in range(span-1):
			(old[i+1,j+1],new[i+1,j+1]) = (new[i+1,j+1], old[i+1,j+1])
	#swaps old and new
	return 0
def init(eggs,spam,span):
	for i in range(span+1):
		for j in range(span+1):
			eggs[i,j] = 0
			spam[i,j] = 0
	#initializes as null
	return 0
life = {}
efil = {}
init(life,efil,50)
print 'Define initial conditions'
#allows user to input a custom starting colony
while True:
	print 'finished?'
	s = raw_input('')
	if (s == 'no') or (s == 'No'):
		i = int(raw_input('x-coord:'))
		j = int(raw_input('y-coord:'))
		flip(i,j,life)
	else:
		print 'How many iterations?'
		h = int(raw_input(''))
		#print 'logit?'
		#s = raw_input('')
		#logit = delta(s,'yes') + delta(s,'Yes')
		logit = 0
		break
#open('log.txt','a')
for i in range(h):
	iter(life,efil,50,logit)
#'log.txt'.close()
