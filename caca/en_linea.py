#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
'''
Created on 13/09/2018

@author: ernesto
'''

n, m = [int(x) for x in input().strip().split(" ")]

p = set(range(1, n + 1))

ops = []

if(m > 1):
    for _ in range(0, m):
        s, n_s = [x for x in input().strip().split(" ")]
        n = int(n_s)
        ops.append((s, n))
        
    cola = ops[1:]
    cola_de_rata = ops[:-1]
#    print("cola {} cola de rata {}".format(cola, cola_de_rata))
    
    if(ops[0][1] not in [e[1] for e in cola]):
        p -= set([e[1] for e in cola])
        
    if(ops[-1][1] not in [e[1] for e in cola_de_rata]):
        p -= set([e[1] for e in cola_de_rata])
    
    if(ops[0][0] == '-'):
        p.remove(ops[0][1])
        
    if(ops[-1][0] == '+'):
        p.remove(ops[-1][1])
        
    for i in range(1, m - 1):
        p.discard(ops[i][1])

print(len(p))
if(len(p)):
    print(" ".join(map(str, sorted(p))))
