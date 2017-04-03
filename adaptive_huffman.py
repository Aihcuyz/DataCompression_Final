from sender import encoder
from receiver import decoder

sender = encoder()
receiver = decoder()

def adapter_huffman(input_string = ''):
    line_encoded_code = ''

    for input_char in input_string:
        encoded_code = sender.encode(input_char)
        receiver.decode(encoded_code)
        line_encoded_code = line_encoded_code + encoded_code
    return line_encoded_code

if __name__ == '__main__':
    binary_code = ''
    with open('input_content.txt') as file_pointer:
        open('encode_log.log','w').close()
        open('decode_log.log','w').close()
        for line_string in file_pointer:
            binary_code = binary_code + adapter_huffman(input_string=line_string)
    print binary_code

