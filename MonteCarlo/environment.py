class Grid:
    def __init__(self, rows, cols, start):
        self.rows = rows
        self.cols = cols
        self.i = start[0]
        self.j = start[1]

    def set(self, rewards, actions):

        self.rewards = rewards
        self.actions = actions

    def set_state(self, s):
        self.i = s[0]
        self.j = s[1]

    def current_state(self):
        return (self.i, self.j)

    def is_terminal(self, s):
        return s not in self.actions

    def move(self, action):
        # check if legal move first
        if action in self.actions[(self.i, self.j)]:
            if action == 'U':
                self.i -= 1
            elif action == 'D':
                self.i += 1
            elif action == 'R':
                self.j += 1
            elif action == 'L':
                self.j -= 1
        return self.rewards.get((self.i, self.j), 0)

    def game_over(self):
        # returns true if game is over, else false
        # true if we are in a state where no actions are possible
        return (self.i, self.j) not in self.actions

    def all_states(self):
        return set(self.actions.keys()) | set(self.rewards.keys())

    def print_values(V, ):
        for i in range(g.rows):
            print("---------------------------")
            for j in range(g.cols):
                v = V.get((i, j), 0)
                if v >= 0:
                    print(" %.2f|" % v, end="")
                else:
                    print("%.2f|" % v, end="")
            print("")

    def print_policy(P, g):
        for i in range(g.rows):
            print("---------------------------")
            for j in range(g.cols):
                a = P.get((i, j), " ")
                print("  %s  |" % a, end="")
            print("")
