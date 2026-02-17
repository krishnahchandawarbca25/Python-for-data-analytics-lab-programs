Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
myset = {10,20,30,40,}
myset.add(50)
myset
{40, 10, 50, 20, 30}
myset.update([60,70])
myset
{70, 40, 10, 50, 20, 60, 30}
myset.remove(10)
>>> myset
{70, 40, 50, 20, 60, 30}
>>> myset.discard(10)
>>> myset
{70, 40, 50, 20, 60, 30}
>>> myset.discard(20)
>>> myset
{70, 40, 50, 60, 30}
>>> myset.pop()
70
>>> myset
{40, 50, 60, 30}
>>> A = {1,2,3 4}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> A = {1,2,3,4}
>>> B = {4,5,6,7,8}
>>> A.union(B)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> A.intersection(B)
{4}
>>> A.difference(B)
{1, 2, 3}
>>> A.difference_update(B)
>>> A
{1, 2, 3}
>>> A.symmetric_difference(B)
{1, 2, 3, 4, 5, 6, 7, 8}
>>> A = {1,2,3}
>>> B = {2,3,5}
>>> A.issubset(B)
False
>>> B.issuperset(B)
True
>>> A.isdisjoint(B)
False
>>> myset.discard(30)
>>> myset
{40, 50, 60}
>>> myset.clear()
>>> myset
set()
