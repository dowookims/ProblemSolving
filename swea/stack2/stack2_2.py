class Stack:
    def __init__(self):
        self.stack = [None] * 250
        self.top = -1

    def pop(self):
        if self.top == -1:
            return None
        result = self.stack[self.top]
        self.stack[self.top] = 0
        self.top -= 1
        return result

    def push(self, item):
        self.top += 1
        self.stack[self.top] = item
        return

    def peek(self):
        return self.stack[self.top]

    def is_empty(self):
        return True if self.top == -1 else False


def find_way(y, x):
    for i in range(4):
        if 0 <= y + delta[i][0] <= (N - 1) and 0 <= x + delta[i][1] <= (N - 1):
            if maze[y + delta[i][0]][x + delta[i][1]] == '3':
                route.push((y + delta[i][0], x + delta[i][1]))
                return True
            if not (int(maze[y + delta[i][0]][x + delta[i][1]]) or visited[y + delta[i][0]][x + delta[i][1]]):
                route.push((y + delta[i][0], x + delta[i][1]))
                visited[y + delta[i][0]][x + delta[i][1]] = 1
                return False
    route.pop()
    return False


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [''] * N
    for i in range(N):
        maze[i] = input()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    route = Stack()
    for x in range(N):
        for y in range(N):
            if maze[y][x] == '2':
                route.push((y, x))

    while True:
        if route.is_empty():
            print("#{} 0".format(t))
            break
        y, x = route.peek()[0], route.peek()[1]
        if find_way(y, x):
            print("#{} 1".format(t))
            break