train=file("train",'w+')
for line in open("conll2000.train1k.txt"):
	if line=='\n':
		print >>train
	token=line.split(' ')
	for index, ite in enumerate(token):
		if index!=0:
			print >> train, ite,




test=file("test",'w+')
for line in open("conll2000.test1k.txt"):
	if line =='\n':
		print >>test
	token=line.split(' ')
	for index, ite in enumerate(token):
		if index!=0:
			print >> test, ite,



