# !Python string are immutable

name = "Kishan"
second_name = '''Kishan
is a good'''
print(second_name)
print(name[0:2])  # it goes from 0 to 1(2-1) Also this make a new string bcs string are immutable
print(name.upper())
print(name.isnumeric())
