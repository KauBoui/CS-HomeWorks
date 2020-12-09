#%% 
from lark import Lark
from lark import Transformer
#%%
grammar =   Lark(r"""

        inpt: expr oper expr 
        
        expr: par
            | expr oper expr
            | num
            | coef_var

        oper: "*" -> mul
            | "+" -> add
            | "/" -> div
            | "-" -> sub
            | "^" -> exp

        par: "(" expr ")" -> par_expr

        num:    SIGNED_NUMBER -> number
            | "(" SIGNED_NUMBER ")" -> par_number

        coef_var: num? CNAME -> var
            | "(" num? CNAME ")" -> par_var

%import     common.SIGNED_NUMBER
%import     common.CNAME
%import     common.WS
%ignore     WS

            """, start='inpt')

# %%
text = "(3 -23) + (-23^3 / (4a + c))"
print(grammar.parse(text).pretty())


