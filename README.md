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
Found a good [stack overflow post](https://stackoverflow.com/questions/15814592/how-do-i-include-negative-decimal-numbers-in-this-regular-expression) for basic regex   
Part 2 runs in ~38 seconds and I don't think I'm capable of optimizing it more unfortunately... 

### Day 16  
Was able to get the right answer for small inputs but really struggled optimizing the DFS. I had to give up and completely look up the solution, but I learned many things.  
[Video](https://www.youtube.com/watch?v=w9Sk7lvyGZI) I used for the solution.  
In DP, because you can't memoize sets, so use bit masking to memoize them.  
Use BFS to optimize and convert an unweighted graph into a weighted graph.  
The bottom of part 2 is really clever and should be reviewed.  

### Day 17
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA "ONLY" TOOK ME A LITTLE OVER 9 HOURS BUT I SURVIVED  
Got the caching hint for part 2 from Reddit.  

### Day 19  
It's optimized enough for Part 1 to run in ~26 seconds and Part 2 to run in ~4 minutes 20 seconds.  
I will optimize it more later...