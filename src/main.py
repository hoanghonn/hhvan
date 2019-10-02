from helper import *
import re
import pprint
import os
import json
import sys

vndict = {
    '1': '../data/vd11k.txt',
    '2': '../data/vd22k.txt',
    '3': '../data/vd39k.txt',
    '4': '../data/vd74k.txt'
}

def main():
    if(len(sys.argv) == 4):
        script_dir = os.path.dirname(__file__)
        rel_path = "../data/vd74k.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        content = read_file(abs_file_path)
        
        #create corresponding regex for each vans
        regex_dict = create_regex(sys.argv[3])

        for van in regex_dict:
            regex = regex_dict[van]
            r = re.compile(regex)
            res = list(filter(r.match, content)) 
            if res:
                print('Van = {:s}'.format(van))
                print('--------')
                for a,b,c in zip(res[::3],res[1::3],res[2::3]):
                    print('{:<30} {:<30} {:<}'.format(a,b,c))
                print('-----------------------------------------')

if __name__ == '__main__':
    main()