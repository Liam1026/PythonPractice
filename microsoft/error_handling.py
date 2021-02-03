x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError:
    print('Not allowed  to divide by Zero')
else:
    print('Something else wnt wrong')
finally:
    print('This is our cleanup code')
