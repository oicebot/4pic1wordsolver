#!/usr/bin/python2
# -*- coding:utf-8 -*-

required = 'dictionary'
number = 3

print u'4Pic1Word作弊器 v1.1 by Oicebot @Guokr.com '
print ' '

while True:
    print u'请输入题中所给字母，不区分大小写，退出请直接回车：',
    required = str(raw_input()).lower()
    if len(required) < 1:
        print u'完毕，感谢使用。'
        break
    if not required.isalpha():
        print u'输入错误，请重新输入！'
        continue

    print u'请输入目标单词的长度（3-10)：',
    try:
        number = int(input())
    except:
        print u'输入错误，请重新输入！'
        continue
    if number < 3:
        number = 3
    print u'--------'
    print u'使用字母来自：',required,'   ',u'搜索单词长度：',number
    print ' '
    
    if number < 5:
        smldict = open("smallwords.txt","r")
        word3 = smldict.readline().strip().split(",")
        word4 = smldict.readline().strip().split(",")
        smldict.close()
        if number == 3:
            dicts = word3
        elif number == 4:
            dicts = word4
            
        print u'推荐单词：',

        line_len = 0
        for words in dicts:
            words=words.lower()
            if len(words) == number:
                if all(a in required for a in words):
                    if all(words.count(a) <= required.count(a) for a in words):
                        line_len += 1
                        print words,
                        if line_len % 8 == 0:
                            print ' '
                
        print ' '
        print ' '
    with open("dictionary.txt","r") as dictionary:
        line_len = 0
        for line in dictionary:
            result = line.strip()
            if len(result) == number:
                if all(a in required for a in result):
                    if all(result.count(a) <= required.count(a) for a in result):
                        line_len += 1
                        print result,
                        if line_len % 8 == 0:
                            print ' '
        print ' '
        print '--------'
                    
