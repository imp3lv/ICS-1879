import telephone

t = telephone.Telephone('0501234567', 'Samsung')

t.Call('Олег', '0671112233')
t.Call('Марія', '0937778899')
print(t.calls)

t.DeleteCall()
print(t.calls)
