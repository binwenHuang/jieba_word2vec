# -*- coding: utf-8 -*-
import jieba.analyse
import codecs

f = codecs.open('鬼吹灯.txt','r',encoding='utf8')
target = codecs.open("guichuideng.txt",'w',encoding='utf8')

print('open files')
line_num  = 1
line = f.readline()

#循环遍历每一行，对其进行分词
while line:
    print('-----procesing',line_num,'--------')
    line_seg = " ".join(jieba.cut(line))
    target.writelines(line_seg)
    line_num = line_num + 1
    line = f.readline()

f.close()
target.close()
exit()
