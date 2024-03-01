"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    arreglo = []
    newarreglo = []
    inicio= 1
    
    
    if(len)(result) % 2 != 0:
            for numero, result in enumerate(result, start=inicio):
                   newarreglo =  f"{result}-{numero}"
                   arreglo.append(newarreglo)  
            arreglo.reverse()    
            return arreglo
    else:
            for numero, result in enumerate(result, start=inicio):
                   newarreglo =  f"{numero}"
                   arreglo.append(newarreglo)  
            arreglo.reverse()   
            return arreglo

r1 = fn_hack_8(["a","b","c","d","e"])
r2 = fn_hack_8(["a","b","c"])
r3 = fn_hack_8(["a","b","c","d"])
r4 = fn_hack_8(["a","b"])
print(r1)
print(r2)
print(r3)
print(r4)
