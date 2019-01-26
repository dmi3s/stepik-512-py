def main():
    with open("data/strings.txt", "rt") as f, open("data/result.txt", "wt") as w:
        lns = f.readlines()
        if not lns[-1][-1] == '\n':
            lns[-1] += '\n'
        w.writelines(reversed(lns))


main()
