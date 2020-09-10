# 使用jieba对汉字分词，genism相似度计算
import jieba
from gensim import corpora,models,similarities

doc0 = "我不喜欢上海"
doc1 = "上海是一个好地方"
doc2 = "北京是一个好地方"
doc3 = "上海好吃的在哪里"
doc4 = "上海好玩的在哪里"
doc5 = "上海是好地方"
doc6 = "我厌恶上海"
doc7 = "喜欢小吃"
doc_test = "我讨厌上海"
all_doc = []
all_doc.append(doc0)
all_doc.append(doc1)
all_doc.append(doc2)
all_doc.append(doc3)
all_doc.append(doc4)
all_doc.append(doc5)
all_doc.append(doc6)
all_doc.append(doc7)
all_doc_list = []

# 分词
for doc in all_doc:
    doc_list = [word for word in jieba.cut(doc)]
    all_doc_list.append(doc_list)

print(all_doc_list)

doc_test_list = [word for word in jieba.cut(doc_test)]

# 获取词袋并编号
dictionary = corpora.Dictionary(all_doc_list)
print(dictionary.token2id)

# doc2bow制作语料库
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
print(corpus)
doc_test_vec = dictionary.doc2bow(doc_test_list)

# 使用tfidf对语料库建模
tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
sim = index[tfidf[doc_test_vec]]

print(sorted(enumerate(sim), key=lambda item: -item[1]))


