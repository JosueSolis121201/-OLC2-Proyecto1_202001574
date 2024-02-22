

reservadas = {
    'console':'CONSOLE',
    'log':'LOG',
    'number':'NUMBER',
    'float':'FLOAT',
    'string':'STRING',
    'boolean':'BOOLEAN',
    'char':'CHAR',
    'var':'VAR',
    'true':'TRUE',
    'false':'FALSE',
    'const':'CONST',
    'if':'IF',
    'else':'ELSE',
    'switch':'SWITCH',
    'case':'CASE',
    'break':'BREAK',
    'default':'DEFAULT',
    'while':'WHILE',
    'for':'FOR',
    'continue':'CONTINUE',
    'return':'RETURN',
    'push':'PUSH',
    'pop':'POP',
    'join':'JOIN',
    'length':'LENGTH',
    'indexof':'INDEXOF',
    'interface':'INTERFACE',
    'object':'OBJECT',
    'values':'VALUES',
    'keys':'KEYS',
    'typeof':'TYPEOF',
    'function':'FUNCTION',
    'parseint':'PARSEINT',
    'parsefloat':'PARSEFLOAT',
    'tostring':'TOSTRING',
    'tolowercase':'TOLOWERCASE',
    'touppercase':'TOUPPERCASE'
}
# Lista de tokens
tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'PUNTO',
    'PUNTOCOMA',
    'CADENA',
    'ENTERO',
    'COMMENTBLOCK',
    'LLAVIZQ',
    'LLAVDER',
    'ID',
    'DECIMAL',
    'MODULO',
    'INCRE',
    'DESCRE',
    'IGUALDAD',
    'DESIGUALDAD',
    'MAYOR',
    'MAYORIGUAL',
    'MENOR',
    'MENORIGUAL',
    'AND',
    'OR',
    'NOT',
    'TERNARIO',
    'CORIZQ',
    'CORDER'
] + list(reservadas.values())


t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_PUNTO    = r'\.'
t_PUNTOCOMA    = r';'
t_LLAVIZQ    = r'{'
t_LLAVDER    = r'}'
t_MODULO   = r'%'
t_INCRE   = r'\+='
t_DESCRE   = r'-='
t_IGUALDAD  = r'=='
t_DESIGUALDAD   = r'!='
t_MAYOR   = r'>'
t_MAYORIGUAL   = r'>='
t_MENOR  = r'<'
t_MENORIGUAL   = r'<='
t_AND   = r'&&'
t_OR  = r'\|\|'
t_NOT   = r'!'
t_TERNARIO   = r'\?'
t_CORIZQ    = r'\['
t_CORDER    = r']'



def t_CADENA(t):
    r'\"(.+?)\"'
    try:
        t.value = str(t.value)
    except ValueError:
        print("Error %d", t.value)
        t.value = ''
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')  


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t


precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO'),
    ('right','UMENOS'),
    )

def p_instrucciones_lista(t):
    '''instrucciones    : TOUPPERCASE'''
    print(t[1])
def p_instruccion_console(t):
    '''instruccion : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA'''
    print(t[5])

def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = -t[2]

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_number(t):
    '''expresion    : ENTERO
                    | CADENA'''
    t[0] = t[1]

def p_error(p):
    if p:
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")



import ply.lex as Lex
import ply.yacc as yacc

if __name__ == '__main__':
    input_text = '''
            touppercase
            '''
    lexer = Lex.lex()
    parser = yacc.yacc()

    result = parser.parse(input_text)