import sympy as sym
import numpy as np

x = sym.Symbol('x')

def func(val):  
    fun =sym.poly(x**2 + 2*x + 3)           # subs(a,b) a에 b로 바꾸는 것 => a에 b를 대입
    return fun.subs(x, val), fun            # 함수에 val 대입한 값과 함수를 리턴
                                            

def func_gradient(fun, val):
    _, function = fun(val)
    diff = sym.diff(function, x)            # diff(f,x) 함수 f를 x로 나누어줌
    return diff.subs(x,val), diff           # 도함수에 val 대입한 값과 도함수를 리턴

def gradient_descent(fun, init_point, lr_rate = 1e-2, epsilon=1e-5):
    cnt = 0
    val = init_point
    diff, _ = func_gradient(fun, init_point)
    while np.abs(diff) > epsilon:
        val = val - lr_rate*diff
        diff, _ = func_gradient(fun, val)
        cnt += 1
        
    print(f'함수 :{fun(val)[1]}, 연산횟수 : {cnt}, 최소점 : ({val},{fun(val)[0]})')

gradient_descent(fun=func,init_point=np.random.uniform(-2,2))

