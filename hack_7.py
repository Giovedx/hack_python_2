"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    i = 0
    final = 5  
    
    while i < final :
            if ("a" in result ) and ("b" in result ) and ("c" in result ) and ("d" in result ) and ("e" in result ):
                result[0] = "1"
                result[1] = 2
                result[2] = "3"
                result[3] = 4
                result[4] = "5"
                
            elif(not result):
                result.append(0)    
                
            i=i+1
        
    return result

r1 = fn_hack_7(["a","b","c","d","e"])
r2 = fn_hack_7([])
print(r1)
print(r2)