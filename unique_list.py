lst=eval(input())
seen=set()
uni_list=[]

for i in lst:
    if i not in seen:
        uni_list.append(i)
        seen.add(i)
print(uni_list)