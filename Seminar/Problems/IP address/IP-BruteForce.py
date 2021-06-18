st = input()
l=len(st)
if l>=4 and l<=12:
    for i in range(1,4):
        if l-i<3:
            break
        if int(st[0:i])<=255:
            for j in range(i+1,i+4):
                if l-j<2:
                    break
                if int(st[i:j])<=255:
                    for x in range(j+1,j+4):
                        if l-x<1:
                            break
                        if (int(st[j:x])<=255):
                            if (int(st[x:])<=255):
                                a = [st[0:i],st[i:j],st[j:x],st[x:]]
                                check = True
                                for k in a:
                                    if len(k)>1 and k[0]=='0':
                                        check=False
                                        break
                                if check:
                                    print(''.join((st[0:i],'.',st[i:j],'.',st[j:x],'.',st[x:])))
else:
    print(False)
    


