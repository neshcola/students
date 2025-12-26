def avg(m):
    le = 0
    for i in m:
        le += 1
    sum = 0
    for i in m:
        sum += i
    e=sum/le
    return e
mas = []

while True:
    x = input()
    if x == 'Харе!':
        break
    try:
        x = int(x)
        mas.append(x)
    except:
        print('не понял...')
result = avg(mas)
print(result)
input()    
  
    

