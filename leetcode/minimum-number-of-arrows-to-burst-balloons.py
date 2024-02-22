class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points =  sorted(points, key=lambda x: x[1])
        arrow_x, count_arrow = points[0][1], 1

        for i in range(1, len(points)):
            if points[i][0] > arrow_x:
                count_arrow += 1
                arrow_x = points[i][1]

        return count_arrow     