from functools import reduce

#lambda
f = lambda x,y : x+y
g = lambda x, : x*x

print(f(5,3))
print(g(3))

data1 = [1,2,3,4,5]
data2 = [5,4,3,2,1]
#map
a = map(g,data1)
print(list(a))

b=map(f,data1,data2)        #zip 없이   
print(list(b))              #fun 인자 수만큼 리스트 가능

#list comprehension 으로 표현 가능

#reduce
print(reduce(lambda x,y:x+y, [1,2,3,4,5]))
