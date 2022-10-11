print("-----Program for printing student name with marks using list-----")
  
# бос сөздік жасаңыз
D = {}
  
n = int(input('How many student record you want to store?? '))
  
# бос тізім жасаңыз
# Оқушы туралы ақпаратты тізімге қосыңыз
ls = []
  
for i in range(0, n):
    
     # Берем комбинированное входное имя и 
 # процентные и разделенные значения 
 # использование функции разделения.
    x,y = input("Enter the student name and it's percentage: ").split()
      
    # Добавьте имя и метки, хранящиеся в x, y
# соответственно, используя кортеж, в список
    ls.append((y,x))
      
# сортировка элементов списка
# на основе меток
ls = sorted(ls, reverse = True)
  
print('Sorted list of students according to their marks in descending order')
  
for i in ls:
    
    
    print(i[1], i[0])