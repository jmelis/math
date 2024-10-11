import sys

from tabulate import tabulate


def get_elements(elements_arg):
    elements = set()
    for chunk in elements_arg.split(","):
        if chunk.startswith("!"):
            add = False
            chunk = chunk[1:]
        else:
            add = True

        chunk_elements = get_chunk_elements(chunk)

        if add:
            elements.update(chunk_elements)
        else:
            elements.difference_update(chunk_elements)
    return sorted(elements)


def get_chunk_elements(chunk):
    if "-" in chunk:
        start, end = chunk.split("-")
        return set(range(int(start), int(end) + 1))
    else:
        return set([int(chunk)])


def cayley_table(elements, operation):
    table = {}
    for i in elements:
        table[i] = {}
        for j in elements:
            table[i][j] = eval(operation, {}, {"x": i, "y": j})
    return table


def get_row(table, el):
    return [table[el][j] for j in table.keys()]


def get_col(table, el):
    return [table[j][el] for j in table.keys()]


def g1_closure(table):
    elements = list(table.keys())
    for i in elements:
        for j in elements:
            if table[i][j] not in elements:
                return False
    return True


def g3_identity(table):
    elements = list(table.keys())
    for el in elements:
        if get_row(table, el) == elements and get_col(table, el) == elements:
            return el
    return None

def g4_inverses(table):
    # assume first one for now
    identity = g3_identity(table)

    elements = list(table.keys())
    for i in elements:
        if True not in [(table[i][j]==identity and table[j][i]==identity) for j in elements]:
            return False
    return True


def print_table(table):
    elements = list(table.keys())

    # header
    data = [[""] + elements]

    for el in elements:
        row = [el]
        for el2 in elements:
            row.append(table[el][el2])
        data.append(row)

    print(tabulate(data, headers="firstrow", tablefmt="grid"))

# parse arguments
if len(sys.argv) != 3:
    print("Usage: python cayley.py <element_set> <operation>")
    sys.exit(1)

elements_arg = sys.argv[1]
operation_arg = sys.argv[2]

elements = get_elements(elements_arg)

table = cayley_table(elements, operation_arg)
print_table(table)

identity = g3_identity(table)

print("Group 1 closure:", g1_closure(table))
print("Group 3 identity:", identity is not None, identity)
print("Group 4 inverses:", g4_inverses(table))
