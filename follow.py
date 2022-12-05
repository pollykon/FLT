class Follow:
    nterms = []
    follow_dict = dict()

    def __init__(self, grammar, first_set):
        self.grammar = grammar
        self.first_set = first_set

    def get_nterms(self):
        grammar = self.grammar

        for rule in grammar:
            if rule['left'] not in self.nterms:
                self.nterms.append(rule['left'])
            for right_rule in rule['right']:
                if right_rule['type'] == 0 and right_rule['value'] not in self.nterms:
                    self.nterms.append(right_rule['value'])

    def get_follow_set(self):
        self.get_nterms()

        self.follow_dict['S'] = set()
        self.follow_dict['S'].add('$')

        for nterm in self.nterms:
            if nterm != 'S':
                self.follow_dict[nterm] = set()
            rules = self.find_all_rules_by_nterm(nterm)
            self.find_follow_set(nterm, rules)
        return self.follow_dict

    def find_follow_set(self, left, rules):
        for rule in rules:
            for right_rule in rule['right']:
                if right_rule['value'] == left:
                    index = rule['right'].index(right_rule)
                    if index == len(rule['right']) - 1:
                        new_set = self.find_follow_set_for_nterm(rule['left'])
                        if new_set is not None:
                            for set_el in new_set:
                                self.follow_dict[left].add(set_el)
                    else:
                        next_rule = rule['right'][index + 1]
                        if next_rule['type'] == 0:
                            first_set = self.find_first_set_for_nterm(next_rule['value'])
                            for set_el in first_set:
                                if set_el == '' and rule['right'].index(next_rule) == len(rule['right']) - 1:
                                    self.follow_dict[left].add('$')
                                    if rule['left'] in self.follow_dict:
                                        for follow_set_el in self.follow_dict[rule['left']]:
                                            self.follow_dict[left].add(follow_set_el)
                                elif set_el == '' and rule['right'].index(next_rule) != len(rule['right']) - 1:
                                    new_rules = []
                                    new_rule = {'left': left, 'right': rule['right'].copy()}
                                    new_rule['right'].remove(next_rule)
                                    new_rules.append(new_rule)
                                    self.find_follow_set(left, new_rules)
                                else:
                                    self.follow_dict[left].add(set_el)
                        if next_rule['type'] == 1:
                            self.follow_dict[left].add(next_rule['value'])

    def find_first_set_for_nterm(self, left):
        return self.first_set[left]

    def find_follow_set_for_nterm(self, left):
        if left in self.follow_dict:
            return self.follow_dict[left]

    def find_all_rules_by_nterm(self, left):
        grammar = self.grammar

        rules = []

        for rule in grammar:
            for right_rule in rule['right']:
                if right_rule['type'] == 0 and right_rule['value'] == left:
                    rules.append(rule)
        return rules
