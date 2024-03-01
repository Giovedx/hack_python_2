"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vowerls = ["a","e","i","o","u"]
    _str = []
    
    for txt in result:
        if txt not in vowerls:
            _str.append(txt)
            
    result = "".join(_str)
    
    
    return result
    
r1 = fn_hack_2("fooziman")
r2 = fn_hack_2("barziman")
r3 = fn_hack_2("qux")

print(r1)
print(r2)
print(r3)