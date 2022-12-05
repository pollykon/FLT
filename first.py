import copy


def product(set1, set2, max_num):
    res = set()

    if len(set1) == 0:
        return set2
    if len(set2) == 0:
        return set1

    for a in set1:
        for b in set2:
            res.add((a + b)[:max_num])
    return res


class First:
    nterms = []
    first_dict = dict()
    first_set = set()
    visited = set()

    def __init__(self, grammar, k):
        self.grammar = grammar
        self.k = k

    def get_nterms(self):
        grammar = self.grammar

        for rule in grammar:
            if rule['left'] not in self.nterms:
                self.nterms.append(rule['left'])
            for right_rule in rule['right']:
                if right_rule['type'] == 0 and right_rule['value'] not in self.nterms:
                    self.nterms.append(right_rule['value'])

    def find_all_rules(self, left):
        grammar = self.grammar

        rules = []

        for rule in grammar:
            if rule['left'] == left[0]:
                rules.append(rule)
        return rules

    def find_first_set(self, k, symbols, visited):
        if k == 0:
            return set()

        if len(symbols) == 0:
            return {tuple()}

        if symbols[0] not in self.nterms:
            return product(
                {(symbols[0],)},
                self.find_first_set(k - 1, symbols[1:], visited),
                k
            )

        curr_visited = copy.deepcopy(visited)
        first = set()
        for rule in self.find_all_rules([symbols[0]]):
            nterms = []
            for right_rule in rule['right']:
                nterms.append(right_rule['value'])

            if rule['right'][0]['value'] == symbols[0] and symbols[0] in curr_visited:
                first.update(product(
                    self.find_first_set(k - 1, nterms, curr_visited),
                    self.find_first_set(k - 1, symbols[1:], curr_visited),
                    k
                ))
            else:
                curr_visited.add(symbols[0])
                first.update(self.find_first_set(k, nterms, curr_visited))

        return first

    def get_first_set(self):
        self.get_nterms()
        for nterm in self.nterms:
            self.first_dict[nterm] = set()

        for nterm in self.nterms:
            firsts = self.find_first_set(self.k, [nterm], set())
            for first in firsts:
                prefix = ''
                for word in first:
                    prefix += word
                self.first_dict[nterm].add(prefix)

        return self.first_dict
