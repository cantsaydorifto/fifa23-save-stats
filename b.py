from final_data import data

for i in data:
    print("{",i["name"] , ", age: ", i["age"], ", Goals:", i["goals"] , ", Assists: ",i["assists"], ", Appearances: ",i["appearances"], ", MOTMs :", i["MOTMs"], "}")