user_list = []
 
while (value := input('Enter a number: ')) != '0':
  try:
    user_list.append(int(value))
  except ValueError:
    ...  
print(*sorted(user_list), sep='\r\n')