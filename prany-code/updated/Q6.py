# 6.How do you determine if a string is a palindrome?

def check_palindrom(s):
    reverse_st=s[::-1]
    if s==reverse_st:
        return f'{s} is palindrom string'
    else:
        return f"{s} is not palindrom"


if __name__=='__main__':
    s=input('enter string for check palindrom ')
    print(check_palindrom(s))
