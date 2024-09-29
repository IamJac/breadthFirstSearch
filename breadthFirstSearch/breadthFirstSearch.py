import collections
import subprocess
import time
def bfs(graph,goal,start):
    if goal not in graph:
        print(F'{goal} is not in the graph')
        return
    if start not in graph:
        print(F'{start} is not in the graph')
    else:
        visited=set()
        q=collections.deque()
        if goal==start:
            print(F"{goal} found-It is the starting point of the search")
            return
        else:
            q.append(start)
            while q:
                node=q.popleft()
                if node not in visited:
                    visited.add(node)
                    for i in graph[node]:
                        if i not in visited:
                            if i==goal:
                                print(F"{goal} has been found in the list containing neighbors of {node}")
                                return
                            else:
                                q.append(i)




graph={'A':['B','C','F','G'],
       'B':['A','C','D','G'],
       'C':['A','B','D','E','F','G'],
       'D':['B','C','E','F'],
       'E':['C','D','F'],
       'F':['A','C','D','E','G','H'],
       'G':['A','B','C','F'],
       'H':['F','I'],
       'I':['H']}
num=None
while num!="w":
    print("Input w as the element to be searched to exit")
    print()
    print("Input element to be searched")
    num=str(input())
    if num=="w":
        print("Terminating the program")
        time.sleep(1)
        break
    else:
        print("Input starting point of the search-[A,B,C,D,E,F,G,H or I]")
        num2=str(input())
        bfs(graph,num,num2)
        time.sleep(5)
        subprocess.call('cls',shell=True)