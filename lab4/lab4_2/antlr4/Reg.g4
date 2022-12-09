grammar Reg;
start : 'a' a | 'b' b | EOF;
a : 'a' a | 'b' b | EOF;
b : 'b' c;
c : 'a' a | 'b' c | 'c' c | EOF;
