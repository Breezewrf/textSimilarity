import sys
import argparse
import numpy as np
sys.path.append('C:\\Users\\Breeze\\Desktop\\soft_engi')
from demo2_2 import analyse
weight = []
value = []


def readData(textPath):
    data = []
    te = ""
    with open(textPath, "r", encoding='utf-8') as org:
        for line in org.readlines():
            te += line  # lines to line
    # 应当先除空格，再解决换行，去除除了逗号以外所有标点，最后用逗号split
    # print(te)
    te = te.replace("\n", "")
    te = te.replace(" ", "")
    ###
    te = te.replace("、", "")
    te = te.replace("：", "")
    te = te.replace("“", "")
    te = te.replace("”", "")
    te = te.replace("；", "")
    te = te.replace("。", "")
    ###

    # print(te)
    temp = te.split("。")
    for i in temp:
        data.append(i.split("，"))
    # Text = dataProcess(data)
    data = sum(data, [])
    print(data)

    return data


def analyseSim(origText, testText):
    j = 0
    size = 0
    for i in range(len(origText)):
        val = analyse(origText[j], testText[j])
        length = len(testText[j])
        weight.append(length)
        value.append(val)
        j += 1
        size += length
    return size


def main(args):

    origText_path = args.origText_path
    testText_path = args.testText_path
    origText = readData(origText_path)
    print(len(origText))
    testText = readData(testText_path)
    print(len(testText))
    # analyse
    size = analyseSim(origText, testText)
    similarity = np.vdot(weight, value)/size
    print("Final similarity:{}".format(similarity))

    out_path = "./result/"
    with open(out_path + 'res.txt', "w", encoding='utf-8') as res:
        res.write(str(similarity))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='text similarity')

    parser.add_argument('--origText_path', type=str, help='path to the original text',
                        default='./data/sim_/orig.txt')
    parser.add_argument('--testText_path', type=str, help='path to the text to be test',
                        default='./data/sim_/orig_0.8_dis_15.txt')
    args = parser.parse_args()
    main(args)