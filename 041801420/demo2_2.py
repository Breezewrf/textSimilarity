# -*- coding:utf-8 -*-
# 同demo2
# https://blog.csdn.net/qq_33689414/article/details/89516331

import jieba
from gensim import corpora, models, similarities


def analyse(base_data, target_data):
    # 1.将base_data中的数据进行遍历后分词
    base_data = [base_data, " "]
    # print(base_data[0])
    l_cut = jieba.lcut

    base_items = [[i for i in l_cut(item)] for item in base_data]
    # print(base_items[0])

    # 2.生成词典
    dictionary = corpora.Dictionary(base_items)
    # 3.通过doc2bow稀疏向量生成语料库
    doctobow = dictionary.doc2bow
    corpus = [doctobow(item) for item in base_items]
    # 4.通过TF模型算法，计算出tf值
    tf = models.TfidfModel(corpus)
    # 5.通过token2id得到特征数（字典里面的键的个数）
    num_features = len(dictionary.token2id.keys())
    # 6.计算稀疏矩阵相似度，建立一个索引
    index = similarities.MatrixSimilarity(tf[corpus], num_features=num_features)

    # 7.处理测试数据

    test_words = [word for word in jieba.cut(target_data)]
    # print(test_words)

    # 8.新的稀疏向量
    new_vec = dictionary.doc2bow(test_words)
    # 9.算出相似度
    sims = index[tf[new_vec]]
    # print(list(sims)[0])
    return list(sims)[0]
