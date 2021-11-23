import sys

filename = sys.argv[1]
contacts = []


def split_string_in_whitespaces(string):
    full_split = string.strip().split(" ")
    split_parts = []
    for split_part in full_split:
        if split_part != "":
            split_parts.append(split_part)

    return split_parts


with open(filename) as file:
    header = split_string_in_whitespaces(file.readline())
    print(header)

    for line in file.readlines():
        if not line:
            continue

        line_values = split_string_in_whitespaces(line)
        contact_map = dict(zip(header, line_values))
        contacts.append(contact_map)

if __name__ == '__main__':
    for contact in contacts:
        print("First : {0} | Last : {1} | Email {2}".format(
            *contact.values()
        ))