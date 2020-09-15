import memory_profiler
import argparse
from main import _main

@profile
def my_func(args):
    _main(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='text similarity')

    parser.add_argument('--origText_path', type=str, help='path to the original text',
                        default='./data/sim_/orig.txt')
    parser.add_argument('--testText_path', type=str, help='path to the text to be test',
                        default='./data/sim_/orig_0.8_dis_15.txt')
    args = parser.parse_args()
    my_func(args)