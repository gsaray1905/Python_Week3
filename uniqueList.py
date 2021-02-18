'''Write a function that filters all 
the unique(unrepeated) elements of a given list.'''

def unique_list(list1):#defining unique_list
    list2= set(list1) # converting to set
    list3=list(list2) #converting back
    return print(list3) # return the new list

unique_list(list1=[1,2,3,3,3,3,4,5,5]) #calling the unique_list function

