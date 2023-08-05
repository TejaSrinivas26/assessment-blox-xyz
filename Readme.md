Note:
● Question 1 is mandatory. Attempt any two questions from each section A and B.
● You can choose any programming language of your choice.
● You can cite any standard algorithm as a part of your solution and need not provide complete
code for the same but provide a clear lib interface with parameters and return values along
with a short note explaining what the method is supposed to do without actual
implementation.
● We expect you to provide gists in github or a github project - which compiles and runs.
● For any problem in section A, provide worst case and average case time and space
complexity.
1. Mandatory : Elaborate what your internship or academic projects were?
○ What did the system do?
○ What other systems have you seen in the wild like that?
○ How do you approach the development problem?
○ What were interesting aspects where you copied code from Stack Overflow?
○ What did you learn from some very specific copy paste? Mention explicitly
some of them.
Section A:
1. You are given cartesian coordinates of n factories in a plane producing some items
that need to be stored in a warehouse.
a. A transport truck begins its journey from the warehouse and it can travel
along any horizontal or vertical line. After collecting items from a factory, the
truck needs to return to the warehouse and deposit the items before visiting
another factory. Find the strategic location of the warehouse such that the
total distance truck needs to travel in order to collect items from all the
factories is minimised.
b. Think of the plane as a grid (with m x m cells) where a factory or warehouse
will be a cell. The truck can again travel from one cell to another adjacent cell
vertically or horizontally except it can’t travel outside the grid boundary.
Additionally certain cells represent no trespass area where the truck can’t
pass through. Find the optimum solution in this setup again minimising total
distance travelled by the truck.
2. You need to implement a session id generator for a very large hypothetical system
handling millions of users concurrently. You need to assign a unique session id which
is a 32 bit integer. Each new user needs to be assigned a unique id not assigned to
any active user. When a user session expires, the same id can be reused.
The problem is we have to deploy the solution on a small system with very less
memory. How can you efficiently design a solution such that it generates and
relinquishes uniques ids minimises the memory footprint of your code. You need to
implement two methods, one should provide a unique session id and the other
should release an active id making it available for reuse.
3. Recall the definition of a convex point set [1] in two dimensions. A half convex point
set is a special case where the point set is convex consisting of at most two
monotonic sequences. A monotonic sequence is a set of points such that
coordinates of the points are increasing/decreasing along both the axes. Note that
coordinate values might increase along one axis and decrease along another one.
A unit distance pair is a pair of two points iff the distance between both the points is
exactly one. Implement the code to compute all the unit distance pairs in a given
half convex point set. Argue an upper bound on the number of such pairs.
a. Input: A list of tuples where each tuple indicates a point with both coordinate
values.
b. Output: A list of pairs of tuples with unit distance.
Section B:
1. Write a function to parse any valid json string into a corresponding Object, List, or
Map object. Note that the integer and floating point should be arbitrary precision.
2. There is an API that one must call to get data. The trouble is it will not let you cross
the limit of call - say 15 calls per minute. If you cross the limit, the system penalises
you by one additional minute of penalty where you can not make any call. Here is
how the API looks like: function string call_me(string input).
Propose a solution by which:
1. You would be able to use the API within the safe limit.
2. What happens if you are supposed to call the API 20 times per minute? Is
there any way to accomplish this?
3. If you were the API designer, what would you do to implement this
behaviour?
3. Banking works by transferring money from account A to account B. Most of the time
account A is in one bank while account B is another bank. Implement the code to
transfer money. Remember, payee's code runs on a different computer than that of
the receiver's code.
1. What are the issues in such a system?
2. What can we do to mitigate some of the issues ?
3. Write the fixing yourself to demonstrate the mitigations.
References:
[1] https://en.wikipedia.org/wiki/Convex_set
[2] https://drive.google.com/file/d/1ShCe6pXQzDlbbQ-adfmAsCDPltEj-zne/view?usp=sharing
