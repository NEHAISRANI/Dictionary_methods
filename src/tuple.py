dict2 = {"one":1, "two":2, False:1}
print(any(dict2)) #False
print "------------"
dict3 = {False:0, True:1}
print(any(dict3)) #False
print "--------------"
empDict = {}
print(any(empDict)) #True
print "--------------"
dict1 = {"one":1, "two":2, "three":3}
print(any(dict1)) #True 
print "--------------"
dict3 = {False:1, False:2}
print(all(dict3)) #False 
print "------------"
