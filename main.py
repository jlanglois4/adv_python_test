import csv
from pathlib import Path

ufos = {}
output_list = []


def main():
    file_path = Path.cwd() / "ufo.csv"

    if file_path.exists():
        with file_path.open() as my_file:
            csv_reader = csv.reader(my_file)
            next(csv_reader)  # skip headings
            for line in csv_reader:
                type = line[4]
                if type in ufos:
                    ufos[type] += 1
                else:
                    ufos[type] = 1

    for key in ufos:
        print(f"{key} {ufos[key]}")
        output_list.append([key, ufos[key]])


def output():
    with open('./output.csv', 'wt') as f:
        csv_writer = csv.writer(f, delimiter='|')
        csv_writer.writerows(output_list)


if __name__ == "__main__":
    main()
    output()
