grammar EdataLr;

expr : expr op=('+'|'|') expr # AddOr
     | WORD                   # Word
     | '(' expr ')'           # Parens
     | op='-' WORD          # Not
     ;

WORD : [a-z]+;
ADD  : '+';
OR   : '|';
NOT  : '-';

WS   : [ \t\r\n]+ -> skip;
