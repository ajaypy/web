"""
https://www.dabeaz.com/coroutines/Coroutines.pdf

Generators produce data for iteration
Coroutines are consumers of data
Coroutines are not related to iteration
----------- ---------------
Generators yield values when nex() is invoked

Couroutines consume values when send() 
Coroutine needs next() or send(None) before they begin executing
"""

def grep1(pattern):

    print ("Looking for %r" % pattern)
    while True:
        line = yield()
        if pattern in line:
            print (line)

g = grep1('python')
#g.send(None)
next(g)
g.send("YYYYYY JJJJJJJ")
g.send("kkk kkk hh")
g.send("aaa python sdrfkk ")
g.close()

def countdown(N):

    print ("counting down from %r" % N)
    while N >= 0:
        new_n = (yield N)
        if new_n is not None:
            N = new_n
        else:
            N -= 1
c = countdown(5)
for n in c:
    print (n)
    if n == 5:
        c.send(3)
