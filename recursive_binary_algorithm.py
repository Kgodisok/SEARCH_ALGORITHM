# This is a searching algorithm.I gurantee that it is efficient for big websites.
#It uses a recursive function which is a function that calls itself
list = []
def created_list():
    i = 0
    while i < 9:
        list.append(i)
        i = i + 1
    return list 


def recusrive_binary_search(list, target):
    length_of_list = len(list)
    if length_of_list == 0:
        return None
    else:
        midpoint = (len(list))//2
        if target == list[midpoint]:
            return target
        else:
            if midpoint < target:
                recusrive_binary_search(list[midpoint+1:], target)
            else:
                recusrive_binary_search(list[:midpoint], target)
    
created_list()
results = recusrive_binary_search(list, 5)

def result(results):
    if results is not None:
        print("Target found at index: ", results)
    else:
        print("Target not found.")

result(results)