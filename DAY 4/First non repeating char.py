def first_non_repeat(string_input):
    hashmap = {}  


    for n in string_input:
        hashmap[n]=hashmap.get(n,0)+1

    for i,n in enumerate(string_input):
         if hashmap[n]==1:
            return[i,n]
    return -1   
    

string_input="ababac"
print(first_non_repeat(string_input))