marks=[45,75,90,33,60]
pass_count=0
fail_count=0
for i in marks:
    if i>=50:
        
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1
print("The number of students passed is :" , pass_count)
print("The number of students failed is :" ,fail_count)
        