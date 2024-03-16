import pytest

TEST_LIST = [1, 2, 3]


def test_list_length():
    assert len(TEST_LIST) == 3


def test_list_append():
    TEST_LIST.append(4)
    assert TEST_LIST == [1, 2, 3, 4]


@pytest.mark.parametrize("input_value", TEST_LIST)
def test_list_index(input_value):
    assert TEST_LIST.index(input_value) == input_value - 1


def test_float_addition():
    float_number = 2.1 + 2.2
    assert round(float_number, 1) == 4.3


def test_float_multiplication():
    float_number = 1.1 * 2
    assert round(float_number, 1) == 2.2


def test_float_division():
    float_number = 5/2
    assert round(float_number, 1) == 2.5


def test_word_to_number_conversion():
    try:
        assert int('Hello')
    except ValueError:
        pass
