"""
6 kyu
https://www.codewars.com/kata/53907ac3cd51b69f790006c5/train/python
"""
#In this kata, you should calculate type of triangle with three given sides a, b and c (given in any order).
#If all angles are less than 90°, this triangle is acute and function should return 1.
#If one angle is strictly 90°, this triangle is right and function should return 2.
#If one angle more than 90°, this triangle is obtuse and function should return 3.
#If three sides cannot form triangle, or one angle is 180° (which turns triangle into segment) - function should return 0.
#Input parameters are sides of given triangle. All input values are non-negative floating point or integer numbers (or both).

# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    longest = max(a,b,c) #O(3)
    if a + b + c <= longest * 2: #O(1)
        return 0 #O(1)
    elif ((a**2)+(b**2)+(c**2))-(longest**2) == (longest**2): #O(1)
        return 2 #O(1)
    elif (2 * (longest ** 2)) < ((a**2)+(b**2)+(c**2)): #O(1)
        return 1 #O(1)
    else:
        return 3 #O(1)
    
#O(1) / function is Constant

print(triangle_type(2, 4, 6)) # return 0 (Not triangle)
print(triangle_type(8, 5, 7)) # return 1 (Acute, angles are approx. 82°, 38° and 60°)
print(triangle_type(3, 4, 5)) # return 2 (Right, angles are approx. 37°, 53° and exactly 90°)
print(triangle_type(7, 12, 8)) # return 3 (Obtuse, angles are approx. 34°, 106° and 40°)