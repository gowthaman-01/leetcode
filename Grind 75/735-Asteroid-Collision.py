class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                while stack:
                    top = stack[-1]
                    if (top > 0 and asteroid > 0) or (top < 0 and asteroid < 0) or (top < 0 and asteroid > 0):
                        stack.append(asteroid)
                        break
                    top = stack.pop()
                    if abs(top) == abs(asteroid):
                        break
                    if abs(top) > abs(asteroid):
                        asteroid = top
                    if not stack:
                        stack.append(asteroid)
                        break
        return stack
    