"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    letter = ["f","n","b"]
    array = []
        
    for i in result:
        if i not in letter:
           array.append(i)
    
    result = "".join(array)
    
    return result

r1 = fn_hack_4("fooziman")
r2 = fn_hack_4("barziman")
r3 = fn_hack_4("qux")

print(r1)
print(r2)
print(r3)
