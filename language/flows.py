# Flows
g = 1
if g < 0:
    g = 0
    print('Negative changed to zero')
elif g == 0:
    print('Zero')
else:
    print('More')

# Loop: break & continue & else
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w)

for i in range(0, 10, 2):
    print(i)

while g < 10:
    g += 1
