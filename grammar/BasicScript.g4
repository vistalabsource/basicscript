grammar BasicScript;

program: statement* EOF;

statement:
	assign ';'
	| expr_s ';'
	| if
	| while
	| for
	| try_catch
	| throw ';'
	| break ';'
	| continue ';'
	| function
	| return ';';

assign: 'let' ID ':' expr;
expr_s: expr;
if: 'if' expr block (ELSE block | ELSE if)?;
ELSE: 'else';
while: 'while' expr block;
for: 'for' ID ':' expr block;
try_catch: 'try' block 'catch' ID block;
throw: 'throw' expr;
break: 'break';
continue: 'continue';
function: 'function' ID (':' param_list)? block;
param_list: ID (',' ID)*;
return: 'return' expr?;

block: '{' statement* '}';

expr:
	expr '||' expr							# Or
	| expr '&&' expr						# And
	| '!' expr								# Not
	| expr ('==' | '!=') expr				# Eq
	| expr ('<' | '<=' | '>' | '>=') expr	# Rel
	| expr '[' expr ']'						# Index
	| '[' arg_list? ']'						# Array
	| '{' pair_list? '}'                    # Dict
	| expr op = ('+' | '-') expr			# AddSub
	| expr op = ('*' | '/') expr			# MulDiv
	| expr '^' expr							# Pow
	| expr '%' expr							# Mod
	| expr ID								# MulImplied
	| ID '(' arg_list? ')'					# FuncCall
	| INT									# Int
	| FLOAT									# Float
	| STRING								# String
	| 'True'								# True
	| 'False'								# False
	| ID									# Id
	| '(' expr ')'							# Parens;

arg_list: expr ( ',' expr)*;
pair_list: pair (',' pair)*;
pair: STRING ':' expr;

ID: [a-zA-Z_][a-zA-Z0-9_]*;
FLOAT: [0-9]+ '.' [0-9]+;
STRING:
	'"' (~["\\] | '\\' .)* '"'
	| '\'' (~['\\] | '\\' .)* '\'';
INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;
LINE_COMMENT: '/*' .*? '*/' -> skip;