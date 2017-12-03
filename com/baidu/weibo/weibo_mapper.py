# -*- coding: utf-8 -*-
import os
import sys
import json
sysin = sys.stdin
sysout = sys.stdout
DATA_DIR = os.path.join(os.path.expanduser("~"), "data")
#DATA_URL = "/".join(["http://cp01-yuanfang-01.epc.baidu.com:8080", "data"])
def get_config_data():
    fp = open(DATA_DIR,"wr")
    line_list= []
    for line in fp.readline():
        line_list.append(line)
    return line_list
if __name__ == '__main__':
    for line  in sysin:
        if line is not None and len(line) >3:
            try:
                line_hdfs_json = json.loads(line,encoding='utf-8')
                for word in get_config_data():
                    if(word in str(line_hdfs_json)):
                        print '%s%s%d' % (word, '\t', 1)
            except Exception as e:
                continue





