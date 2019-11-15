menu = {}
menu['1']="add" 
menu['2']="subtract"
menu['3']="multiply"
menu['4']="divide"
menu['5']="modulus"
while True: 
  options=menu.keys()
  options.sort()
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("Please Select:") 
    if selection =='1': 
      print "add" 
    elif selection == '2': 
      print "subtract"
    elif selection == '3':
      print "multiply" 
    elif selection == '4': 
      print "divide"
    elif selection == '5':
      print "modulus"
    else: 
      print "Unknown Option Selected!" 
