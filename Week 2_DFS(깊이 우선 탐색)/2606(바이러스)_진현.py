import sys

class Stack:
    def __init__(self) -> None:
        self.s_list = []
        self.top = 0
        self.max = 100
    
    def push(self, item) -> None:
        if self.pop == self.max:
            exit(1)
        self.s_list.append(item)
        self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            exit(1)
        self.top -= 1
        return self.s_list.pop()

    def isempty(self) -> bool:
        return self.top == 0
    
    def isfull(self) -> bool:
        return self.top == self.max


def dfs(com_n, edges) -> None:
    stack = Stack()
    visited = [False] * (com_n + 1) # index 0 is dummy
    cnt = -1 # 1번 컴퓨터 제외

    stack.push(1)
    while not stack.isempty():
        vtx = stack.pop()

        if visited[vtx]:
            continue
        else:
            visited[vtx] = True
            cnt += 1
        
        for i in range(len(edges[vtx])):
            if not visited[edges[vtx][i]]:
                stack.push(edges[vtx][i])
    
    print(cnt)


com_n = int(sys.stdin.readline())
e_n = int(sys.stdin.readline())
edges = dict()
for i in range(1, com_n + 1):
    edges[i] = []

for _ in range(e_n):
    st, dest = map(int, sys.stdin.readline().split())
    edges[st].append(dest)
    edges[dest].append(st)
dfs(com_n, edges)
