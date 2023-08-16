from convert_to_binary import count_first_1s

def main():
    test_convert_to_binary()

def test_convert_to_binary():
    assert count_first_1s(125) == 5
    assert count_first_1s(439) == 3
    assert count_first_1s(0) == 0
    assert count_first_1s(1) == 0

if __name__ == "__main__":
    main()