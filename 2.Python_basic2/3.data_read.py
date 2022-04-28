import csv
import os
import pprint


class ReadCSV:
    def __init__(self, file_path):
        self.file_path = file_path
        os.chdir(file_path)

    def read_file(self):
        with open("data-01-test-score.csv", newline="\n") as f:
            data = list(csv.reader(f))      # <_csv.reader object at 0x000001F46E29F6A0> 메모리 주소를 불러와서
                                            # pprint로 이쁘게 출력 하는 거 말고 첨 부터 이쁘게 저장은 안 되나요ㅠㅠ ?
        return data


file_path = "C:\\Users\\윤수\\Desktop\\Nyungsu\\코딩\\AI_Basic_coaching_study\\week_2"

read_csv = ReadCSV(file_path)
pprint.pprint(read_csv.read_file())
