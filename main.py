# from textSimarity import demo2_2
import jieba
from gensim import corpora, models, similarities
import argparse
import numpy as np
from textSimarity.demo2_2 import analyse
weight = []
value = []


def readData(origText_path):
    data = []
    te = ""
    with open(origText_path, "r", encoding='utf-8') as org:
        for line in org.readlines():
            # 应当先除空格，再解决换行，最后用逗号、句号split
            # line = line.replace("\n", "")
            # line = line.replace(" ", "")
            # line = line.strip("\n")
            # if line != "\n" and line != '':
            #     data.append(line)
            te += line
    # print(te)
    te = te.replace("\n", "")
    te = te.replace(" ", "")
    ###
    te = te.replace("、", "")
    te = te.replace("：", "")
    te = te.replace("“", "")
    te = te.replace("”", "")
    te = te.replace("；", "")
    # te = te.replace("，", "")
    te = te.replace("。", "")
    ###
    #return te

    print(te)
    temp = te.split("。")
    for i in temp:
        data.append(i.split("，"))
    # Text = dataProcess(data)
    data = sum(data, [])
    print(data)

    return data


def dataProcess(data):
    Text = []
    for sector in data:
        sector = sector.strip()
        for i in sector.split("。"):
            for j in i.split("，"):
                if j == '' or j == ' ':
                    continue
                Text.append(j)
    print(Text)
    return Text


def analyseSim(origText, testText):
    j = 0
    size = 0
    for i in range(len(origText)):
        val = analyse(origText[j], testText[j])
        # 试图设置模糊检测
        # cnt = -4
        # if val < 0.3:
        #     val_arr = []
        #     while val < 0.3 and cnt < 4:
        #         cnt += 1
        #         val_arr.append(analyse(origText[j], testText[j+cnt]))
        #     val = max(val_arr)
        #     j += cnt-1

        length = len(testText[j])
        weight.append(length)
        value.append(val)
        j += 1
        size += length
    return size


def main():
    origText_path = "data/sim_/orig.txt"
    testText_path = ["data/sim_/orig_0.8_mix.txt", "data/sim_/orig_0.8_del.txt",
                     "data/sim_/orig_0.8_add.txt", "data/sim_/orig_0.8_dis_15.txt"]
    origText = readData(origText_path)
    print(len(origText))
    testText = readData(testText_path[3])
    print(len(testText))
    size = analyseSim(origText, testText)
    print(np.vdot(weight, value)/size)

    parser = argparse.ArgumentParser()
    parser.add_argument("--text1", help="this is the position to the text1")
    parser.parse_args()


if __name__ == '__main__':
    main()
