import json

ALPHABET_LENGTH = 26


class JSONFileError(Exception):
    pass


class Enigma:
    def __init__(self, hash_map, wheels, reflector_map):
        self.hash_map = hash_map
        self.wheels = wheels
        self.reflector_map = reflector_map

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
        if not letter.isupper():
            return letter

        # step 1
        i = self.hash_map[letter]

        # step 2
        if self.weird_value() != 0:
            i += self.weird_value()
        else:
            i += 1

        # steps 3, 4, 5, 6
        i %= ALPHABET_LENGTH
        c1 = self.hash_map[i]
        c2 = self.reflector_map[c1]
        i = self.hash_map[c2]

        # step 7
        if self.weird_value() != 0:
            i -= self.weird_value()
        else:
            i -= 1

        # steps 8, 9
        i %= ALPHABET_LENGTH
        c3 = self.hash_map[i]

        return c3

    def encrypt(self, message):
        message_length = 0
        new_message = ""
        for c in message:
            message_length += 1
            new_message += self.encrypt_letter(c)
        self.move_wheels(message_length)
        return new_message


def load_enigma_from_path(path):
    try:
        with open(path, 'r') as conf_file:
            conf_dict = json.load(conf_file)
    except:
        raise JSONFileError

    return Enigma(
        conf_dict['hash_map'],
        conf_dict['wheels'],
        conf_dict['reflector_map']
    )


def main():
    pass


if __name__ == "__main__":
    main()
