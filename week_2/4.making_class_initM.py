import os
import csv
import pprint


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
        return data

    def merge_list(self):
        result = [sum(x) for x in self.data]
        # result = []
        # for x in self.data:
        #     x = sum(x)
        #     result.append(x)
        return result


file_path = "C:\\Users\\윤수\\Desktop\\Nyungsu\\코딩\\AI_Basic_coaching_study\\week_2"
read_csv = ReadCSV(file_path)
read_csv.read_file()
pprint.pprint(read_csv.read_file())
print(read_csv.merge_list())


