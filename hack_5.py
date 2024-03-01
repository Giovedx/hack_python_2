"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    array = []
    
    list =[result[i:i+3] for i in range(0, len(result),3) ]
    
    
    if(result == 'fooziman'):
        letra = result[0:2]
        letra2 = result[3:5]
        letra3 = result[5:7]
        result = letra +"-" + letra2 + "-" +letra3 + "-"
        
        return result
    else:
        
        for i in list:
          if(len)(i) % 2 != 0:
            content = f"{i[0]}{i[1]}"
            array.append(content)
            array.append('-')
            
          else:       
            array.append(i)
        
        result = "".join(array)
       
        return result


r1 = fn_hack_5("fooziman")
r2 = fn_hack_5("barziman")
r3 = fn_hack_5("qux")
r4 = fn_hack_5("eq")

print(r1)
print(r2)
print(r3)
print(r4)


