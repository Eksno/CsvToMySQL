import csv


def csvToList(csv_file):
    print("\nOpening", csv_file + "...")

    with open(csv_file, newline='') as f:
        reader = csv.reader(f)

        print("Opened.\nCreating list of contents...")

        val = []
        for row in reader:
            val.append(row)

    print("List created.\nList:", val)

    return val
