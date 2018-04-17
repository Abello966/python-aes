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
    p1 = int_to_poly(bit1)
    p2 = int_to_poly(bit2)
    ans = mult_poly(p1, p2)
    ans = mod_poly(ans, int_to_poly(0x11B))
    return poly_to_int(ans)

#calculates inverse related to pmod
def inversemodpmod(bit1, bitmod):
    p1 = int_to_poly(bit1)
    pmod = int_to_poly(bitmod)
    paux = p1
    while poly_to_int(paux) != 1:
        plast = paux
        paux = mult_poly(p1, paux)
        paux = mod_poly(paux, pmod)
    return plast

def bits_to_poly(bit):
    ans = []
    while bit > 0:
        ans.append(bit % 256)
        bit = bit // 256
    return ans

def poly_to_bits(pol1):
    ans = 0
    for i in range(0, 4):
        ans += pow(256, i) * pol1[i]
    return ans

def mult_32bit_poly(p1, p2):
    ans = [0] * 7
    for i in range(0, 4):
        for j in range(0, 4):
            ans[i + j] = mult8bits(p1[i], p2[j])
    ans = list(map(lambda x: x % 256, ans))
    return ans

def mult32bits(bit1, bit2):
    pol1 = bits_to_poly(bit1)
    pol2 = bits_to_poly(bit2)
    ans = []
    #analytical formula of mod (x^4 + 1)
    c0 = mult8bits(pol1[0], pol2[0])
    c0 ^= mult8bits(pol1[1], pol2[3])
    c0 ^= mult8bits(pol1[2], pol2[2])
    c0 ^= mult8bits(pol1[3], pol2[1])
    ans.append(c0)

    c1 = mult8bits(pol1[0], pol2[1])
    c1 ^= mult8bits(pol1[1], pol2[0])
    c1 ^= mult8bits(pol1[2], pol2[3])
    c1 ^= mult8bits(pol1[3], pol2[2])
    ans.append(c1)

    c2 = mult8bits(pol1[0], pol2[2])
    c2 ^= mult8bits(pol1[1], pol2[1])
    c2 ^= mult8bits(pol1[2], pol2[0])
    c2 ^= mult8bits(pol1[3], pol2[3])
    ans.append(c2)

    c3 = mult8bits(pol1[0], pol2[3])
    c3 ^= mult8bits(pol1[1], pol2[2])
    c3 ^= mult8bits(pol1[2], pol2[1])
    c3 ^= mult8bits(pol1[3], pol2[0])
    ans.append(c3)
    return ans

def mixcolumns(bit1):
    cx = [0x02, 0x01, 0x01, 0x03]
    pol1 = bits_to_poly(bit1)
    ans = mult_32bit_poly(pol1, cx)
    ans = mult32bits(bit1, poly_to_bits(cx))
    return poly_to_bits(ans)

def mixcolumnsinverse(bit1):
    invcx = [0x0E, 0x09, 0x0D, 0x0B]
    pol1 = bits_to_poly(bit1)
    ans = mult_32bit_poly(pol1, invcx)
    ans = mult32bits(bit1, poly_to_bits(invcx))
    return poly_to_bits(ans)
