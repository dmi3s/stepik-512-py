import os
import os.path


def collect(start):
    result = []
    for current_dir, dirs, files in os.walk(start):
        if any( f for f in files if f.endswith(".py")):
            result.append(current_dir)
    return result


def main():
    os.chdir("data/files")
    start = "main"
    dirs = collect(start)
    dirs.sort()
    with open("answer.txt", "wt", encoding="utf-8") as w:
        w.write("\n".join(dirs))


main()