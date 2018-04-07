def int_to_poly(n):
    pol = []
    while (n > 0):
        pol.append(n % 2)
        n = n // 2
    return pol

def poly_to_int(p):
    res = 0
    for i in range(0, len(p)):
        res += pow(2, i) * p[i]
    return res

def diff_poly(p1, p2):
    ans = []
    if (len(p2) >= len(p1)):
        for i in range(0, len(p1)):
            ans.append(p1[i] - p2[i])
        for j in range(0, len(p2) - len(p1)):
            ans.append(-1 * p2[len(p1) + j])
    else:
        for i in range(0, len(p2)):
            ans.append(p1[i] - p2[i])
        for j in range(0, len(p1) - len(p2)):
            ans.append(p1[len(p2) + j])
    last = ans.pop()
    while last == 0 and len(ans) > 0:
        last = ans.pop()
    ans.append(last)
    return ans
        
def mult_poly(p1, p2):
    ans = [0] * (len(p1) + len(p2) - 1)
    
    for i in range(0, len(p1)):
        for j in range(0, len(p2)):
            ans[i + j] += p1[i] * p2[j]
    
    ans = list(map(lambda x: x % 2, ans))
    while ans.pop() == 0:
        pass
    ans.append(1)
    return ans            

#Assumes that len(p1) - 1 = last significative digit
def mod_poly(p1, pmod): 
    while (len(p1) >= len(pmod)):
        diff = len(p1) - len(pmod)
        paux = []
        for i in range(0, diff):
            paux.append(0)
        paux.append(1)
        paux = mult_poly(paux, pmod)
        p1 = diff_poly(p1, paux)
        p1 = list(map(lambda x: x % 2, p1))
    return p1
  
def mult8bits(bit1, bit2):
    print("{} convertido para polinomio".format(hex(bit1)))
    p1 = int_to_poly(bit1)
    print(p1)
    print("{} convertido para polinomio".format(hex(bit2)))
    p2 = int_to_poly(bit2)
    print(p2)
    print("Multiplicacao de polinomios")
    ans = mult_poly(p1, p2)
    print(ans)
    print("Modulo 0x11B")
    ans = mod_poly(ans, int_to_poly(0x11B))
    print(ans)
    print("Converte em numero")
    return poly_to_int(ans)

#calcula inversa pmod
def inversemodpmod(bit1, bitmod):
    p1 = int_to_poly(bit1)
    pmod = int_to_poly(bitmod)
    paux = p1
    while poly_to_int(paux) != 1:
        plast = paux
        paux = mult_poly(p1, paux)
        paux = mod_poly(paux, pmod)
    return plast
