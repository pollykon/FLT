from parsing import Parser
from utils import print_grammar
from first import First
from follow import Follow
import argparse

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
	lines = [i for i in lines if len(i) > 0]
	return lines


if __name__ == "__main__":
	input_lines = read_grammar()
	parser = Parser()
	grammar = parser.parse_grammar(input_lines)
	grammar_copy = grammar.copy()
	print_grammar(grammar)

	parser = argparse.ArgumentParser(description="First and follow sets")

	parser.add_argument(
		"-k", default=1, type=int,
		help="Length of elements in first_k set",
	)
	args = parser.parse_args()

	first = First(grammar, args.k)
	first_set = first.get_first_set()
	print('First set: ', first_set)

	first_1 = First(grammar, 1)
	first_set_1 = first_1.get_first_set()

	follow = Follow(grammar_copy, first_set_1)
	follow_set = follow.get_follow_set()
	print('Follow set: ', follow_set)
