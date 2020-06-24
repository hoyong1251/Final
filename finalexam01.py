

def calculpi(count):
    answer=0
    if(count==1): return float(4*1)
    for x in range(1,count+1):
        if x%2==1:
            answer+=float(1/(2*x-1))
        else:
            answer-=float(1/(2*x-1))
    return float(4*answer)
num=1
print("i \tm(i)")
while 1:
    print("{0} \t {1}".format(num,round(calculpi(num),4)))
    num+=100
    if num==1001:
        break