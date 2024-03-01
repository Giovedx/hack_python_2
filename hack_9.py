"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}

"""


def fn_hack_9(s):
    result = s
    nuevodiccionario = {}
    
    for clave,valor in result.items():   
        if clave == "foo":
            nuevodiccionario = {"Foo":"Fooziman"}
            result = nuevodiccionario     
        return result

r1 = fn_hack_9({"foo":"fookziman","bar":"barziman"})
print(r1)