import pytest
from data.test_data import test_data
from parsing_bytes_ver1 import get_data_from_payload as parse_slice
from parsing_bytes_ver2 import get_data_from_payload as parse_bit_shifting


@pytest.fixture(scope="session")
def name(pytestconfig):
    return pytestconfig.getoption("name")


@pytest.mark.parametrize("test_input,expected", test_data)
def test_parser(name, test_input, expected):
    if name == 'slicer':
        print('Test using slice method')
        assert parse_slice(test_input) == expected, 'Error while testing with slice method'
    if name == 'bit_shift':
        print('Test using bit_shifting method')
        assert parse_bit_shifting(test_input) == expected, 'Error while testing with bit shifting method'
