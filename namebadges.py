# Kristen Flaherty
# Sec 01

#input name
name = input('Enter name:\n')

#create name badge text
name_badge = 'Hello, my name is '+ name

#new list variable with name badge text as item
list_item =[name_badge]

#find character length of name, which will be # of items in list
num = len(name)

#multiply list item with name badge by character-length of name
name_list = list_item * num

print(name_list)
