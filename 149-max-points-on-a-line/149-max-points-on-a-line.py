class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # A unique line can be created by choosing two points
        # A line can be represented using two numbers m,b (mx+b)
        
        # Base cases: 1 or 2 points in the array
        if len(points) <= 2:
            return len(points)
        
        # Key = "m,b" (for horizontal or oblique lines) or "vX" (for vertical lines)
        # Value = array of x-values (y-values for vertical lines)
        lines = {}
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                # p1 is the first value on the x-axis
                p1, p2 = (points[i], points[j]) if (points[i][0] < points[j][0]) else (points[j], points[i])
                
                # Vertical lines
                if p1[0] == p2[0]:
                    vX = f"v{p1[0]}"
                    if vX in lines:
                        if p1[1] not in lines[vX]:
                            lines[vX].append(p1[1])
                        if p2[1] not in lines[f"v{p1[0]}"]:
                            lines[vX].append(p2[1])
                    else:
                        lines[vX] = [p1[1], p2[1]]
                    continue
                    
                # Horizontal and Obliques lines
                m = (p2[1] - p1[1]) / (p2[0] - p1[0])
                b = p1[1] - (p1[0] * m)
                mb = f"{m},{b}"
                
                if mb in lines:
                    if p1[0] not in lines[mb]:
                        lines[mb].append(p1[0])
                    if p2[0] not in lines[mb]:
                        lines[mb].append(p2[0])
                else:
                    lines[mb] = [p1[0], p2[0]]
              
        # Find max len(x-vals) in lines **Can be optimized (put into above)**
        maxPoints = 0
        for lSym in lines.keys():
            if maxPoints < len(lines[lSym]):
                maxPoints = len(lines[lSym])
           
        return maxPoints