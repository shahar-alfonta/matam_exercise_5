import sys
import json

ALPHABET_LENGTH = 26
O_INDEX_NOT_FOUND = -1


class JSONFileError(Exception):
    pass


class Enigma:
    def __init__(self, hash_map, wheels, reflector_map):
        self.hash_map_stoi = hash_map
        self.hash_map_itos = {value: key for key, value in hash_map.items()}
        self.wheels = wheels
        self.reflector_map = reflector_map

        self.original_wheels = wheels.copy()

    def reload_wheels(self):
        self.wheels = self.original_wheels.copy()

    def move_wheels(self, message_length):
        self.wheels[0] = self.wheels[0] % 8 + 1

        if message_length % 2 == 0:
            self.wheels[1] *= 2
        else:
            self.wheels[1] -= 1

        if message_length % 10 == 0:
            self.wheels[2] = 10
        elif message_length % 3 == 0:
            self.wheels[2] = 5
        else:
            self.wheels[2] = 0

    def weird_value(self):
        return (self.wheels[0] * 2 - self.wheels[1] + self.wheels[2]) % ALPHABET_LENGTH

    def encrypt_letter(self, letter):
        # step 1
        i = self.hash_map_stoi[letter]

        # step 2
        if self.weird_value() != 0:
            i += self.weird_value()
        else:
            i += 1

        # steps 3, 4, 5, 6
        i %= ALPHABET_LENGTH
        c1 = self.hash_map_itos[i]
        c2 = self.reflector_map[c1]
        i = self.hash_map_stoi[c2]

        # step 7
        if self.weird_value() != 0:
            i -= self.weird_value()
        else:
            i -= 1

        # steps 8, 9
        i %= ALPHABET_LENGTH
        c3 = self.hash_map_itos[i]

        return c3

    def encrypt(self, message):
        cipher_length = 0
        encrypted_message = ""
        for letter in message:
            if letter.islower():
                cipher_length += 1
                letter = self.encrypt_letter(letter)
            encrypted_message += letter
            self.move_wheels(cipher_length)
        self.reload_wheels()
        return encrypted_message

    def encrypt_file(self, input_file_path):
        encrypted_messages = []

        with open(input_file_path, 'r') as input_file:
            message = input_file.readline()
            while message:
                encrypted_messages.append(self.encrypt(message))
                message = input_file.readline()

        return encrypted_messages


def load_configuration_from_path(path):
    try:
        with open(path, 'r') as conf_file:
            conf_dict = json.load(conf_file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise JSONFileError()

    return Enigma(
        conf_dict['hash_map'],
        conf_dict['wheels'],
        conf_dict['reflector_map']
    )


def handle_argparse():
    try:
        c_index = sys.argv.index('-c')
        i_index = sys.argv.index('-i')
    except ValueError:
        print("Usage: python3 enigma.py -c <config_file> -i <input_file> -o <output_file>")
        exit(1)

    try:
        o_index = sys.argv.index('-o')
    except ValueError:
        o_index = O_INDEX_NOT_FOUND

    args_dict = {'config_file': sys.argv[c_index + 1], 'input_file': sys.argv[i_index + 1]}
    if o_index != O_INDEX_NOT_FOUND:
        args_dict['output_file'] = sys.argv[o_index + 1]

    return args_dict


def main():
    args = handle_argparse()
    enigma = load_configuration_from_path(args['config_file'])

    encrypted_messages = enigma.encrypt_file(args['input_file'])

    if args.get('output_file'):
        with open(args['output_file'], 'w') as output_file:
            for cipher in encrypted_messages:
                output_file.write(cipher)
    else:
        print(*encrypted_messages, sep='')


if __name__ == "__main__":
    main()
    # try:
    #     main()
    # except:
    #     print("The enigma script has encountered an error")
    #     exit(1)
