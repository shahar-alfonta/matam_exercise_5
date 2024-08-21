
ALPHABET_LENGTH = 26


class Enigma:
    def __init__(self, hash_map, wheels, reflector_map):
        self.new_message = None
        self.hash_map = hash_map
        self.wheels = wheels
        self.reflector_map = reflector_map

    def move_wheels (self, wheels , len):
        wheels[0] = wheels[0] % 8 + 1
        if len % 2 == 0:
            wheels[1] *= 2
        else:
            wheels[1] -= 1
        if len % 10 == 0:
            wheels[2] = 10
        elif len % 3 == 0:
            wheels[2] = 5
        else:
            wheels[2] = 0

    def encrypt_letter(self, letter):
        wheels = self.wheels
        if letter.isupper():
            i = self.hash_map[letter]
            if (wheels[0] * 2 - wheels[1] + wheels[2]) % ALPHABET_LENGTH != 0:
                i += (wheels[0] * 2 - wheels[1] + wheels[2]) % ALPHABET_LENGTH
            else:
                i += 1
            i = i % ALPHABET_LENGTH
            c1 = self.hash_map[i]
            c2 = self.reflector_map[c1]
            i = self.hash_map[c2]
            if (wheels[0] * 2 - wheels[1] + wheels[2]) % ALPHABET_LENGTH != 0:
                i -= (wheels[0] * 2 - wheels[1] + wheels[2]) % ALPHABET_LENGTH
            else:
                i -= 1
            c3 = self.hash_map[i]
            return c3
        else:
            return letter

    def encrypt(self, message):
        wheels = self.wheels
        len = 0
        for c in message:
            len +=1
            self.new_message += self.encrypt_letter(c)
        self.move_wheels(wheels, len)
        return self.new_message


def load_enigma_from_path(path):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
