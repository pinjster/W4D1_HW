"""
6 kyu
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).
#Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
    total = 0 #O(1)
    if number >= 3: #O(1)
        for n in range(1 , (number // 3) + 1): #O(n) / Linear as it is determined by var number inside range
            total += 3 * n #O(1)
        if number % 3 == 0: #O(1)
            total -= 3 * (number // 3) #O(1)
    if number >= 5: #O(1)
        for n in range(1 , (number // 5) + 1): #O(n) / Linear as it is determined by var number inside range
            total += 5 * n #O(1)
        if number % 5 == 0: #O(1)
            total -= 5 * (number // 5) #O(1)
    if number >= 15: #O(1)
        for n in range(1 , (number // 15) + 1): #O(n) / Linear as it is determined by var number inside range
            total -= 15 * n #O(1)
        if number % 15 == 0: #O(1)
            total += 15 * (number // 15) #O(1)
    return total #O(1)

#O(3n) -> #O(n) / function is linear

print(solution(4))
print(solution(6))
print(solution(16))
print(solution(3))
print(solution(5))
print(solution(45))
print(solution(0))
print(solution(-1))
print(solution(10))
print(solution(20))
print(solution(200))
