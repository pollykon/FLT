import re
import sys
import time

from parsing import Parser
from utils import print_grammar
from first import First
from follow import Follow


def read_grammar():
	lines = []
	while True:
		try:
			lines.append(input())
		except EOFError:
			break

	lines = [
		i.replace(' ', '').replace('\t', '').replace('\r', '')
		for i in lines
	]
	lines = [i for i in lines if len(i)>0]
	return lines


if __name__ == "__main__":
	input_lines = read_grammar()
	parser = Parser()
	grammar = parser.parse_grammar(input_lines)
	grammar_copy = grammar.copy()
	print_grammar(grammar)

	first = First(grammar, 2)
	first_set = first.get_first_set()
	print('First set: ', first_set)

	first_1 = First(grammar, 1)
	first_set_1 = first_1.get_first_set()

	follow = Follow(grammar_copy, first_set_1)
	follow_set = follow.get_follow_set()
	print('Follow set: ', follow_set)

	# first_k = FirstK(first_set, 5, grammar).get_first_k()
