a = 5
b = 10
if a < b:
   print(f"valori iniziali: a = {a} e b = {b}") 
l = []

d = {
    'pari': [],
    'dispari': []         
}
while l:
    e = l.pop()
    if e % 2 == 0:
        d['pari'].append(e) 
print(d)        