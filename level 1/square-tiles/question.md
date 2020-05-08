#  Q: We are given a tile or area x, we have to find the minimum number of square tiles with the largest area possible that we can divide it into. Return the answer as a list

**Explanation:** Lets assume we are given a tile of area=180
So the nearest possible largest square tile will be of area 169 (sides 13 each).
Now the area of tile left is 180-169=11
Now from 11, the largest possible square will be of area 9 (sides 3 each).
The area of tile left will be 11-9=2
Now, from 2 we can create the largest possible tile of area 1 (sides 1 each)
The area left will be 2-1=1
Similarly, againg we can create the largest tile of area 1.
so the output in this case will be [169,9,1,1]

To crosscheck this solution, we can add up the elements of the list, they should give us back the actual starting area i.e 180