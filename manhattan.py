#init in nav class should instantiate the heading, east west and north south, default should be north
# two loop for col, two loop for row. each for one +1, -1.
class Manhattan:
    def compute_path(self, start_tuple, end_tuple, heading) -> list[tuple[int, int]]:
        '''
        This function computes the path from the start to the end point.
        It also updates the heading as the path is traversed.
        '''
        final_heading = heading
        start_x, start_y = start_tuple  # type: ignore
        end_x, end_y = end_tuple
        path = []
        path.append((start_x, start_y))
        
        while start_x != end_x or start_y != end_y:
            if start_x + 1 < end_x:
                start_x += 1
                path.append((start_x, start_y))
                if final_heading != "E":  
                    final_heading = "E"
            if start_x -1 > end_x:
                start_x -= 1
                path.append((start_x, start_y))
                if final_heading != "W": 
                    final_heading = "W"
            if start_y +1< end_y:
                start_y += 1
                path.append((start_x, start_y))
                if final_heading != "N": 
                    final_heading = "N"
            if start_y -1> end_y:
                start_y -= 1
                path.append((start_x, start_y))
                if final_heading != "S":  
                    final_heading = "S"
        path.append((start_x, start_y))
        return path, final_heading # type: ignore
