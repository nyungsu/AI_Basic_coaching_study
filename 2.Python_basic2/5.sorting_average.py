import os
import csv
import pprint

"""
read_file 함수에서 메모리에 데이터를 올리는 방식으로 코드를 구현 했을때,
2주차 미션 5번의 출력 예시와 같이
read_file 함수를 실행하지 않은 상태에서 merge_list를 실행하면
메모리에 데이터가 없어서 에러가 뜨는 이슈가 발생하였습니다.
이를 바탕으로 init에서 메모리에 데이터를 바로 올리는 방법을 생각하였으나,
클래스가 선언 된 뒤로 계속 메모리를 차지하지 않을까 싶은 마음에 코치님께 질문드린 결과
init에서 데이터를 올리는 방법으로 하되
제너레이터를 사용하여 메모리 효율을 가져가는 방법을 선택하였습니다.
"""


class ReadCSV:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_file()              
       
# 데이터 타입 변환은 계산 단계가 아닌 입력 단에서 관리해 주는 편이 좋다고 하셔서 read_file 에서 int로 바꿔서 저장하자
    def read_file(self):
        os.chdir(file_path)          
        with open("data-01-test-score.csv", newline="\n") as f:
            temp = list(csv.reader(f))
            data = []
            for i in temp:                              #list comprehension 2중으로 하기 힘드넹
                str2int = [int(x) for x in i]
                data.append(str2int)
            data = (x for x in data)  # Generator Comprehension
        return data 

    def merge_list(self):
        result = [sum(x)/len(x) for x in self.data]
        return sorted(result)              


file_path = "C:\\Users\\윤수\\Desktop\\Nyungsu\\코딩\\AI_Basic_coaching_study\\week_2"
read_csv = ReadCSV(file_path)
print(read_csv.merge_list())







