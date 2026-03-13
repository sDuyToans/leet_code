class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 3 x 3
        # O (r x c) + O (r x c) + O (r x c) -> O(r x c)
        # rows = len(board)
        # cols = len(board[0])

        # row_start = 3
        #
        # while row_start <= rows:
        #     cols_start = 3
        #
        #     while cols_start <= cols:
        #         mem = [0] * (rows + 1)
        #         for i in range(row_start - 3, row_start):
        #             for j in range(cols_start - 3, cols_start):
        #                 if board[i][j] == '.':
        #                     continue
        #                 else:
        #                     number = int(board[i][j])
        #                     if mem[number] == 1:
        #                         return False
        #                     else:
        #                         mem[number] += 1
        #         cols_start += 3
        #
        #     row_start += 3
        #
        # for row in range(rows):
        #     arr = [0] * (cols + 1)
        #     for col in range(cols):
        #         if board[row][col] == '.':
        #             continue
        #         current = int(board[row][col])
        #         if arr[current] != 0:
        #             return False
        #         else:
        #             arr[current] = 1
        #
        # for col in range(cols):
        #     arr = [0] * (cols + 1)
        #     for row in range(rows):
        #         if board[row][col] == '.':
        #             continue
        #         current = int(board[row][col])
        #         if arr[current] != 0:
        #             return False
        #         else:
        #             arr[current] = 1
        #
        # return True

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                current = board[r][c]
                if current == '.':
                    continue

                box_idx = (r // 3) * 3 + (c // 3)

                if current in rows[r] or current in cols[c] or current in boxes[box_idx]:
                    return False

                rows[r].add(current)
                cols[c].add(current)
                boxes[box_idx].add(current)

        return True


s = Solution()

tests = [
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
    [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
    [[".", ".", "4", ".", ".", ".", "6", "3", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     ["5", ".", ".", ".", ".", ".", ".", "9", "."],
     [".", ".", ".", "5", "6", ".", ".", ".", "."],
     ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
     [".", ".", ".", "7", ".", ".", ".", ".", "."],
     [".", ".", ".", "5", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "."]],
    [[".", ".", ".", ".", "5", ".", ".", "1", "."],
     [".", "4", ".", "3", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
     [".", ".", "2", ".", "7", ".", ".", ".", "."],
     [".", "1", "5", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "2", ".", ".", "."],
     [".", "2", ".", "9", ".", ".", ".", ".", "."],
     [".", ".", "4", ".", ".", ".", ".", ".", "."]]
]

for test in tests:
    print(s.isValidSudoku(test))
