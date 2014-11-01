
train=file('train','w+')
index=1
for line in open('featuretrain.txt'):
    if line =='\n' :
        print >>train,'\n',
        print >>train, '\n',

    else:
        tokens=line.strip().split(' ')
        for ite in tokens:
            lenn=len(ite)
            if lenn >2 and ite[lenn-1]=='0' and ite[lenn-2]=='@':
                print >> train,ite[0:lenn-2],
            else:
                print >>train, ite,
        if len(tokens)==0:
            print >>train

        print >>train
    index+=1

test=file('test','w+')
index=1
for line in open('featuretest.txt'):
    #if index==17:
    #    print 'fuck'
    if line=='\r\n':
        print >>test
        print >> test

    else:
        tokens=line.strip().split(' ')
        for ite in tokens:
            lenn=len(ite)
            if lenn >2 and ite[lenn-1]=='0' and ite[lenn-2]=='@':
                print >> test,ite[0:lenn-2],
            else:
                print >>test, ite,
        if len(tokens)==0:
            print>>test
        print >>test
    index+=1







__author__ = 'hanz'
