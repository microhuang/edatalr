grammar EdataLr;

expr : expr op=('+'|'|') expr # AddOr
     | WORD                   # Word
     | '(' expr ')'           # Parens
     | op='-' WORD          # Not
     ;

WORD : t:[a-zA-Z]+|c:[a-zA-Z]+|[a-zA-Z]+;
ADD  : '+';
OR   : '|';
NOT  : '-';

WS   : [ \t\r\n]+ -> skip;
