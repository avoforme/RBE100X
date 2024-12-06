#init in nav class should instantiate the heading, east west and north south, default should be north
# two loop for col, two loop for row. each for one +1, -1.
class Manhattan:
    def compute_path(self, start_tuple, end_tuple) -> list[tuple[int, int]]:
        '''
        This function computes the path from the start to the end point.
        It also updates the heading as the path is traversed.
        '''
        current_row, current_col = start_tuple
        end_row, end_col = end_tuple
        path = []
        path.append((current_row, current_col))
        
        while current_row != end_row or current_col != end_col:
            if current_row + 1 <= end_row:
                current_row += 1
                path.append((current_row, current_col))
            if current_row -1 >= end_row:
                current_row -= 1
                path.append((current_row, current_col))
            if current_col +1<= end_col:
                current_col += 1
                path.append((current_row, current_col))
            if current_col -1>= end_col:
                current_col -= 1
                path.append((current_row, current_col))
        return path # type: ignore
