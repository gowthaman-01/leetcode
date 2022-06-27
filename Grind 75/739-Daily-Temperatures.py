def dailyTemperatures(temperatures):
    stack, output = [], [0 for j in range(len(temperatures))]
    for i, temperature in enumerate(temperatures):
        while stack:
            if temperature > stack[-1][1]:
                top = stack.pop()
                output[top[0]] = i - top[0]
            else:
                break
        stack.append((i, temperature))
    return output
