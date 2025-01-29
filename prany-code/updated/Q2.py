"""
2.Reverse the sentence
ex- I/p= I love you o/p=you love I
"""

def reverse_sentence(s):
    wl=s.split(' ')
    reverse_s=' '.join(wl[::-1])
    return reverse_s

s="I love you"
print(reverse_sentence(s))