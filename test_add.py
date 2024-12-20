from add import add_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(5,5) == 11
    print('TEST 1: 5+5 = 10 is tested sucessfully')
    assert add_two_numbers('a',3) == 'Can only perform addition on numbers'
    print('TEST 2: "a"+3 gives error is tested sucessfully')
    assert add_two_numbers(3.0,40.0) == 43.0
    print('TEST 3: 3.0+40.0 = 43.0 is tested sucessfully')
    assert add_two_numbers(9.0,40) == 49.0
    print('TEST 4: 9.0+40.0 = 49.0 is tested sucessfully')

if __name__ == '__main__':
    test_add_two_numbers()
