from platform import node


def in_order_traverse():
    pass 

def right_child(a):
    pass

def is_left_child(a):
    pass

def father(a):
    pass

b = 0

def larger_list(a):
    result = [a]
    if a == b:
        return result
    # If b occurs in the process of in_order_traverse,
    # it will terminate and return immediately.
    result.append(in_order_traverse(right_child(a)))
    if is_left_child(father(a)):
        result.append(larger_list(father(a)))
    return result
        
def decide()
nodelist = []
R = []

for i in nodelist:
    if 0 in R and 1 in R:
        decide(0)
    else:
        decide(R[0])

