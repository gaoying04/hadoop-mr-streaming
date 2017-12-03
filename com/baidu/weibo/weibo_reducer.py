# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    world_dic ={}
    for line in sys.stdin:
        world,num = line.strip().split('\t')
        count =  int(num)
        world_dic[world]=world_dic.get(world,0) +count
    print(str(world_dic))

