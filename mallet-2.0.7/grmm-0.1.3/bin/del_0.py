test=file('f_test','w+')
for line in open('test'):
	t=line.split(' ')
	for ite in t:
		lenn=len(ite)
	#print t
		if lenn >2 and ite[lenn-1]=='0' and ite[lenn-2]=='@':
			print >> test,ite[0:lenn-2],
		else:
			print >>test, ite,

train=file('f_train','w+')
for line in open('train'):
	t=line.split(' ')
	for ite in t:
		lenn=len(ite)
	#print t
		if lenn >2 and ite[lenn-1]=='0' and ite[lenn-2]=='@':
			print >> train,ite[0:lenn-2],
		else:
			print >>train, ite,