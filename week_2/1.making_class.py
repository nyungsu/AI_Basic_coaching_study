import copy

class Score:
    def __init__(self, mid, final):
        self.__mid = mid
        self.__final = final
                                                    # private로 선언 
    @property                                       # property 꼭 공부해라 윤수야
    def mid(self):
        mid = copy.deepcopy(self.__mid)             # 데이터를 다룰 때 기존의 데이터가 훼손되지 않게 
        return mid                                  # copy 시켜서 다루는 습관을 가지자

    @property
    def final(self):
        final = copy.deepcopy(self.__final)
        return final

    def print_average(self):
        print((score.mid + score.final) / 2)


score = Score(50, 75)
score.print_average()
