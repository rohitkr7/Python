def fib(num):
    a,b = 0, 1
    for i in range(0,num):
        yield "{}: {}".format(i+1,a)
        a,b = b, a+b

for item in fib(10):
    print(item)


# yield keyword is used to create generators
# yield basically sends the result to the calling function and saves the execution state 
# so that once the exectuion state comes back it just start executing from the state it has left earlier