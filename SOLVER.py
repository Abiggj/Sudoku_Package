class solverr():

    def __init__(self, question_original):

        self.question_set = question_original

        self.sol = {11, 12, 13, 14, 15, 16, 17, 18, 19,
                    21, 22, 23, 24, 25, 26, 27, 28, 29,
                    31, 32, 33, 34, 35, 36, 37, 38, 39,
                    41, 42, 43, 44, 45, 46, 47, 48, 49,
                    51, 52, 53, 54, 55, 56, 57, 58, 59,
                    61, 62, 63, 64, 65, 66, 67, 68, 69,
                    71, 72, 73, 74, 75, 76, 77, 78, 79,
                    81, 82, 83, 84, 85, 86, 87, 88, 89,
                    91, 92, 93, 94, 95, 96, 97, 98, 99}

        self.boxes = {1: (11, 12, 13, 21, 22, 23, 31, 32, 33),
                      2: (14, 15, 16, 24, 25, 26, 34, 35, 36),
                      3: (17, 18, 19, 27, 28, 29, 37, 38, 39),
                      4: (41, 42, 43, 51, 52, 53, 61, 62, 63),
                      5: (44, 45, 46, 54, 55, 56, 64, 65, 66),
                      6: (47, 48, 49, 57, 58, 59, 67, 68, 69),
                      7: (71, 72, 73, 81, 82, 83, 91, 92, 93),
                      8: (74, 75, 76, 84, 85, 86, 94, 95, 96),
                      9: (77, 78, 79, 87, 88, 89, 97, 98, 99)}

        self.question_constants = list()

        for x in range(11, 100):
            if x % 10 == 0:
                continue
            else:
                if self.question_set[x] > 0:
                    self.question_constants.append(x)

        self.solved_set = list()
        self.question_constants = set(self.question_constants)
        self.perm = self.sol - self.question_constants
        self.perm = list(self.perm)

    def solve_please(self):
        self.solver(self.question_set, self.perm, self.boxes, self.question_constants)

    def box_check(self, loc, y, ss, boxes):
        box_number = 0
        r = int(loc / 10)
        c = loc % 10
        for x in range(1, 10):
            if (10 * r) + c in boxes[x]:
                box_number = x
        box = boxes[box_number]
        for x in range(0, 9):
            test = box[x]
            if (10 * r) + c == test:
                continue
            elif ss[test] == y:
                return 0
        return 1

    def column_check(self, loc, y, ss):
        r = int(loc / 10)
        c = loc % 10
        for x in range(1, 10):
            if r == x:
                continue
            if ss[(10 * x) + c] == y:
                return 0
        return 1

    def row_check(self, loc, y, ss):
        r = int(loc / 10)
        c = loc % 10
        for x in range(1, 10):
            if c == x:
                continue
            elif ss[(10 * r) + x] == y:
                return 0
        return 1

    def possibility(self, loc, ss, y, bb):
        possible = self.row_check(loc, y, ss)
        possible += self.column_check(loc, y, ss)
        possible += self.box_check(loc, y, ss, bb)
        if possible == 3:
            return True

    def possible_check(self):
        p = len(self.question_constants)
        total, rown, coln, num, loc = 0, 0, 0, 0, 0
        for x in self.question_constants:
            loc = x
            num = self.question_set[loc]
            total += self.row_check(loc, num, self.question_set) + self.column_check(loc, num, self.question_set) + self.box_check(loc, num, self.question_set, self.boxes)
        if total / 3 == p:
            return True
        else:
            return False

    def Setter(self, SS):
        global solved_set
        if type(SS) == type(' '):
            self.solved_set = SS
        else:
            self.solved_set = list(SS)
            self.solved_set = dict(self.solved_set)

    def solver(self, solution_set, per, bb, qc):
        for x in per:
            if solution_set[x] == 0:
                for y in range(1, 10):
                    if self.possibility(x, solution_set, y, bb):
                        solution_set[x] = y
                        self.solver(solution_set, per, bb, qc)
                        solution_set[x] = 0
                return
        if x == per[-1]:
            self.Setter(solution_set.items())