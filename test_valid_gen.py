from succ_utils import CreditIdentifier


def test_valid():
    ci = CreditIdentifier()
    assert ci.valid("914210031524040048") == False


def test_gen():
    ci = CreditIdentifier()
    ret = ci.gen_random_credit_code()
    print(ret["code"])
    assert ci.valid(ret["code"])
