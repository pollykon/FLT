from utils import get_new_first

class First:
    nterms = []
    first_dict = dict()
    visited = set()
    first_set = set()

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

    def find_first_set(self, k, rule_els, checked):
        if k == 0:
            return set()

        if len(rule_els) == 0:
            return {tuple()}

        if rule_els[0] not in self.nterms:
            return get_new_first(
                {(rule_els[0],)},
                self.find_first_set(k - 1, rule_els[1:], checked),
                k
            )

        curr_visited = checked.copy()
        first = set()
        for rule in self.find_all_rules([rule_els[0]]):
            nterms = []
            for right_rule in rule['right']:
                nterms.append(right_rule['value'])

            if rule['right'][0]['value'] == rule_els[0] and rule_els[0] in curr_visited:
                first.update(get_new_first(
                    self.find_first_set(k - 1, nterms, curr_visited),
                    self.find_first_set(k - 1, rule_els[1:], curr_visited),
                    k
                ))
            else:
                curr_visited.add(rule_els[0])
                first.update(self.find_first_set(k, nterms, curr_visited))

        return first
