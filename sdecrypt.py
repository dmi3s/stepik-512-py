from simplecrypt import encrypt, decrypt, DecryptionException


def main():
    with open("data/encrypted.bin", "rb") as inp:
        encrypted = inp.read()

    with open("data/passwords.txt", "r") as inp:
        pwds = list(map(lambda s: s.strip(), inp.readlines()))

    for p in pwds:
        try:
            r = decrypt(p, encrypted).decode('utf8')
            print(r)
            break
        except DecryptionException:
            continue


main()
