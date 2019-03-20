from katas.knights_dialer import dialer, dialer_dp


def test_dialer():
    assert 1 == dialer(1, 0)


def test_dialer1():
    assert 5 == dialer(1, 2)


def test_dialer2():
    assert 6 == dialer(6, 2)


def test_dialer3():
    assert 18136064 == dialer(6, 20)


def test_dialer4():
    assert 0 != dialer(6, 500)


def test_dialer_dp():
    # assert 1 == dialer_dp(1, 0)
    # assert 2 == dialer_dp(1, 1)
    assert 1 == dialer_dp(6, 0)
    assert 3 == dialer_dp(6, 1)
    # assert 5 == dialer_dp(1, 2)
    assert 6 == dialer_dp(6, 2)
    assert 18136064 == dialer_dp(6, 20)


def test_dialer_dp_2():
    assert 0 != dialer_dp(6, 5000)
