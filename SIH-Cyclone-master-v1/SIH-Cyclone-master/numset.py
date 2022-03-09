def numset():     
    s = 0
    for i in range(0, 23):
        s = s+100
        x = s + 30
        x = str(x)

        d = str(s)
        
        print(d.zfill(4))
        print(x.zfill(4))

numset()