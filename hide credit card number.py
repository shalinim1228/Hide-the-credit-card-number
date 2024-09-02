def cc_number(number):
    number_str = str(number)
    hidden_part = '*' * (len(number_str) - 4)
    visible_part = number_str[-4:]
    return hidden_part + visible_part


number = int(input("enter the number"))
print(cc_number(number))
