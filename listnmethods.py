l1 = [23, 23, 24, 43, "Harry"]

print(l1)
l1.remove("Harry") # it modifies the list 
l1.extend([111,323,423])
print(l1)
print(l1[0:2])
l1[0] = "changed" # So list are immutable
print(l1)