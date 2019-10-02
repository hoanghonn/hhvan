import itertools

def read_file(file):
    with open(file, encoding='utf8') as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]
    return content


def create_regex(word):
    words = word.split(" ")
    res = {}
    l = []
    for w in words:
        w_arr = w.split()
        tempList = []
        for i in range(len(w_arr)):
            vans = get_list_of_van(w) 
            tempList.extend(vans)
        l.append(tempList)
    for v in list(itertools.product(*l)):
        van = ''
        temp = ''
        for i in range(len(v)):
            van += v[i] + ' '
            if(i == len(v)-1):
                temp += ".*" + v[i] + "$"
            else: temp += ".*" + v[i] + "\s"
        res[van] = temp
    return res

def get_list_of_van(word):
    vowels = ['a','i','y','u','e','o']
    list_of_van = []
    for c in word:
        if c in vowels or ord(c) > 122:
            list_of_van.append(word[word.index(c):])
    return list_of_van




