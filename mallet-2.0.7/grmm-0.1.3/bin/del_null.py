train= file('f_train', 'w+')
for line in open('train'):
    t = line.strip().split(' ')
    for ite in t:
        if ite == 'W=':
            print >> train, 'W=A'
        else:
            print >> train, ite,
    print >> train

test = file('f_test', 'w+')
for line in open('test'):
    t = line.strip().split(' ')
    for ite in t:
        if ite == 'W=':
            print >> test, 'W=A'
        else:
            print >> test, ite,
    print >> test

__author__ = 'hanz'
