"""
http://jlmartin.faculty.ku.edu/~jlmartin/courses/math105-F11/Lectures/chapter5-part1.pdf
http://jlmartin.faculty.ku.edu/~jlmartin/courses/math105-F11/Lectures/chapter5-part2.pdf

http://jlmartin.faculty.ku.edu/courses.html

An Euler Path is a path that uses every edge of a graph exactly once
Euler Path starts and ends at different vertices

An Euler circuit is a circuit that uses every edge of a graph exactly once.
Euler circuit starts and ends at same vertex.


1. Determine Existence of Euler Path
------------------------------------
For every vertex v other than the starting and ending vertices, the path P 
enters v the same number of time that it leaves v ( s times)

Therefore there are 2s edges having v as an endpoint
Therefore all vertices other than the two endpoints of P must be even vertices.

If starting point is X and ending point is Y
P leaves X one more time than it enters
P leaves Y one fewer time than it enters

The start and end points must be odd vertices

if a graph G has an Euler path, then it must have exactly two odd vertices.

2. Determine Existence of Euler Path
------------------------------------
For every vertex v each edge having v as an endpoint shows up exactly once in C.

if A graph G has an Euler Circuit, then all its vertices  must be event vertices.



Does every graph with zero odd vertices have an Euler Circuit?
Does every graph with two odd vertices have an Euler Circuit?

3. Handshaking Theorem
----------------------
In every graph , the sum of the degrees of all vertices equals twice the number 
of edges


edges = (d1 + d2 + .... + dn) / 2
so (d1 + d2 + .... + dn) must be even
so d1 , d2 , .... , dn) must have even number of odd numbers


4. Bridges
An edge ,which can make a graph disconnected on its removal 
Loops cannot be bridges

4.Fleury's Algorithm
--------------------
To find an Euler path or an Euler Circuit:

1. Make sure the graph has either 0 or 2 odd vertices
2. If there are 0 odd, start anywhere, if there are 2
odd vertices, start at one of them
3. Follow edges one at a time. If choice between bride and non-bridge
always choose the non-bridge
4. Stop when you run out of edges
"""
