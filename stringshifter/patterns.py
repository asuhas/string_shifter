from stringshifter.utils import get_len, replace_in_string, replace_for_non_contigous, find_index,generate_power_set

def _generate_pattern_list(string,pattern,powerset):
    seen=set()
    out=[]
    h= get_len(pattern)-1
    for s in powerset:
        for k,j in enumerate(s):
            if pattern[k]==string[j] :
                if k==h and not seen.intersection(set(s)):
                    out.append(s)
                    seen.update(s)
                continue
            else:
                break
    return out[::-1]


def non_contigious_right_replace_non_recursive(left,right,left_pattern,right_pattern):
    l_arr=[]
    r_arr=[]
    ps = generate_power_set(range(get_len(right)),get_len(right_pattern))
    valid_power_set = _generate_pattern_list(right,right_pattern,ps)
    index,offset= _get_index_offset(left,left_pattern,0)
    while index!=-1 and valid_power_set:
        l_arr.append(range(index,offset))
        r_arr.append(valid_power_set[-1])
        valid_power_set.pop()
        index, offset = _get_index_offset(left, left_pattern, index)
    replacement = replace_for_non_contigous(left,right,right_pattern,left_pattern,l_arr,r_arr)
    return replacement


def _get_index_offset(string,pattern,index):
    p = find_index(string,pattern,index)
    return p,p+get_len(pattern)

def _fill_contigious_pattern_array_rex(left, right, left_pattern, right_pattern, larr, rarr, loff, roff):
    index_left,offset_left= _get_index_offset(left,left_pattern,loff)
    index_right,offset_right = _get_index_offset(right,right_pattern,roff)
    if index_left != -1 and index_right != -1:
        larr.extend(range(index_left, offset_left))
        rarr.extend(range(index_right, offset_right))
        return _fill_contigious_pattern_array_rex(left, right, left_pattern, right_pattern, larr, rarr, offset_left, offset_right)
    else:
        return larr, rarr

def pattern_replace_recursive(left,right,left_pattern,right_pattern):
    larr,rarr = _fill_contigious_pattern_array_rex(left, right, left_pattern, right_pattern, [], [], 0, 0)
    replacement = replace_in_string(left, right, right_pattern, left_pattern, larr, rarr)
    return replacement

def pattern_replace_non_recursive(left, right, left_pattern, right_pattern):
    left_arr = []
    right_arr = []
    index_left,offset_left = _get_index_offset(left,left_pattern,0)
    index_right,offset_right= _get_index_offset(right,right_pattern,0)
    while index_left != -1 and index_right != -1:
        left_arr.extend(range(index_left, offset_left))
        right_arr.extend(range(index_right, offset_right))
        index_left, offset_left = _get_index_offset(left, left_pattern, offset_left)
        index_right, offset_right = _get_index_offset(right, right_pattern, offset_right)
    replacement = replace_in_string(left, right, right_pattern, left_pattern, left_arr, right_arr)
    return replacement


if __name__ == "__main__":
    left = "ABCDEF"
    right = "GHBXCD"
    lp = "ABC"
    rp = "BCD"
    print(non_contigious_right_replace_non_recursive(left, right, lp, rp))
    print(pattern_replace_recursive(left, right, lp, rp))
    # s="AAABBBCCC"
    # p="ABC"
    # ps = generate_power_set(range(len(s)),len(p))
    # i=_generate_pattern_list(s,p,ps)

