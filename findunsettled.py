import pandas as pd
import os
from tkinter import filedialog
from tkinter import messagebox

list_file = []                                          #파일 목록 담을 리스트 생성
files = filedialog.askopenfilenames(initialdir="/",\
                 title = "파일을 선택 해 주세요",\
                    filetypes = (("*.xlsx","*xlsx"),("*.xls","*xls"),("*.csv","*csv")))
#files 변수에 선택 파일 경로 넣기

if files == '':
    messagebox.showwarning("경고", "파일을 추가 하세요")    #파일 선택 안했을 때 메세지 출력

print(files)    #files 리스트 값 출력

for dir in files:
    dirname,basename = os.path.splitext(dir)

print(basename)
if basename == '.xlsx' or basename == '.xls':
    df = pd.read_excel(io=dir,engine='openpyxl',skiprows=11,names=['거래일시', '금액','내용', '메모'], usecols="B,D,G,H")
else:
    df = pd.read_csv(filepath_or_buffer=dir)    

df = df.fillna("")



# 정산 금액, 인원 입력 후 미정산 인원 추려내기 
amount = int(input('정산 금액: '))
#personnel = int(input('인원: '))
str = input('인원(복사 후 붙여넣기): ')
person_list = str.split()
print(person_list)

settlement = round(amount/len(person_list))

settle_df = df.loc[df['금액']==settlement]

print(settlement)

print(settle_df['금액'].count())

for name in person_list:
    if(settle_df['내용']==name).any():
        person_list.remove(name)

print(person_list)


# #https://m.blog.naver.com/janghanui/222399697657 
# # 파일 탐색기 만들어서 찾아서 넣기