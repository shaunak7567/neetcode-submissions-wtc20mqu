class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)]
        stack =[]
        
        for p,s in sorted(pair)[::-1]: # Reverse sorted order
            stack.append((target-p) / s)
            if len(stack) >=2 and stack[-1] <= stack[-2]: # If second car reaches target before first car, that means they will collide 
                stack.pop()
        return len(stack)
        
            


