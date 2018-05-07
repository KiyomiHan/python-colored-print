from colored_log import my_print, print_info, print_test, print_warn

l = [2,3,3]
dic ={
    'dict': True
}
string = 'this is string'
tup = ('p',9,';')

# customize
my_print(
    l, dic, string,'test', tup, 
    fe='red',
    bk='white', 
    dp='underline',
    sep='^',
    Time=True,
    )

print_info(l, dic, string,'test', tup)
print_warn('warn')
print_test('no time',Time=False)