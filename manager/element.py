import os

def copy(src_file, destination_file):
    with open(src_file, 'r') as f:
        dane = f.read()
    with open(destination_file, 'w') as f:
        f.write(dane)

if __name__ == '__main__':
    exercises_path = os.path.dirname(__file__)
    src_file = os.path.join(exercises_path, 'dane', 'plik.txt')
    destination_file = os.path.join(exercises_path, 'dane', 'copied-plik.txt')
    copy(
        src_file=src_file,
        destination_file=destination_file,
    )