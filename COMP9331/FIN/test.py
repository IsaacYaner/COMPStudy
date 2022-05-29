def XOR(str1, str2):    #实现模2加法
    ans = ''
    if str1[0] == '0':
        return '0', str1[1:]
    else:
        for i in range(len(str1)):
            if (str1[i] == '0' and str2[i] == '0'):
                ans = ans + '0'
            elif (str1[i] == '1' and str2[i] == '1'):
                ans = ans + '0'
            else:
                ans = ans + '1'
    return '1', ans[1:]

def div2(str1, str2):
    lenght = len(str2)
    str3 = str1 + '0'*(lenght-1)
    yus = str3[0:lenght]
    for i in range(len(str1)):         #模二除法  补位
        str4,yus = XOR(yus, str2)
        if i == len(str1)-1:
            break
        else:
            yus = yus+str3[i+lenght]
    return yus

D = '100011110'
G = '1111'
data = div2(D, G)
print(data)