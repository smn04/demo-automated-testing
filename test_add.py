from add import add_two_numbers,subtract_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(3,4) == 7
    print('TEST 1: 3+4 = 7 is tested sucessfully')
    assert add_two_numbers('a',3) == 'Can only perform addition on numbers'
    print('TEST 2: "a"+3 gives error is tested sucessfully')

if __name__ == '__main__':
    test_add_two_numbers()
