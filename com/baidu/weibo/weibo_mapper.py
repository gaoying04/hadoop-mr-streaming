# -*- coding: utf-8 -*-
import os
import sys
import json

sysin = sys.stdin
sysout = sys.stdout
DATA_DIR = os.path.join(os.path.expanduser("~"), "data")
print(DATA_DIR)
#DATA_URL = "/".join(["http://cp01-yuanfang-01.epc.baidu.com:8080", "data"])
def get_config_data():
   fp=open(DATA_DIR,"w")
    line_list= []
    for line in fp.readline():
        line_list.append(line.strip())
    return line_list
if __name__ == '__main__':
    for line  in sys.stdin:
        hdfs_log = line.decode("uft-8")
        try:
                for word in get_config_data():
                    if(word in str(hdfs_log)):
                        #print '%s%s%d' % (word, '\t', 1)
                        sys.stdout.write('%s%s%d' % (word, '\t', 1))
                        sys.stdout.flush()
        except Exception as e:
            continue





