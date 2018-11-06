import re
import pprint
import os

def read_file(file):
    with open(file, encoding='utf8') as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]
    return content


def create_re(word):
    words = word.split()
    res = {}
    for i in range(len(words)):
        temp_vans = [get_van(w) for w in words[i:]]
        temp_van = ''
        for v in temp_vans:
            temp_van = temp_van + '.*' + v + '\s'
        temp_van = temp_van[:-2] + '$'
        res[len(words)-i] = temp_van
    return res

def get_van(word):
    vowels = ['a','i','y','u','e','o']
    for c in word:
        if c in vowels or ord(c) > 122:
            return word[word.index(c):]


def main():

    script_dir = os.path.dirname(__file__)
    rel_path = "../data/vd74k.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    
    content = read_file(abs_file_path)
    van_dict = create_re('bia')
    
    for k in van_dict:
        r = re.compile(van_dict[k])
        res = list(filter(r.match, content)) 
        if res:
            print('Nums of van = {:d}'.format(k))
            for a,b,c in zip(res[::3],res[1::3],res[2::3]):
                print('{:<30} {:<30} {:<}'.format(a,b,c))


if __name__ == '__main__':
    main()

