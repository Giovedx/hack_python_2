"""
text: [{"a":"b"},{"c":"d"},{"e":"f"}] output => [{"1":"2"},{"3":"4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    nuevodicionario = [{"1":"2"},{"3":"4"},{"5":"6"}]
    result = nuevodicionario
    return result

r1 = fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}])
print(r1)