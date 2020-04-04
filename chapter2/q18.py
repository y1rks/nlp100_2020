'''
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''

import sys, csv, operator

rows = csv.reader(open('hightemp.txt'), delimiter='\t')

for row in sorted(rows, key=operator.itemgetter(2), reverse=True):
  print(row)