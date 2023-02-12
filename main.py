import pandas as pd
import openpyxl
import numpy as np
import re

name_list = []
sheet_location = "D:\coding\goodstudy\학생 관리표.xlsx"

def print_test(day):
    location = "D:/coding/goodstudy/단어/하이퍼2000/" + str(day) + "day.txt"
    f = open(location, "r")

    print(f.readline())
    f.close()

def extract_days(str):
    pattern = "([0-9]+) - ([0-9]+)day"

    result = re.search(pattern, str)
    first_day = int(result.group(1))
    last_day = int(result.group(2))

    for i in range(first_day, last_day+1):
        print_test(i)


wb = openpyxl.load_workbook(sheet_location, data_only=True)
sheet_list = wb.sheetnames
w1 = wb[sheet_list[0]]

for i in range(1,17):
    name_list.append(w1.cell(row=i, column=2).value)

print("-" * 20)
print("로딩완료")
print("시트이름 : ", sheet_list[0])
print("-" * 20)

input_name = input("이름을 입력하세요 : ")
print("-" * 20)
if(input_name in name_list):
    name_index = name_list.index(input_name) + 1

else:
    print("입력한 이름이 존재하지 않습니다.")
    quit()

book_name = w1.cell(row=name_index, column=6).value
if book_name == None:
    print("단어시험이 없습니다.")
    quit()
else:
    test_day = w1.cell(row=name_index, column=7).value
    print(input_name + "의 오늘 단어시험 범위는",book_name,test_day + "입니다.")

extract_days(test_day)