str_ = list(input'Введите строку: ')
signs_ = list("!()-[]{};:'\',<>./?@#$%^&*_~")
symb_corr =str()
for i in str_:
    if i not in signs_:
        symb_corr += i
    else:
        continue
print(symb_corr)