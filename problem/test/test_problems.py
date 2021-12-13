from ..problems import *

import numpy as np
from numpy.testing import assert_equal, assert_allclose


def test_p1():
    """
    testing p1() function
    :return:
    """
    ad1 = p1()
    assert (isinstance(ad1, set) or isinstance(ad1, list) or isinstance(ad1, tuple))
    assert (len(ad1) > 0)
    assert(set(map(str.casefold, ad1)) == {"a", "b", "e"})


def test_p2():
    """
    testing p2() function
    :return:
    """
    ad2 = p2()
    assert(isinstance(ad2, float))
    assert (np.isclose(ad2, constants.c / 500e-9, rtol=1e-3))


def test_p3():
    """
    testing p3() function
    :return:
    """
    freq_double = p3()
    assert (isinstance(freq_double, bool))
    assert (freq_double is False)


def test_p4():
    """
    testing p4() function
    :return:
    """
    speed_halves = p4()
    assert (isinstance(speed_halves, bool))
    assert (speed_halves is False)


def test_p5():
    """
    testing p5() function
    :return:
    """
    E_HeNe = p5()
    assert (isinstance(E_HeNe, float))
    assert (np.isclose(E_HeNe, 3.1391e-19, rtol=1e-3))


def test_p6():
    """
    testing p6() function
    :return:
    """
    e_doubles = p6()
    assert (isinstance(e_doubles, set) or isinstance(e_doubles, list) or isinstance(e_doubles, tuple))
    assert (len(e_doubles) > 0)
    assert (set(map(str.casefold, e_doubles)) == {"a", "c", "e", "f"})


def test_p7():
    """
    testing p6() function
    :return:
    """
    p_greenlaser = p7()
    assert (isinstance(p_greenlaser, float))
    assert (np.isclose(p_greenlaser, 3.336e-10, rtol=1e-3))


def test_p8():
    """
    testing p8() function
    :return:
    """
    wlength_C60 = p8()
    assert (isinstance(wlength_C60, float))
    assert (np.isclose(wlength_C60, 9.273e-13, rtol=1e-3))


def test_p9():
    """
    testing p8() function
    :return:
    """
    ad3 = p9()
    assert (isinstance(ad3, bool))
    assert (ad3 is True)


def test_p10():
    """
    testing p10() function
    :return:
    """
    ad3b = p10()
    assert (isinstance(ad3b, set) or isinstance(ad3b, list) or isinstance(ad3b, tuple))
    assert (len(ad3b) == 1)
    assert (set(map(str.casefold, ad3b)) == {"b"})


def test_p11():
    """
    testing p11() function
    :return:
    """
    ad4 = p11()
    assert (isinstance(ad4, float))
    assert (np.isclose(ad4, constants.h / 1e-13, rtol=1e-3))


def test_p12():
    """
    testing p12() function
    :return:
    """
    ad5 = p12()
    assert (isinstance(ad5, float))
    assert (np.isclose(ad5, 2.467e15, rtol=1e-3))


def test_p13():
    """
    testing p13() function
    :return:
    """
    ad6 = p13()
    assert (isinstance(ad6, set) or isinstance(ad6, list) or isinstance(ad6, tuple))
    assert (len(ad6) > 0)
    assert (set(map(str.casefold, ad6)) == {"e"} or set(map(str.casefold, ad6)) == {"b", "e"})


def test_p14():
    """
    testing p14() function
    :return:
    """
    ad7 = p14()
    assert (isinstance(ad7, set) or isinstance(ad7, list) or isinstance(ad7, tuple))
    assert (len(ad7) > 0)
    assert (set(map(str.casefold, ad7)) == {"a", "c", "d"})


def test_p15():
    """
    testing p15() function
    :return:
    """
    p_from_k, E_from_k = p15()
    assert (isinstance(p_from_k, float))
    assert (isinstance(E_from_k, float))
    assert (np.isclose(p_from_k, 1.055e-27, rtol=1e-3))
    assert (np.isclose(E_from_k, 3.162e-19, rtol=1e-3))


def test_p16():
    """
    testing p16() function
    :return:
    """
    momentum_d9, frequency_d9 = p16()
    assert (isinstance(momentum_d9, float))
    assert (isinstance(frequency_d9, float))
    assert (np.isclose(momentum_d9, 1.069e-27, rtol=1e-3))
    assert (np.isclose(frequency_d9, 4.836e+14, rtol=1e-3))


def test_p17():
    """
    testing p16() function
    :return:
    """
    wl_baseball = p17()
    assert (isinstance(wl_baseball, float))
    assert (np.isclose(wl_baseball, 1.e-34, rtol=1e-2))


def test_p18():
    """
    testing p18() function
    :return:
    """
    ansSE2 = p18()
    assert (isinstance(ansSE2, set) or isinstance(ansSE2, list) or isinstance(ansSE2, tuple))
    assert (len(ansSE2) == 1)
    assert (set(map(str.casefold, ansSE2)) == {"e"})


def test_p19():
    """
    testing p19() function
    :return:
    """
    prob_canbe_negative = p19()
    assert (isinstance(prob_canbe_negative, bool))
    assert (prob_canbe_negative is False)


def test_p20():
    """
    testing p20() function
    :return:
    """
    zzstar = p20()
    assert (isinstance(zzstar, set) or isinstance(zzstar, list) or isinstance(zzstar, tuple))
    assert (len(zzstar) > 0)
    assert (set(map(str.casefold, zzstar)) == {"b", "d"})


def test_p21():
    """
    testing p20() function
    :return:
    """
    is_also_eigenfunction = p21()
    assert (isinstance(is_also_eigenfunction, bool))
    assert (is_also_eigenfunction == True)


