from itertools import product
from copy import deepcopy
from gc import collect

class Node:
    def __init__(self,id):
        self.id = id
        self.dict = {}

    def __str__(self):
        return str(self.id) + " : " + str(self.dict)

    def __repr__(self):
        return str(self.id) + " : " + str(self.dict)

ptarget = {}
ctarget = {}
def tryDelete(nodes,_len):
    global ctarget
    global ptarget
    for i in range(len(nodes)):
        ptarget = {}
        ctarget = {}
        collect()
        y = nodes[:]
        x = y.pop(i)
        tNodes = []
        for node in y:
            for input,result in node.dict.items():
                if result == x:
                    node.tDict = deepcopy(node.dict)
                    tNodes.append(node)
                    if x.dict[input] == x.id:
                        node.dict[input] = node
                    else:
                        node.dict[input] = x.dict[input]
                    
        if pathPossible(y,_len ,False) == -1:
            return x.id
        for n in tNodes:
            n.dict = n.tDict
            del n.tDict
    return -2

def FindTarget(node,p):
    if len(p) == 1:
        return node.dict[p[0]]
    node_in_ptarget = node in ptarget
    node_in_ctarget = node in ctarget
    if not node_in_ptarget or p not in ptarget[node]:
        x = Gnodes[FindTarget(node,p[:-1])].dict[p[-1]]
        if not node_in_ctarget:
            ctarget[node] = {}
        ctarget[node][p] = x
        if not node_in_ptarget:
            ptarget[node] = {}
        ptarget[node][p] = x
    return ptarget[node][p]

def allSatisy(nodes,p):
    x = FindTarget(nodes[0], p)
    return all(FindTarget(node, p) == x for node in nodes[1:])

def allPossiblePaths(l,n):
    #x = int(((l+1)*(l+2))/2)
    global ctarget
    global ptarget
    for i in range(1, n + 1):
        ptarget = ctarget
        ctarget = {}
        for p in product(range(l),repeat=i):
            yield p

def pathPossible(nodes,_len ,isItereate=True):
    i = 1
    isFound = False
    for p in allPossiblePaths(_len,len(nodes)):
        if allSatisy(nodes,p):
            isFound = True
            break

    if isFound:
        return -1
    elif not isItereate:
        return -2
    else:
        return tryDelete(nodes,_len)

Gnodes = []
def answer(li):  
    Gnodes[:] = []
    target = {}
    for i in range(len(li)):
        Gnodes.append(Node(i))#[i] = Node(i)
    for i in range(len(li)):
        for j in range(len(li[i])):
            Gnodes[i].dict[j] = li[i][j]
    return pathPossible(Gnodes,len(Gnodes[0].dict))

def check(li,ans):
    x = answer(li)
    print(str(li) + " : " + str(ans) + " : " + str(x))

def main():
    check([[2,1],[2,0],[3,1],[1,0]],-1)
    check([[1,2],[1,1],[2,2]],1)
    check([[1,3,0],[1,0,2],[1,1,2],[3,3,3]],-1)

if __name__ == '__main__':
    main()