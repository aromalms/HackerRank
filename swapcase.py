#swapcase
def swap_case(s):
    new=''
    for i in s:
        if i.isupper():
            i=i.lower()
            new=new+i
        else:
            i=i.upper()
            new=new+i
    return new

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)