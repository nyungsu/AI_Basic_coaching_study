# class People():
#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
#     def __str__(self) -> str:
#         return (f"제 이름은 {self.name}이고, 나이는{self.age}입니다.")
        
# ys = People(name='정윤수',age=26)
# # print(ys)

# class Korean(People):
#     #name,age는 부모 클래스 사용
#     #country만 받아서 씀
#     def __init__(self, name, age,country) -> None:
#         super().__init__(name, age)
#         self.country = country
        
# ys = Korean(name='윤수',age=26,country='korea')

# print(ys.name,ys.age,ys.country)
        



class Person():
    def __init__(self,name,age) -> None:
        self.name =name
        self.age = age
    def about_me(self):
        print(f"저의 이름은 {self.name}이고요, 나이는 {self.age}살 입니다.")
        
class Student(Person):
    def __init__(self, name, age,major) -> None:
        super().__init__(name, age)
        self.major = major
        
    def about_me(self):
        super().about_me()
        print(f'제 전공은 {self.major}입니다.')
        
ys = Student(name='윤수',age=26,major='E/E')

ys.about_me()