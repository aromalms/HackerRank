#read value of 'n' and print 1,2...n without using string fun()
if __name__ == '__main__':
    n = int(input())
num=0
for i in range (1,n+1):
    if i<10:
        num=num*10+i
    elif i<100:
        num=num*100+i
    else:
        num=num*1000+i
print(num)