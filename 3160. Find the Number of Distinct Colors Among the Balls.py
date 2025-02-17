from collections import Counter

class Solution:
    def queryResults(self, max_value: int, operations: list[list[int]]) -> list[int]:
        result = []
        ball_color_map = {}  
        color_count = Counter()  

        for ball_id, new_color in operations:
            if ball_id in ball_color_map:
                previous_color = ball_color_map[ball_id]
                color_count[previous_color] -= 1
                if color_count[previous_color] == 0:
                    del color_count[previous_color]  

            ball_color_map[ball_id] = new_color
            color_count[new_color] += 1

            result.append(len(color_count))

        return result
