import re

from тфя.lab4.git_polina.FLT.lab4.lab4_1.utils import Types

class Parser:
	def __init__(self):
		# compiling regexes to speed up
		self.nonterm_regex = re.compile("\[[A-Za-z]+[0-9]*\]")
		self.term_regex = re.compile("([A-Za-z]|[0-9])+")
		# ( nonterm | term )*
		self.right_part_regex = re.compile(
			# (term|nterm)*(\|(term|nterm)+)*
			"(([A-Za-z]|[0-9])|(\[[A-Za-z]+[0-9]*\]))*(\|(([A-Za-z]|[0-9])|(\[[A-Za-z]+[0-9]*\]))+)*"
			)

	def parse_grammar(self, lines):
		rules = []
		for line in lines:
			rules.extend(self.parse_rules(line))
		return rules

	def parse_rules(self, line):
		# parse nonterm
		res = self.get_nonterm_match(line)
		if res is None:
			raise ValueError(f"Error when parsing line: {line}. Not found first nonterminal")
		left_end_index = res.span()[1]
		symbol_left = line[1:left_end_index-1]
		# parse ->
		if not line[left_end_index:].startswith('->'):
			raise ValueError(f"Error when parsing line: {line}. Expected -> after nonterminal")
		line = line[left_end_index+2:]
		# parse right part
		lines = line.split('|')
		rules = []
		for part_line in lines:
			rule = {"left": None, "right": []}
			rule["left"] = symbol_left
			rule["right"] = self.parse_right_rule_part(part_line)
			rules.append(rule)
		return rules

	def parse_right_rule_part(self, line):
		assert self.right_part_regex.fullmatch(line),\
			f"Error when parsing line: {line}. Right part have invalid syntax"
		# использую while вместо рекурсии
		res = []
		while len(line)>0:
			if line[0] == '[':
				nonterm_end = line.find(']')
				res.append(self.parse_nonterm(line[:nonterm_end+1]))
				line = line[nonterm_end+1:]
			else:
				term_end = line.find('[')
				if term_end == -1:
					term_end = len(line)
				for i in range(term_end):
					res.append(self.parse_term(line[i]))
				line = line[term_end:]
		if len(res) == 0:
			res.append(self.parse_term('')) # add epsilon
		return res

	def parse_nonterm(self, value):
		return {
			"type": Types.nonterminal,
			"value": value[1:-1]
		}

	def parse_term(self, value):
		return {
			"type": Types.terminal,
			"value": value
		}

	def get_nonterm_match(self, value):
		return self.nonterm_regex.match(value)

	def get_term_match(self, value):
		return self.term_regex.match(value)