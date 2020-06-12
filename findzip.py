# 郵便番号検索
import sys

 # コマンドライン引数を確認 --- (*1)
if len(sys.argv) <= 1:
     print("以下のように入力してください")
     print("python findzip.py (住所)")
     sys.exit()
addr = sys.argv[1].strip()

 # CSVファイルを開く --- (*2)
fp = open("KEN_ALL.CSV", "rt", encoding="shift_jis")

 # 一行ずつ読んで住所の一致を調べる --- (*3)
for line in fp:
     line = line.replace(' ', '')
     line = line.replace('"', '')
     cells = line.split(",")
     zipno = cells[2] # 郵便番号
     ken = cells[6] # 都道府県
     shi = cells[7] # 市区
     cho = cells[8] # 市区以下
     title = ken + shi + cho
     if title.find(addr) >= 0:
         print(zipno + ":" + title)
fp.close()
