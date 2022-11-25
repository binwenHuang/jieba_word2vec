# # -*- coding: utf-8 -*-
# from gensim.models import Word2Vec
# from gensim.models.word2vec import LineSentence
# import logging
#
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#
#     #word2vec第一个参数代表要训练的语料
#     #sg = 1 表示使用skip-Gram 模型进行训练
#     #size 表示特征向量的维度，默认100，大的size表示更多的训练数据，但是
#     #window表示当前词与预测词在一个句子中的最大距离是多少
#     #min_count 可以对字典做截断，词频少于min_count次数的单位会被丢弃掉
#     #workers 表示训练的并行数
#
# def main():
#     shuju = open('guichuideng.txt','rb')
#
#     model = Word2Vec(LineSentence(shuju),sg=1,vector_size=100,window=10,min_count=5,workers=15,sample=1e-3)
#
#     model.save('guichuideng.word2vec')
#
#     print('训练完成')
#
# if __name__ == '__main__':
#     main(

import cv2
cap = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    cv2.imshow("img",img)
    key = cv2.waitKey(0)
    if key==ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
