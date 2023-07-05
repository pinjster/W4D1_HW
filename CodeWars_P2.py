"""
7 kyu
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
"""
#Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    count = 0 #O(1)
    for n in sentence: #O(n) / Linear / dependant on given length of sentence
        if n in 'aeiuo': #O(5) / constant / worst-case cycles through 5 times
            count += 1 #O(1)
    return count #O(1)

#O(n)

print(get_count("aeiou"))
print(get_count("y"))
print(get_count("bcdfghjklmnpqrstvwxz y"))
print(get_count(""))
print(get_count("abracadabra"))