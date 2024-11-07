n = str(input())
pred_n = []
F = False
setik = set()
while not(F or n == '1'):
    new_n = 0
    for i in n:
        new_n += int(i)**2
    pred_n += [n]
    leng = len(setik)
    setik.add(n)
    F = (len(setik) == leng)
    n = str(new_n)
if n != '1':
    print("Sad😞")
else:
    print("Happy☺")
    pred_n += ['1']
    ind = 0
    for i in pred_n[:len(pred_n) - 1]:
        ind += 1
        for j in range(len(i)):
            print(i[j] + '²', end = '')
            if j < len(i) - 1:
                print('+', end = '')
        print("="+pred_n[ind])