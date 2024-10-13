def compose(s1, s2):
    out = [[], []]
    for i in range(len(s1[0])):
        key_s1 = s1[1][i]
        key_s2 = s2[0].index(key_s1)
        out[0].append(s1[0][i])
        out[1].append(s2[1][key_s2])
    return out

if __name__ == '__main__':
    import json
    import sys

    # python3 lib/sym_perms.py '[[1,2,3,4],[1,4,3,2]]' '[[1,4,3,2],[3,1,2,4]]'
    # [1, 2, 3, 4]
    # [3, 1, 2, 4]
    s1 = json.loads(sys.argv[1])
    s2 = json.loads(sys.argv[2])
    comp = compose(s1, s2)
    print(comp[0])
    print(comp[1])
