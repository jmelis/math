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
