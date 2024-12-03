'''
This is a practice program to showcase collections in python 3
'''

import pprint
pp = pprint.PrettyPrinter(indent=4)



if __name__ == "__main__":

    my_list = [10, 20, 40, 60, 70]
    my_dict = {10:'Nizar', 
               20:'Basel', 
               30:'Nada'}

    # list comprehension
    print(my_list)
    print(my_list[0])
    print(len(my_list))
    # print last item
    print(my_list[len(my_list)-1])
    print(my_list[-1])
    # print a range of items in a list
    print(my_list[:3])
    print(my_list[1:4])
    # let's do dict operations
    print(my_dict)
    my_dict2 = {10:'Nizar', 
               20:'Basel', 
               30:'Nada',
               40: {1:'q',
                    2:'b',
                    3:'c',
                    4:'d'}
                }
    pp.pprint(my_dict2)
 
    # look up iems in a dict
    print(my_dict[20])
    print(my_dict2[40][2])
 
    # list comprehension
    print([i / 10 for i in my_list])
    print([i // 10 for i in my_list])
    print([my_dict[k] for k in my_dict])
 
    for item in my_list:
        try:
            print(my_dict[item])
        except KeyError:
            continue
  
 
    # more list comprehension
    my_second_list = my_list[1:4]
    print(my_second_list)
    my_list += my_second_list  # append second list to first list
    print(my_list)
 
    # list sorting      
    print(sorted(my_list))
    print(sorted(my_list, reverse=True))
    # get only unique items in the list
    print(set(my_list))
    print(sorted(set(my_list)))  # will return a list, not expected
    print(sorted(list(set(my_list))))