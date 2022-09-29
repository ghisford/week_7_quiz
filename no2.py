#2. The snail climbs up 7 feet each day and slips back 2 feet each night. 
# How many days will it take the snail to get out of a well with the given 
# depth?. Using python, write a function to solve this problem. Sample Input: 
# 31 Sample Output: 6

def snail(depth:int):
    days = 0
    steps = 0
    while True:
        steps += 7
        steps -= 2
        if steps >= depth:
            return days
        days +=1

print(snail(31))