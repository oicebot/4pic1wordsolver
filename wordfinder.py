#!/usr/bin/python3
# -*- coding:utf-8 -*-

required = 'dictionary'
number = 3

print('4Pic1Word作弊器 v1.0 by Oicebot @Guokr.com ',end='\n')

while True:
    print('请输入题中所给字母，不区分大小写，退出请直接回车：',end='')
    required = input().lower()
    if len(required) < 1:
        print('完毕，感谢使用。')
        break
    if not required.isalpha():
        print('输入错误，请重新输入！')
        continue

    print('请输入目标单词的长度（3-10)：',end='')
    try:
        number = int(input())
    except:
        print('输入错误，请重新输入！')
        continue
    if number < 3:
        number = 3
    print('--------')
    print('使用字母来自：',required,'   ','搜索单词长度：',number)
    print(' ')
    
    with open("dictionary.txt","r") as dictionary:
        line_len = 0
        for line in dictionary:
            result = line.strip()
            if len(result) == number:
                if all(a in required for a in result):
                    if all(result.count(a) <= required.count(a) for a in result):
                        line_len += 1
                        print(result,end='  ')
                        if line_len % 8 == 0:
                            print(' ')
        print(' ')
        print('--------')
                    
