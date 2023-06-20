import glob, os
import json

os.chdir(".")

def read_file(file):
    with open(file, 'r') as file:
        return file.read()


def write_json(file, data):
    with open(file, 'w') as fout:
        json.dump(data, fout, indent=4)

for file in glob.glob("*.txt"):
    content = read_file(file)

    to_parse_in_rows = content.replace('[', '').replace(']', '').split(', ')

    rows = []

    for part in to_parse_in_rows:
        field12, field3, field4, field5 =  part.replace("'", '').split(',')

        field1, field2 = field12.split('~')

        row = {
            'class': field1,
            'field2': int(field2),
            'field3': int(field3),
            'field4': int(field4),
            'field5': int(field5)
        }

        rows.append(row)

    write_json(file.replace('.txt', '.json'), rows)