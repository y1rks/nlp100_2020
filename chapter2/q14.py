'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
'''
import sys

lineNum = int(sys.argv[1]) if len(sys.argv) <= 2 else exit('Invalid args number')

with open('hightemp.txt') as f:
  text = f.readlines()
  for i in range(len(text)):
    if i >= lineNum:
      break

    print(text[i], end='')
