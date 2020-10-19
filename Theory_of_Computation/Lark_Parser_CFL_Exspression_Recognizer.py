#%% 
from lark import Lark
#%%
grammar =   Lark(r"""

        inpt: expr oper expr
        
        expr: par
            | expr oper expr
            | num

        oper: "*" 
            | "+" 
            | "/" 
            | "-" 

        par: "(" expr ")"

        num:    SIGNED_NUMBER 
            | "(" SIGNED_NUMBER ")"

%import     common.SIGNED_NUMBER
%import     common.WS
%ignore     WS

            """, start='expr')



# %%
text = "(3 -23) + (-23 / (4 + 3))"
grammar.parse(text)
print(_.pretty())

# %%
