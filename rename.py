import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

def rename_files():
    dirs = os.listdir(CURR_DIR)
    dirs = [d for d in dirs if os.path.isdir(d) and d[0] != '.']

    for subtopic in dirs:
        toBeRenamed = [i for i in os.listdir(subtopic) if i.startswith("Notes")]
        if len(toBeRenamed) == 0:
            continue
        print(toBeRenamed)
        for i in toBeRenamed:
            os.rename(os.path.join(CURR_DIR,subtopic, i), os.path.join(subtopic, i.replace("Notes", subtopic)))


if __name__ == "__main__":
    rename_files()