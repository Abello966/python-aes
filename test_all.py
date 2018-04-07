import aes

##

def test_int_to_poly():
    assert aes.int_to_poly(0x45) == [0, 1, 0, 0, 0, 1, 0, 1]
    assert aes.int_to_poly(0x0A) == [0, 0, 0, 0, 1, 0, 1, 0]
    assert aes.int_to_poly(0x94) == [1, 0, 0, 1, 0, 1, 0, 0]

def test_poly_to_int():
    assert aes.poly_to_int([0, 1, 0, 0, 0, 1, 0, 1]) == 0x45
    assert aes.poly_to_int([0, 0, 0, 0, 1, 0, 1, 0]) == 0x0A
    assert aes.poly_to_int([1, 0, 0, 1, 0, 1, 0, 0]) == 0x94

def test_mult_poly():
    pola = [0, 1, 0, 0, 0, 1, 0, 1]
    polb = [0, 0, 0, 0, 1, 0, 1, 0]
    polans = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
    assert aes.mult_poly(pola, polb) == polans

def test_poly_mod():
    pola = [1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
    polmod = [1, 0, 0, 1, 0, 1, 0, 0]
    polans = [1, 0, 0, 0, 1, 1, 0, 1, 1]
    assert aes.poly_mod(pola, polmod) == polans

def test_mult8bits():
    assert aes.mult8bits(0x45, 0x0A) == 0x94


