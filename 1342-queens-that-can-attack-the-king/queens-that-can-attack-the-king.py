class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        
        same_row = []
        same_col = []
        same_diag_up = []
        same_diag_down = []
        
        for i in queens:
            # row
            if i[0] == king[0]:
                same_row.append(i)
            # column
            elif i[1] == king[1]:
                same_col.append(i)
            # \
            elif king[0] - king[1] == i[0] - i[1]:
                same_diag_up.append(i)
            # /
            elif king[0] + king[1] == i[0] + i[1]:
                same_diag_down.append(i)
        
        # row
        diff_left = float('inf')
        diff_right = float('inf')
        row_ans_left = []
        row_ans_right = []
        
        for i in same_row:
            if i[1] < king[1]:
                if king[1] - i[1] < diff_left:
                    diff_left = king[1] - i[1]
                    row_ans_left = [i]
            else:
                if i[1] - king[1] < diff_right:
                    diff_right = i[1] - king[1]
                    row_ans_right = [i]
        
        # column
        diff_above = float('inf')
        diff_below = float('inf')
        col_ans_above = []
        col_ans_below = []
        
        for i in same_col:
            if i[0] < king[0]:
                if king[0] - i[0] < diff_above:
                    diff_above = king[0] - i[0]
                    col_ans_above = [i]
            else:
                if i[0] - king[0] < diff_below:
                    diff_below = i[0] - king[0]
                    col_ans_below = [i]
        
        # \
        diff_above = float('inf')
        diff_below = float('inf')
        diag_up_ans_above = []
        diag_up_ans_below = []
        
        for i in same_diag_up:
            if i[0] < king[0]:
                if king[0] - i[0] < diff_above:
                    diff_above = king[0] - i[0]
                    diag_up_ans_above = [i]
            else:
                if i[0] - king[0] < diff_below:
                    diff_below = i[0] - king[0]
                    diag_up_ans_below = [i]
        
        # /
        diff_above = float('inf')
        diff_below = float('inf')
        diag_down_ans_above = []
        diag_down_ans_below = []
        
        for i in same_diag_down:
            if i[0] < king[0]:
                if king[0] - i[0] < diff_above:
                    diff_above = king[0] - i[0]
                    diag_down_ans_above = [i]
            else:
                if i[0] - king[0] < diff_below:
                    diff_below = i[0] - king[0]
                    diag_down_ans_below = [i]
        
        ans.extend(row_ans_left)
        ans.extend(row_ans_right)
        ans.extend(col_ans_above)
        ans.extend(col_ans_below)
        ans.extend(diag_up_ans_above)
        ans.extend(diag_up_ans_below)
        ans.extend(diag_down_ans_above)
        ans.extend(diag_down_ans_below)
        
        return ans
