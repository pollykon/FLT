class Types:
    nonterminal = 0
    terminal = 1

def get_nonterm_to_rule(grammar):
    nonterm_to_rule = {}
    for c, rule in enumerate(grammar):
        left = rule['left']
        #
        if left in nonterm_to_rule:
            nonterm_to_rule[left].append(c)
        else:
            nonterm_to_rule[left] = [c]
    return nonterm_to_rule

def print_grammar(grammar, border_top=False, border_bottom=False):
    if border_top:
        print('-'*40)
    nonterm_to_rule = get_nonterm_to_rule(grammar)
    for nonterm, rules_indexes in nonterm_to_rule.items():
        s = f"[{nonterm}] -> "
        for rule_ind in rules_indexes:
            s_rule = ""
            for item in grammar[rule_ind]['right']:
                if item['type'] == Types.nonterminal:
                    s_rule += f"[{item['value']}]"
                else:
                    if len(item['value']) == 0:
                        s_rule += "_eps_"
                    else:
                        s_rule += item['value']
            s_rule += " | "
            s += s_rule
        print(s[:-2])
    if border_bottom:
        print('-'*40)


def get_new_first(first1, first2, k):
    res = set()

    if len(first1) == 0:
        return first2
    if len(first2) == 0:
        return first1

    for a in first1:
        for b in first2:
            res.add((a + b)[:k])
    return res

