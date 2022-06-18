import configuration
from bitstring import BitArray
from textwrap import wrap


def hex_to_bit(input_hex_str: str) -> str:
    """Returns a string with a binary number from a string with a hex value"""
    return str(BitArray(hex=input_hex_str).bin)


def to_little_endian(input_string: str) -> str:
    """Returns a string of bits with each byte flipped from right to left"""
    wrap_list = wrap(input_string, 8)
    return ''.join([i[::-1] for i in wrap_list])


def get_data_from_payload(payload: str) -> dict:
    """Main parser"""
    payload_bit_str = hex_to_bit(payload)
    payload_reversed_bytes_str = to_little_endian(payload_bit_str)

    parsed_data = {}

    for _id, seq in enumerate(configuration.device_settings):
        for offset, field in seq.items():
            start_idx = _id * 8 + offset

            parse_data_value = str(int(payload_reversed_bytes_str[start_idx:start_idx + field[0]], 2))

            if field[1] == 'field1':
                parsed_data[field[1]] = configuration.field1[parse_data_value]
            elif field[1] == 'field4':
                parsed_data[field[1]] = configuration.field4[parse_data_value]
            elif field[1] == 'field8':
                parsed_data[field[1]] = configuration.field8[parse_data_value]
            else:
                parsed_data[field[1]] = f'{int(parse_data_value):02d}'
    return parsed_data
