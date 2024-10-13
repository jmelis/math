def parse_elements_arg(elements_arg):
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
    identity = g3_identity(table)

    elements = list(table.keys())
    for i in elements:
        if True not in [(table[i][j]==identity and table[j][i]==identity) for j in elements]:
            return False
    return True

if __name__ == '__main__':
    """
    python3 lib/cayley.py '1-3,5' 'x*y % 7'
    ╒════╤═════╤═════╤═════╤═════╕
    │    │   1 │   2 │   3 │   5 │
    ╞════╪═════╪═════╪═════╪═════╡
    │  1 │   1 │   2 │   3 │   5 │
    ├────┼─────┼─────┼─────┼─────┤
    │  2 │   2 │   4 │   6 │   3 │
    ├────┼─────┼─────┼─────┼─────┤
    │  3 │   3 │   6 │   2 │   1 │
    ├────┼─────┼─────┼─────┼─────┤
    │  5 │   5 │   3 │   1 │   4 │
    ╘════╧═════╧═════╧═════╧═════╛
    G1 closure:   False
    G3 identity:  1
    G4 inverses:  False
    """

    import sys
    import tabulate

    if '--latex' in sys.argv:
        sys.argv.remove('--latex')
        tablefmt = "latex"
    else:
        tablefmt = "fancy_grid"

    elements_arg = sys.argv[1]
    operation = sys.argv[2]

    elements = parse_elements_arg(elements_arg)
    table = cayley_table(elements, operation)

    # print table with tabulate
    headers = [""] + elements
    rows = []
    for i in elements:
        rows.append([i] + get_row(table, i))
    print(tabulate.tabulate(rows, headers, tablefmt=tablefmt))

    print("G1 closure:  ", g1_closure(table))
    print("G3 identity: ", g3_identity(table))
    print("G4 inverses: ", g4_inverses(table))
