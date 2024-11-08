
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftMASMENOSleftPORDIVIDIDOrightUMENOSAND BOOLEAN BREAK CADENA CASE CHAR COMMENTBLOCK CONSOLE CONST CONTINUE CORDER CORIZQ DECIMAL DEFAULT DESCRE DESIGUALDAD DIVIDIDO ELSE ENTERO FALSE FLOAT FOR FUNCTION ID IF IGUALDAD INCRE INDEXOF INTERFACE JOIN KEYS LENGTH LLAVDER LLAVIZQ LOG MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MODULO NOT NUMBER OBJECT OR PARDER PARIZQ PARSEFLOAT PARSEINT POP POR PUNTO PUNTOCOMA PUSH RETURN STRING SWITCH TERNARIO TOLOWERCASE TOSTRING TOUPPERCASE TRUE TYPEOF VALUES VAR WHILEinstrucciones    : TOUPPERCASEinstruccion : CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMAexpresion : expresion MAS expresion\n                  | expresion MENOS expresion\n                  | expresion POR expresion\n                  | expresion DIVIDIDO expresionexpresion : MENOS expresion %prec UMENOSexpresion : PARIZQ expresion PARDERexpresion    : ENTERO\n                    | CADENA'
    
_lr_action_items = {'TOUPPERCASE':([0,],[2,]),'$end':([1,2,],[0,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> TOUPPERCASE','instrucciones',1,'p_instrucciones_lista','main.py',162),
  ('instruccion -> CONSOLE PUNTO LOG PARIZQ expresion PARDER PUNTOCOMA','instruccion',7,'p_instruccion_console','main.py',165),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria','main.py',169),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria','main.py',170),
  ('expresion -> expresion POR expresion','expresion',3,'p_expresion_binaria','main.py',171),
  ('expresion -> expresion DIVIDIDO expresion','expresion',3,'p_expresion_binaria','main.py',172),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','main.py',179),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_agrupacion','main.py',183),
  ('expresion -> ENTERO','expresion',1,'p_expresion_number','main.py',187),
  ('expresion -> CADENA','expresion',1,'p_expresion_number','main.py',188),
]
