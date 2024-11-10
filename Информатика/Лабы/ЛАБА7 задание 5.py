def f(a):
    w = a.split("/")
    p=["у", "е", "ё", "ы", "а", "о", "э", "я", "и", "ю","Е"]
    t = 5
    prav=[]
    if len(w)==3:
        for x in range(3):
            u = list(w[x])
            l = 0
            for i in u:
                if i in p:
                    l+=1
            prav.append(str(l))
    n="".join(prav)
    if n =='575':
         return "haiku",n
    else:
        return "ne haiku",n
text = input()
print(f(text))