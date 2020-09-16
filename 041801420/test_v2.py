import unittest
from main import readData, analyseSim
import numpy as np
import coverage
base_path = "C:\\Users\\Breeze\\Desktop\\soft_engi\\textSimilarity\\textSimilarity\\041801420\\data\\sim_\\"


class TestForAllTextTfIdf(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("call setup……")

    @classmethod
    def tearDown(self):
        print("call teardown")

    def test_self_tfidf(self):
        print("正在载入orig.txt")
        _main("orig.txt",
              "orig.txt")

    def test_add_tfidf(self):
        print("正在载入orig.txt")
        _main("orig.txt",
              "orig_0.8_dis_10.txt")

    def test_del_tfidf(self):
        print("正在载入orig.txt")
        _main("orig.txt",
              "orig_0.8_dis_10.txt")

    def test_dis_1_tfidf(self):
        print("正在载入orig_0.8_dis_1.txt")
        _main("orig.txt",
              "orig_0.8_dis_1.txt")

    def test_dis_3_tfidf(self):
        print("正在载入orig_0.8_dis_3.txt")
        _main("orig.txt",
              "orig_0.8_dis_3.txt")

    def test_dis_7_tfidf(self):
        print("正在载入orig_0.8_dis_7.txt")
        _main("orig.txt",
              "orig_0.8_dis_7.txt")

    def test_dis_11_tfidf(self):
        print("正在载入orig_0.8_dis_10.txt")
        _main("orig.txt",
              "orig_0.8_dis_10.txt")

    def test_dis_15_tfidf(self):
        print("正在载入orig_0.8_dis_15.txt")
        _main("orig.txt",
              "orig_0.8_dis_15.txt")

    def test_dis_mix_tfidf(self):
        print("正在载入orig_0.8_mix.txt")
        _main("orig.txt",
              "orig_0.8_mix.txt")

    def test_dis_rep_tfidf(self):
        print("正在载入orig_0.8_rep.txt")
        _main("orig.txt",
              "orig_0.8_rep.txt")


def _main(origText_path, testText_path):
    _path = testText_path
    origText_path = base_path + origText_path
    testText_path = base_path + testText_path
    weight = []
    value = []
    origText = readData(origText_path)
    # print(len(origText))
    testText = readData(testText_path)
    # print(len(testText))
    # analyse
    size = analyseSim(origText, testText, weight, value)
    similarity = np.vdot(weight, value) / size
    print(("Final similarity of {} is : %.2f" % similarity).format(_path))

    out_path = "C:\\Users\\Breeze\\Desktop\\soft_engi\\textSimilarity\\textSimilarity\\041801420\\result\\"
    with open(out_path + 'res.txt', "a+", encoding='utf-8') as res:
        res.write(("%.2f"%(similarity))+'\n')
    res.close()
    return similarity


if __name__ == '__main__':
    unittest.main()
