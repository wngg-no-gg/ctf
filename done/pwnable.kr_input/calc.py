bytes = ""
for i in range(0, 99):
    if (i == 64):
        str += "`printf \"\\x00\"` "
    else:
        str += b"{} ".format(i)
print(str)