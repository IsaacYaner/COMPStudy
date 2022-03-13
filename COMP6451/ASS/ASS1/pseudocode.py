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

x1 = 480
N1 = DDFE0E8D462AF661F81DB36589C39882DC0F2330785B5D80CD34F2F520AD618F
x2 = 250
N2 = 4FB1D4840AC542177AB2F8D8F2D2D988CC2C2CD42CCB7F7D0D19148508E82548



