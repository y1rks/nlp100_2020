'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
'''

import q20

text = q20.getBritishText()

for line in text.split('\n'):
  if 'Category' in line:
    print(line)