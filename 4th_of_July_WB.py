#4th of July Time Complexity!
#A city is putting on a fireworks show for the 4th of July. 
#There are `n` types of fireworks, and for each type, there’s a specific amount of time it takes to launch that firework.
#The city wants to put on a show that lasts for `m` minutes.
#The function `create_show` takes a list of fireworks 
#(each represented as an integer indicating the time in minutes it takes to launch) and a total time for the show `m`.
# The function will return a list of fireworks that will fill the show’s time as evenly as possible.
import random

def create_show(fireworks, show_time):
    fireworks.sort() #O(n log(n)) / logarithmic dependant / does not alter
    show = [] #O(1)
    remaining_time = show_time #O(1)
    while remaining_time > 0 and fireworks: #O(log(n)) / logarithmic / incrementally decreases fireworks and time each cycle 
           # Select a random firework
           firework = random.choice(fireworks) #O(1) / constant / chooses 1 from list and returns it 
           if firework <= remaining_time: #O(1) 
               # Add the firework to the show
               show.append(firework) #O(1) / constant / does not need to alter list, only add at end
               remaining_time -= firework #O(1) / constant / increments time down
           else:
              # This firework is too long, remove it from consideration
              fireworks.remove(firework) #O(n) / linear / goes through list of fireworks to find specific firework and removes 
#O(n log(n)) logarithmic as it perpetually removes 1. making it dependant on how many of fireworks
    return show