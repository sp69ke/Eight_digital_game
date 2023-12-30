class PuzzleSolver:
    def __init__(self, initial_state):
        self.open_list = []
        self.closed_list = set()
        self.initial_state = initial_state
        self.heuristic = self.manhattan_distance

    def manhattan_distance(self, current):
        distance = 0
        for i in range(3):
            for j in range(3):
                if current.state[i][j] != 0:
                    x, y = divmod(current.state[i][j]-1, 3)
                    distance += abs(x-i) + abs(y-j)
        return distance

    def solve(self):
        heapq.heappush(self.open_list, self.initial_state)
        while self.open_list:
            current = heapq.heappop(self.open_list)
            if current.is_goal_state():
                path = []
                while current.parent is not None:
                    path.append(current.state)
                    current = current.parent
                path.append(self.initial_state.state)
                return path[::-1]
            self.closed_list.add(tuple(map(tuple, current.state)))
            for child in current.generate_children():
                if tuple(map(tuple, child.state)) in self.closed_list:
                    continue
                child.g = current.g + 1
                child.h = self.heuristic(child)
                child.f = child.g + child.h
                for existing in self.open_list:
                    if tuple(map(tuple, child.state)) == tuple(map(tuple, existing.state)):
                        if child.f < existing.f:
                            existing.parent = child.parent
                            existing.g = child.g
                            existing.h = child.h
                            existing.f = child.f
                        break
                else:
                    heapq.heappush(self.open_list, child)
        else:
            print("No solution exists!")