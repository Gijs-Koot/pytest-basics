from ptb import funcs

def test_badsum():

    assert funcs.badsum(1, 3) == 4, "1 and 3 makes 4!"


def test_with_tmppath(tmp_path):
    
    print(tmp_path)

    assert True



def not_test_badsum_with_fixture(correct_sums):

    for a, b, c in correct_sums:
        assert funcs.badsum(a, b) == c, f"{a} and {b} makes {c}!"
    