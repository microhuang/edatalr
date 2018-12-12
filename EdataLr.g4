grammar EdataLr;

# 英文单词，支持 与 或 非 三种操作，括弧改变结合优先级

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
