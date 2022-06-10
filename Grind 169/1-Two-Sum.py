def TwoSum(array, target):
    numDict = {}
    for i, num in enumerate(array):
        if (target - num) in numDict:
            return [i, numDict[target - num]]
        numDict[num] = i
