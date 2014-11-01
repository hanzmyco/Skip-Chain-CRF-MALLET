train=file('ttt','w+')
for index,line in enumerate(open('ttest')):
    if line =='\n' :
        print >>train
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








__author__ = 'hanz'
