grammar EdataLr;

expr : expr op=('+'|'|') expr # AndOr
     | WORD                   # Word
     | '(' expr ')'           # Parens
     | op='-' WORD            # Not
     ;

WORD : [a-zA-Z]+|[t|c][:][a-zA-Z]+;
AND  : '+';
OR   : '|';
NOT  : '-';

WS   : [ \t\r\n]+ -> skip;
