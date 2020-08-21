from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    def queenPlace(row, col):
        if row == n:  # Succesfully placed in all rows with out conflicts.
            result.append()  # Adding that combination to result.
            return
        for col in range(n):  # Placing all columns from 0 to n-1.
            attack = False  # Flag to check if it is in attacking position.
            for r, c in enumerate(rows[:row]):
                # Checking for conflicts with previous rows.
                if abs(c-col) in (0, row - r):
                    # If conflict exists, we break the loop there and col moves to next option.
                    attack = True
                    break
            if not attack:
                # If no conflict found, we place a queen in that column and recursively apply the same function to the next row.
                rows[row] = col
                queenPlace(row+1, col)
    rows = [0]*n
    result = []
    queenPlace(0,0)
    return result


print(solveNQueens(5))
