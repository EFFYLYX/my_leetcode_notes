def merge_sort(l):
    if len(l) == 1:
        return l
    half = len(l) //2
    l1 = merge_sort(l[0:half])
    l2 = merge_sort(l[half:])
    return merge(l1,l2)

def merge(l1,l2):
    i = 0
    j = 0
    ans = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            ans.append(l1[i])
            i+=1
        else:
            ans.append(l2[j])
            j+=1

    if i < len(l1):
        ans.extend(l1[i:])
    if j < len(l2):
        ans.extend(l2[j:])
    return ans

print(merge_sort([7,6,4,5]))
'''
4567
'''
