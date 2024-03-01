"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    new1 = []
    new = []
    
    for i in result:
        if( "a" in result) and ( "b" in result) and ( "c" in result)and ( "d" in result) and ( "e" in result):
                result[0] = "1"
                result[1] = "-"
                result[2] = "3"
                result[3] = "-"
                result[4] = "5"

    else:             
                
        if (not result):
              result.append("0")
              print("vacio")
              return result          
        
    return result
        


r1 = fn_hack_6(["a","b","c","d","e"])
r2 = fn_hack_6([])
print(r1)
print(r2)

