g = 1
if g < 0:
    g = 0
    print('1- ', 'Negative changed to zero')
elif g == 0:
    print('1- ', 'Zero')
else:
    print('1- ', 'More')

# Loop: break & continue & else
words = ['cat', 'window', 'defenestrate']
for w in words:
    print('2- ', w)

for i in range(0, 10, 2):
    print('3- ', i)

while g < 10:
    print('4- ', g)
    g += 1
