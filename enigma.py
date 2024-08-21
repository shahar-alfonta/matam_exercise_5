import json

class JSONFileError(Exception):
    pass

def encrypt_letter(self, letter):
    if c.isupper():
        i = hash_map[c]
        if ((wheels[0] * 2 - wheels[2] + wheels[3]) % 26 != 0):
            i += (wheels[0] * 2 - wheels[2] + wheels[3]) % 26
        else:
            i += 1
        i = i % 26
        c1 = self.hash_map[i]
        c2 = self.reflector_map[c21]
        i = self.hash_map[c2]
        if ((wheels[0] * 2 - wheels[2] + wheels[3]) % 26 != 0):
            i -= (wheels[0] * 2 - wheels[2] + wheels[3]) % 26
        else:
            i -= 1
        c3 = self.hash_map[i]
        return c3


class Enigma:
    def __init__(self, hash_map, wheels, reflector_map):
        self.hash_map = hash_map
        self.wheels = wheels
        self.reflector_map = reflector_map
        self.new_message

    def encrypt(self, message):
        wheels = self.wheels
        for c in message:
            self.new_message += encrypt_letter(c)
        wheels[0] = wheels[0] % 8 + 1
        if sum(1 for letter in message if letter.islower()) % 2 == 0:
            wheels[1] *= 2
        else:
            wheels[1] -= 1
        if sum(1 for letter in message if letter.islower()) % 10 == 0:
            wheels[2] = 10
        elif sum(1 for letter in message if letter.islower()) % 10 == 0:
            wheels[2] = 5
            else:
            wheels[2] = 0

    return self.new_message


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

