def sec_max(lst):
    breakpoint()
    max1=0
    max2=0
    lst=list(set(lst))
    for i in lst:
        if type(i) in (int,float):
            if i>max1:
                max1=i
    lst.remove(max1)
    for i in lst:
        if type(i) in (int,float):
            if i>max2:
                max2=i
    print(f'second max no from list is {max2}')
    lst.append(max1)
    print(list)

sec_max([45,66,7.5,73,102,102,102])
# def sec_max(lst):
#     uni_list=list(set(lst))
#     uni_list.sort(reverse=True)
#     print(uni_list[1])
# sec_max([45,66,7.5,102,73.5,73.51])
