items = [1,5,2,3,100,75]


n=len(items)
for i in range(n):
    for j in range(n-i-1):
        breakpoint()
        if items[j][i] > items[j+1][i]:
            items[j],items[j+1] = items[j+1] ,items[j]


print(items)

'''
#by using inbuilt function
ori_dict=eval(input())
sorted_list = sorted(ori_dict.items(), key=lambda x: x[1])  
sorted_dict = dict(sorted_list)
print(sorted_dict)'''
 



