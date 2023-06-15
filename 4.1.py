'''def strcounter(s): # O ( N*M)
    for sym in set(s) :
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('adcnra')

def strcounter(s): # O (N**2)
    for sym in s :
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)
strcounter('adcnra')'''

def strcounter(s):#O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1

print("Излачлоаи")


