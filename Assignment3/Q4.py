result=0
dic = {1: 100 ,
       2: "Junaid",
       3: 200,
       4:"Not numerical",
       5: 50}

for value in dic.values():
    if type(value) == int or type(value) == float:
        result = result + value        
        
print(f"Sum = {result}")
