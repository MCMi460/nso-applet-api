h = {}

# Chrome headers -> Python dictionary

with open('t.txt', 'r') as file:
    l = file.read().split('\n')
    for n in range(0, len(l), 2):
        try:
            h[l[n].rstrip(':')] = l[n+1]
        except IndexError:
            break

print(h)
