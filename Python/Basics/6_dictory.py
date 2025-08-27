# collection of key values pair
mydict = {
    "fast": "quick manner",
    "authority": " to give powe soeone",
    "marks":[1,3,5,6],
    "anotherdict": {"harry":"a coder"}
}
print(mydict['fast'])
print(mydict['marks'])
print(mydict['anotherdict'])
# nested dictory and dict are muatble can be change
print(mydict['anotherdict']['harry'])


# some functions and items give ( keys,value) of dict
print(mydict.keys())
print(list(mydict.keys()))
print(list(mydict.values()))
print((mydict.items()))

updatedict ={
    "loveish":"hello",
    "harry":"dancer"  #also update
}
mydict.update(updatedict)
print(mydict)

print(mydict.get("harry2"))  # return none but simple throw error
# print(mydict("harry2")) 