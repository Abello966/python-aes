import aes

##
def test_int_to_poly():
    assert aes.int_to_poly(0x45) == [1, 0, 1, 0, 0, 0, 1]
    assert aes.int_to_poly(0x0A) == [0, 1, 0, 1]
    assert aes.int_to_poly(0x94) == [0, 0, 1, 0, 1, 0, 0, 1]

def test_poly_to_int():
    assert aes.poly_to_int(aes.int_to_poly(0x45)) == 0x45
    assert aes.poly_to_int(aes.int_to_poly(0x0A)) == 0x0A
    assert aes.poly_to_int(aes.int_to_poly(0x94)) == 0x94

def test_diff_poly():
    pola = [1]
    polb = [1]
    assert aes.diff_poly(pola, polb) == [0]
    polc = [1, 1]
    pold = [1]
    assert aes.diff_poly(polc, pold) == [0, 1]
    assert aes.diff_poly(pold, polc) == [0, -1]
    pole = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
    polf = [0, 1, 1, 0, 1, 1, 0, 0, 0, 1]
    assert aes.diff_poly(pole, polf) == [0, 0, -1, 0, -1, 0, 0, 1]

def test_mult_poly():
    pola = aes.int_to_poly(0x45)
    polb = aes.int_to_poly(0x0A)
    polans = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1] 
    assert aes.mult_poly(pola, polb) == polans

def test_mod_poly():
    pola = [0, 1, 0, 0, 0, 1, 0, 1, 0, 1] 
    polmod = aes.int_to_poly(0x11B)
    polans = aes.int_to_poly(0x94)
    assert aes.mod_poly(pola, polmod) == polans

def test_mult8bits():
    assert aes.mult8bits(0x45, 0x0A) == 0x94


