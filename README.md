# Notes

### Day 7 part 1
Got stuck because I tried to solve it doing a single linear scan on the input.  
Needed to look on Reddit for help.  

### Day 8
Learned to use  
``
2DArray = [ [ -1 for j in range(COL) ] for i in range(ROW) ]  
``  
over  
``
2DArray = [ [ -1 ] * COL ] * ROW
``  

### Day 11
Learned how to get the lcm of all elements of a list  
``
lcmOfList = lcm(*List)
``  
Couldn't figure out the lcm trick on my own for part 2.  
Found the hint on Reddit. 

### Day 12  
BFS  

### Day 13  
Learned ``json.loads(x)``  
Got stuck on the sorting but got a GENIUS hint from reddit that sorting is not necessary.  
  
### Day 14
Learned ``zip()``

### Day 15  
Found a really good stack overflow post for basic regex  
https://stackoverflow.com/questions/15814592/how-do-i-include-negative-decimal-numbers-in-this-regular-expression  
Part 2 runs in ~38 seconds  