def first_non_repeting_char(charss):
    char_cnt={}
    for ch in charss:
        print("--ch--", ch)
        char_cnt[ch]=char_cnt.get(ch,0)+1
    print("ch-->",char_cnt)
    for s in char_cnt:
        if char_cnt[s]==1:
            return s
    return None

print("non-->",first_non_repeting_char('anjali'))