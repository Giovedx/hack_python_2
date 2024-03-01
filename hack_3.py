"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    new = ""
    
    if ('a' in s) or ('e' in s) or ('i' in s) or ('o' in s) or ('u' in s) or ('q' in s ):
          new =  (s.replace("a","@")
                   .replace("e","3")
                   .replace("i","¡")
                   .replace("o","0")
                   .replace("u","v")
                   .replace("q","Q")
                   .replace("f","F")
                   .replace("n","N")
                   .replace("b","B") 
                   .replace("x","X"))
    
   
    else:
       print(result)
       
    result = new
    
    return result


r1 = fn_hack_3("fooziman")
r2 = fn_hack_3("barziman")
r3 = fn_hack_3("3q")
r4 = fn_hack_3("qu")
r5 = fn_hack_3("qux")
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)

