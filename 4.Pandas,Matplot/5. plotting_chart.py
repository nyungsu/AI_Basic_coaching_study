import matplotlib.pyplot as plt

names = ['group_a','group_b','group_c']
values = [1,10,100]

plt.figure(figsize=(9,3))       # 창의 크기

plt.subplot(1,3,1)
plt.bar(names,values)

plt.subplot(1,3,2)
plt.scatter(names,values)

plt.subplot(1,3,3)
plt.plot(names,values)

plt.show()

# 그래프 종류
# https://medium.com/@peteryun/python-matplotlib-%EA%B8%B0%EB%B3%B8-6e23e5fd2f16
# 참고