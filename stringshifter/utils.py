
def shift_string(s,n):
    mod=n%26 # since shifts are circular and alphabets only contain 26 letters,
    ascii_a = ord('a') #reference pointer to how much distance between char and a
    #algorithm
    # Find distance from 'a'
    # add shift
    # convert back to valid ascii level using %26
    #convert to char
    #append
    return array_to_str([chr((ord(char) - ascii_a + mod) % 26 + ascii_a) for char in s.lower()])


def array_to_str(my_list):
    string = str(my_list.pop(0))
    while my_list:
        string += str(my_list.pop(0))
    return string

def check_num(n):
    '''
    Check if number is int
    :param n:
    :return:
    '''
    if type(n) is not int:
        raise ValueError("Shift should be integer")

def check_string_validity(s):
    '''
    Check if the string is valid to be processed
    :param s: string
    :return: void
    '''
    if get_len(s)<1: # if string is empty throw
        raise ValueError("Cannot supply empty string")
    try:
        a= s.encode("ascii") #if char cannot be converted to ascii throw
        if not a.isalpha(): # if char is not valid alphabet throw (could have also iterated over each char and checked 97<=ord(c)<=122)
            raise ValueError("Only valid english charcters allowed in input")

    except:
        raise ValueError("Only valid english characters allowed in input")

def get_len(s):
    '''
    My solution for finding the length of an iterable
    :param s: iterable
    :return: length of iterable
    '''
    q=0
    for i in s:
        q+=1
    return q
def map_case(s):
    '''
    Maps the case of the string to a bool array
    :param s: string
    :return: array of case True for upper False for lower
    '''
    return [True if x.isupper() else False for x in s ]

def convert_to_input_case(s,case_map):
    j=[0]*get_len(s)
    for i,q in enumerate(s):
        if case_map[i]:
            j[i]=q.upper()
        else:
            j[i] = q
    return array_to_str(j)

def join_string(a,b):
    len_a = get_len(a)
    len_b =  get_len(b)
    s = len_a+len_b
    l = [0]*(s)
    for i in range(0,s):
        if i<len_a:
            l[i]= a[i]
        else:
            k = abs(len_a-i)
            l[i]=b[k]
    return array_to_str(l)

def check_divisibility(s,n):
    if get_len(s)%n is not 0:
        raise Exception("S should be divisible by 3")

def find_index(s,p,start):
    try:
        return s.index(p,start)
    except ValueError as err:
        return -1

def replace_in_string(a,b,p_a,p_b,l_a,l_b):
    a_len = get_len(a)
    b_len = get_len(b)
    pa_len = get_len(p_a)
    pb_len= get_len(p_b)
    tot_len = a_len+b_len
    a_replaced = 0
    b_replaced = 0
    l=[0]*tot_len
    for i in range(0,tot_len):
        if i< a_len:
            replace_left= i in l_a
            if replace_left:
                l[i] = p_a[a_replaced]
                a_replaced+=1
                if a_replaced==pa_len:
                    a_replaced=0
            else:
                l[i] = a[i]
        else:
            k = abs(a_len - i)
            replace_right=k in l_b
            if replace_right:
                l[i]=p_b[b_replaced]
                b_replaced+=1
                if b_replaced==pb_len:
                    b_replaced=0
            else:
                l[i]=b[k]
    return array_to_str(l)

def replace_for_non_contigous(a,b,p_a,p_b,l_a,l_b):
    a_n= a
    b_n=b
    for i,j in zip(l_a,l_b):
        a_n=_r(a_n,p_a,i)
        b_n = _r(b_n,p_b,j)
    return join_string(a_n,b_n)

def _r(a,b,r):
    j = list(a)
    q=0
    for i in range(get_len(j)):
        if i in r:
            j[i]=b[q]
            q+=1
    return array_to_str(j)

def generate_power_set(set,set_size):
    x = get_len(set)
    sets = []
    for i in range(1<<x):
        sets.append([set[j] for j in range(x) if (i&(1<<j))])
    return [s for s in sets if get_len(s)==set_size]



if __name__=="__main__":
   # print(join_string("XXXXXXAC","DEFL"))
    #print(generate_power_set(range(1,5),3))
    #print(_r("ABCDE","QQQ",[0,1,2]))
    print()
