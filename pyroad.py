import os
import  datetime

#現行ディレクトリ以下のファイルをすべて取得する
#現在のディレクトリの中のディレクトリの中身を含める
def allFileListGet():
    path = '.'      # '.'は現在ディレクトリの意味
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list

def pyFileListGet(allFileList):
    pyFileList = []
    for file_name in allFileList:
        if file_name    [-3:] == '.py':    # .pyで終わるファイルのみ取得
            pyFileList.append(file_name)

    return pyFileList

def returnLines(pyList):    #.pyファイルの行数をすべて足す
    line_sum = 0
    for file_name in pyList:
        lines_count = sum(1 for line in open(f'{file_name}', 'r', encoding="utf-8_sig"))
        line_sum += lines_count

    return line_sum

#python pyroad.pyなどと実行した時に、実行結果を    pyroad.txtに保存
# 行数、年、月、時、分、秒の順番で書き込む
def fileWrite(date):
    f = open('pyroad.txt', 'a')
    now = datetime.datetime.now()
    f.write(f'{date},{now.year},{now.month},{now.day},{now.hour},{now.minute},{now.second}\n')
    f.close()

pyroadCount = sum(1 for line in open('pyroad.py', 'r', encoding="utf-8_sig"))  #pyroad.pyの行数は除外
#現在ディレクトリでpyroad.pyを除いたpyファイルの行数を取得

allLines =  returnLines(pyFileListGet(allFileListGet())) - pyroadCount

#1000行未満は二等兵。1000行以上2000行未満は一等兵という順
rankList = ['二等兵', '一等兵', '上等兵', '伍長', '軍曹', '准尉', '少尉', '中尉', '大尉','少佐', '中佐', '大佐', '准将', '少将', '中将', '大将', '元帥', '大総統', '現人神', '創造神']
levelLinesList = [1000,2000, 3000,4000,5000,6000,7000,8000,9000,10000,12000,14000,16000,18000,20000,25000,30000,50000,75000,100000,200000]

if allLines < levelLinesList[0]:    # 1000行未満の場合
    print(f'{allLines}行Pythonを書いているぞ！')
    print(f'お前は{rankList[0]}でまだ新米パイソニスタだ。\n書け！書けば分かる！')
    print('ごちゃごちゃ考えるな！1行でもコードを書け！')
elif allLines > levelLinesList[-1] - 1: #5000行以上の場合
    print(f'{allLines}行もPythonを書いているとは...')
    print(f'あなた様は{rankList[-1]}です。')
    print('その調子で頑張ってくさい。')
else:       #上の2つ以外の場合
    for i, _ in enumerate(levelLinesList):      #小さいほうから総当たりの方法
        if allLines > levelLinesList[i] - 1 and allLines < levelLinesList[i+1]:
            print(f'{allLines}行もPythonを書いているぞ！')
            print(f'お前は{rankList[i+1]}パイソニスタだ！')
            print('ごちゃごちゃ考えるな。１行でもコードを書け！')
            break

#  データの書き込み。いつ何行書いていたのか記録をするため。
fileWrite(allLines)
