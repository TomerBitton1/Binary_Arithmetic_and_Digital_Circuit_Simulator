from PIL import Image
#------------Flags-------------
def overflow(Result,binary_1,binary_2):
    print('\n---Flags---')
    if (binary_1[0] == binary_2[0]) and (binary_1[0] != Result[0]):
        print(' Overflow - 1')
    else:
        print(' Overflow - 0')
    
def flags(Result):
    if Result.find('1') == -1:  #Zero Flag
        print(' Zero - 1')
    else:
        print(' Zero - 0')
    if Result[0] == '1':  #Sign Flag
        print(' Sign - 1')
    else:
        print(' Sign - 0')
    if Result.count('1') % 2 == 0:  #Parity Flag
        print(' Parity - 1')
    else:
        print(' Parity - 0')

#-------Conversions functions--------
def check_bin(Input): #Check if the input is a binary number
    input_chars=set(Input)
    binary_chars={'1','0'}
    if binary_chars==input_chars or input_chars=={'0'} or input_chars=={'1'}:
        return True
    return False
    
def check_octal(Input): #Check if the input is an octal number
  for i in Input:
    if i>='8':
        return False
  return True

def check_hex(Input): #Check if the input is an hexadecimal number
    valid_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}
    uppercased_input = Input.upper()  
    for i in uppercased_input:
        if i not in valid_chars:  
            return False
    return True

def bin_to_dec(binary_number): #Convert binary to decimal
    length=len(binary_number)
    sum=0
    for i in range(length):
        sum+=int(binary_number[i])*2**(length-1-i)
    return sum

def dec_to_bin(decimal_number): #Convert decimal to binary
    binary_result = ''
    while decimal_number > 0:
        binary_result += str(decimal_number % 2)  
        decimal_number = decimal_number // 2 
    return binary_result[::-1] if  binary_result else '0'  

def bin_to_octal(binary_number): #Convert binary to octal
    length=len(binary_number)
    octal_result = ''
    for i in range(2):
        if length%3!=0:
            binary_number='0'+binary_number
            length=len(binary_number)
        else:
            break
    for i in range(0,length,3):
        octal_result+=str(bin_to_dec(binary_number[i:i+3]))
    return octal_result

def oct_to_bin(octal_number): #Convert octal to binary 
    binary_segment=''
    binary_result=''
    length=len(octal_number)
    for i in range(length):
        binary_segment=dec_to_bin(int(octal_number[i]))
        for k in range(2):
          if len(binary_segment)<3:
            binary_segment='0'+binary_segment
        binary_result+=binary_segment
    return binary_result

def bin_to_hex(binary_number): #Convert binary to hexadecimal
    length=len(binary_number)
    hex_result=''
    hex_char=''
    for i in range(3):
        if length%4!=0:
            binary_number='0'+binary_number
            length=len(binary_number)
        else:
            break
    for i in range(0,length,4):
        hex_char=str(bin_to_dec(binary_number[i:i+4]))
        if hex_char=='10':
            hex_char='A'
        elif hex_char=='11':
            hex_char='B'
        elif hex_char=='12':
            hex_char='C'
        elif hex_char=='13':
            hex_char='D'
        elif hex_char=='14':
            hex_char='E'
        elif hex_char=='15':
            hex_char='F'
        hex_result+=hex_char
    return hex_result

def hex_to_bin(hex_number):  #Convert hexadecimal to binary
    hex_number = hex_number.upper()
    length = len(hex_number)
    binary_result = ''
    for i in range(length):  
        binary_result += format(int(hex_number[i], 16), '04b')
    return binary_result

#-------Operations functions--------
def AND_op(binary_1,binary_2): #AND operation
    and_result=''
    len_1=len(binary_1)
    len_2=len(binary_2)
    if len_1<len_2:
        for i in range(len_1,len_2):
            binary_1='0'+binary_1
    elif len_1>len_2:
        for i in range(len_2,len_1):
            binary_2='0'+binary_2
    for i in range(len_1):
        and_result+=str(int(binary_1[i])*int(binary_2[i]))
    return and_result

def logical_shift(binary_number,direction): #Logical shift operation, left and right
    length =len(binary_number)
    shifted_result =''
    if direction==1: #Left
      for i in range(1,length ):
          shifted_result +=binary_number[i]
      return shifted_result +'0'
    elif direction==2: #Right
      for i in range(0,length -1): 
          shifted_result +=binary_number[i]
      return '0'+shifted_result 

def arithmetic_shift(binary_number): #Arithmetic shift right operation
    length=len(binary_number)
    s=binary_number[0] #keeping the sign
    for i in range(length-1):
        s+=binary_number[i]
    return s 

def circular_shift(binary_number,direction): #Circular shift operation, left and right.
    length=len(binary_number)
    shifted_result =''
    if direction==1: #left
       for i in range(1,length): 
         shifted_result+=binary_number[i]  
       return shifted_result +binary_number[0]
    elif direction==2: #right 
       for i in range(0,length-1): 
         shifted_result+=binary_number[i]
       return binary_number[length-1]+shifted_result 

#-----------------------MAIN----------------------- 
choice = 1
while choice!=0: #Main loop
    print('\nMain Menu','\n1.Conversions','\n2.Operations','\n3.Implementations','\n0.Exit')
    while True:
        choice = input('Hello, please type a number from the menu: ')
        if not choice.isdigit():
            print(f"'{choice}' isn't a number. Please enter a valid number.")
        elif (int(choice) < 0 or int(choice) > 3):
            print('Input Error. Please choose a number between 0 and 3.')
        else:
            choice = int(choice)
            break  

    #----------------Conversions-------------------
    if choice==0:
        print("Exiting the program. Goodbye!")
        break
    
    if choice==1:
         print('\n1.Binary to octal','\n2.Octal to binary','\n3.Binary to decimal','\n4.Decimal to binary','\n5.Binary to hexadecimal','\n6.Hexadecimal to binary','\n0.Main Menu' )
         while True:
            conversion_choice = input('What type of convert would you like to do? ')
            if not conversion_choice.isdigit():
                print(f"'{conversion_choice}' isn't a number. Please enter a valid number.")
            elif (int(conversion_choice) < 0 or int(conversion_choice) > 6):
                print('Input Error. Please choose a number between 0 and 6.')
            else:
                conversion_choice = int(conversion_choice)
                break              

         if conversion_choice==1: #Convert binary to octal
             bin=input('\nEnter a binary number to convert to an octal number: ')
             while not check_bin(bin):
                  print('Required a binary number, try again')
                  bin=input('\nEnter a binary number to convert to an octal number: ')
             print('\n Answer:','\n',bin_to_octal(bin))

         elif conversion_choice==2: #Convert octal to binary 
             while True:
              oct=input('Enter an octal number to convert to a binary number: ')
              if not oct.isdigit():
                  print(f"'{oct}' isn't a number. Please enter a valid number.") 
              elif not check_octal(oct):
                  print('Required an octal number, try again')  
              else:
                  print('\n Answer:','\n',oct_to_bin(oct))
                  break  

         elif conversion_choice==3: #Convert binary to decimal
             bin=input('\nEnter a binary number to convert to a decimal number: ')
             while not check_bin(bin):
                   print('Required a binary number, try again')
                   bin=input('\nEnter a binary number to convert to a decimal number: ')
             print('\n Answer:','\n',bin_to_dec(bin))

         elif conversion_choice==4: #Convert decimal to binary
             while True:
              dec=input('\nEnter a decimal number to convert to a binary number: ')
              if dec.startswith('-') and dec[1:].isdigit():  #Check if input is negative number
                print("Please don't enter negative numbers.")    
              elif not dec.isdigit():
                print(f"'{dec}' isn't a number. Please enter a valid number.") 
              else:
                dec=int(dec)
                print('\n Answer:','\n',dec_to_bin(dec))
                break

         elif conversion_choice==5: #Convert binary to hexadecimal
             bin=input('\nEnter a binary number to convert to a hexadecimal number: ')
             while not check_bin(bin):
                   print('Required a binary number, try again')
                   bin=input('\nEnter a binary number to convert to a hexadecimal number: ')
             print('\n Answer:','\n',bin_to_hex(bin))

         elif conversion_choice==6: #Convert hexadecimal to binary
             hex=input('\nEnter a hexadecimal number to convert to a binary number: ')
             while not check_hex(hex):
                   print('Required a hexadecimal number, try again')
                   hex=input('\nEnter a hexadecimal number to convert to a binary number: ')
             print('\n Answer:','\n',hex_to_bin(hex))
             
     #----------------Operations-------------------      
    if choice==2:  
        print('\n1.AND', '\n2.ADD', '\n3.INC', '\n4.DEC', '\n5.DIVISION', '\n6.MULTIPLY', '\n7.SHIFT','\n0.Main Menu' )
        while True:
            operation_choice = input('What type of operation would you like to do? ')
            if not operation_choice.isdigit():
                print(f"'{operation_choice}' isn't a number. Please enter a valid number.")
            elif (int(operation_choice) < 0 or int(operation_choice) > 7):
                print('Input Error. Please choose a number between 0 and 7.')
            else:
                operation_choice = int(operation_choice)
                break  

        if operation_choice == 1: #AND
            binary_1 = input('Enter the first binary number: ')
            while not check_bin(binary_1):
                print('Required a binary number, try again')
                binary_1 = input('\nEnter the first binary number: ')
            binary_2 = input('Enter the second binary number: ')
            while not check_bin(binary_2):
                print('Required a binary number, try again')
                binary_2 = input('\nEnter the second binary number: ')
            print('\n Answer:','\n',binary_1, ' and ', binary_2, '=', AND_op(binary_1, binary_2))
            print('\n---Flags---')
            flags(AND_op(binary_1, binary_2))

        elif operation_choice == 2: #ADD
            binary_1 = input('Enter a binary number: ')
            while not check_bin(binary_1):
                print('Required a binary number, try again')
                binary_1 = input('\nEnter a binary number: ')
            b = bin_to_dec(binary_1)
            binary_2 = input('Enter the binary number you would like to add: ')
            while not check_bin(binary_2):
                print('Required a binary number, try again')
                binary_2 = input('\nEnter the binary number you would like to add: ')
            d = bin_to_dec(binary_2)
            result = d + b
            print('\n Answer:','\n',binary_1, '+', binary_2, '=', dec_to_bin(result))
            overflow(dec_to_bin(result),binary_1,binary_2)
            flags(dec_to_bin(result))

        elif operation_choice == 3: #INC
            bin = input('Enter a binary number you would like to increment: ')
            while not check_bin(bin):
                print('Required a binary number, try again')
                bin = input('Enter a binary number you would like to increment: ')
            result = bin_to_dec(bin) + 1
            print('\n Answer:','\n',bin, '+ 1 =', dec_to_bin(result))
            print('\n---Flags---')
            flags(dec_to_bin(result))

        elif operation_choice == 4: #DEC
            bin = input('Enter a binary number you would like to decrement: ')
            while not check_bin(bin):
                print('Required a binary number, try again')
                bin = input('Enter a binary number you would like to decrement: ')
            if bin.find('1') == -1:
                print('\n Answer:','\n',bin, '- 1 =', '1111111111111111')
                print('\n---Flags---')
                flags('1111111111111111')
            else:    
                result = bin_to_dec(bin) - 1
                print('\n Answer:','\n',bin, '- 1 =', dec_to_bin(result))
                print('\n---Flags---')
                flags(dec_to_bin(result))

        elif operation_choice == 5: #DIVISION
            Numerator = input('Enter a binary divisible number: ')
            while not check_bin(Numerator):
                print('Required a binary number, try again')
                Numerator = input('\nEnter a binary divisible number: ')               
            denominator = input('Enter a binary dividing number: ')
            while not check_bin(denominator) or (check_bin(denominator) and denominator.find('1') == -1):  #Validate denominator
                if not check_bin(denominator):
                    print('Required a binary number, try again.')
                elif denominator.find('1') == -1:  #Checks if denominator is zero
                    print('Cannot be divided by zero, try again.')
                denominator = input('\nEnter a binary dividing number: ')            
            result = int(bin_to_dec(Numerator) / bin_to_dec(denominator))
            print('\n Answer:','\n',Numerator, '/', denominator, '=', dec_to_bin(result))
            print('\n---Flags---')
            flags(dec_to_bin(result))

        elif operation_choice == 6: #MULTIPLY
            binary_1 = input('Enter the first binary number: ')
            while not check_bin(binary_1):
                print('Required a binary number, try again')
                binary_1 = input('\nEnter the first binary number: ')
            binary_2 = input('Enter the second binary number: ')
            while not check_bin(binary_2):
                print('Required a binary number, try again')
                binary_2 = input('\nEnter the second binary number: ')
            result = bin_to_dec(binary_1) * bin_to_dec(binary_2)
            print('\n Answer:','\n',binary_1, '*', binary_2, '=', dec_to_bin(result))
            print('\n---Flags---')
            flags(dec_to_bin(result))

        elif operation_choice == 7: #SHIFT
            print('1.Arithmetic shift', '\n2.Logical shift', '\n3.Circular shift')
            shift_type = input('What shift would you like to do? ')
            while shift_type != '1' and shift_type != '2' and shift_type != '3':
                print('Input Error, try again')
                shift_type = input('What shift would you like to do? ')
            shift_type = int(shift_type)   
            
            if shift_type == 1: #Arithmetic shift
                print('\n1.A arithmetic shift left', '\n2.A arithmetic shift right')
                direction = input('Direction: ')
                while direction != '1' and direction != '2':
                    print('Input error, try again')
                    direction = input('Direction: ')
                direction = int(direction)
                binary_number = input('Enter the binary number: ')
                while not check_bin(binary_number):
                    print('Required a binary number, try again')
                    binary_number = input('\nEnter the binary number: ')   
                shift_count = input('How many shifts? ')
                while not shift_count.isdigit():
                    print('Input error, try again.')
                    shift_count = input('How many shifts? ')  
                shift_count = int(shift_count)  
                if shift_count == 0: 
                    print('\n Answer:','\n',binary_number)
                if direction == 1:  #Left
                    for i in range(0, shift_count):
                        new_binary = logical_shift(binary_number, direction) #A logical shift left
                    if new_binary[0] != binary_number[0] and shift_count != 0: #A left shift operation must be checked for overflow
                        print('\n Answer:','\n',new_binary, 'There is an overflow')
                    elif shift_count != 0:
                        print('\n Answer:','\n',new_binary) 
                elif direction == 2:  #Right
                    for i in range(0, shift_count):
                        binary_number = arithmetic_shift(binary_number)
                        print('\n Answer:','\n',binary_number)

            elif shift_type == 2: #Logical shift
                print('\n1.A logical shift left', '\n2.A logical shift right')
                direction = input('Direction: ')
                while direction != '1' and direction != '2':
                    print('Input error, try again')
                    direction = input('Direction: ')
                direction = int(direction)
                binary_number = input('Enter the binary number: ')
                while not check_bin(binary_number):
                    print('Required a binary number, try again')
                    binary_number = input('\nEnter the binary number: ')
                shift_count = input('How many shifts? ')
                while not shift_count.isdigit():
                    print('Input error, try again.')
                    shift_count = input('How many shifts? ')  
                shift_count = int(shift_count) 
                if shift_count == 0: 
                    print('\n Answer:','\n',binary_number)
                if direction == 1:  #Left
                    for i in range(0, shift_count):
                        new_binary = logical_shift(binary_number, direction) 
                    if new_binary[0] != binary_number[0] and shift_count != 0: #A left shift operation must be checked for overflow
                        print('\n Answer:','\n',new_binary, 'There is an overflow')
                    elif shift_count != 0:
                        print('\n Answer:','\n',new_binary) 
                elif direction == 2:  #Right
                    for i in range(0, shift_count):
                        binary_number = logical_shift(binary_number,direction)
                        print('\n Answer:','\n',binary_number)

            elif shift_type == 3: #Circular shift
                print('\n1.A left circular shift', '\n2.A right circular shift')
                direction = input('Direction: ')
                while direction != '1' and direction != '2':
                    print('Input error, try again')
                    direction = input('Direction: ')
                direction = int(direction)
                binary_number = input('Enter the binary number: ')
                while not check_bin(binary_number):
                    print('Required a binary number, try again')
                    binary_number = input('\nEnter the binary number: ')              
                shift_count = input('How many shifts? ')
                while not shift_count.isdigit():
                    print('Input error, try again.')
                    shift_count = input('How many shifts? ')  
                shift_count = int(shift_count)  
                if shift_count == 0: 
                    print('\n Answer:','\n',binary_number)
                for i in range(0, shift_count):
                    binary_number = circular_shift(binary_number, direction)
                    print('\n Answer:','\n',binary_number)

    #--------------------------Implementations-------------------------- 
    if choice==3:
        print('\n1.Gates','\n2.Combinational circuits','\n3.Sequential circuits','\n0.Main Menu' )
        while True:
          implementation_choice=input('What type of implement you would like to do? ')
          if not implementation_choice.isdigit():
              print(f"'{implementation_choice}' isn't a number. Please enter a valid number.")
          elif (int(implementation_choice) < 0 or int(implementation_choice) > 3):
              print('Input Error. Please choose a number between 0 and 3.')
          else:
              implementation_choice = int(implementation_choice)
              break  

        if implementation_choice == 1: #-------Gates-------
            print('\nAll gates using:', '\n1.NAND gates', '\n2.NOR gates')
            while True:
              gate_choice =input('Select type of gate to implement: ')
              if not gate_choice .isdigit():
                  print(f"'{gate_choice }' isn't a number. Please enter a valid number.")
              elif (int(gate_choice ) < 1 or int(gate_choice ) > 2):
                  print('Input Error. Please choose a number between 1 and 2.')
              else:
                  gate_choice  = int(gate_choice )
                  break  
            if gate_choice  == 1:
                img=Image.open('ALLGATES_using_NAND.jpg')
                img.show()     
            if gate_choice ==2:
                img=Image.open('ALLGATES_using_NOR.jpg')
                img.show()

        elif implementation_choice==2: #-----Combinational circuits------
            print('\n1.Half Adder','\n2.Full Adder','\n3.Half Subtractor','\n4.Full Subtractor','\n5.Multiplexer','\n6.Demultiplexer','\n7.Decoder','\n8.Encoder')
            while True:
              circuit_choice=input('Select the combinational circuit to implement: ')
              if not circuit_choice.isdigit():
                  print(f"'{circuit_choice}' isn't a number. Please enter a valid number.")
              elif (int(circuit_choice) < 1 or int(circuit_choice) > 8):
                  print('Input Error. Please choose a number between 1 and 8.')
              else:
                  circuit_choice = int(circuit_choice)
                  break  
            if circuit_choice==1: #Half Adder
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND gates','\n4.Decoder 2 to 4 & OR & NOT gates','\n5.MUX 2 & NOT gate','\n6.MUX 4')
                while True:
                  component_choice=input('Select the relevant components: ')
                  if not component_choice.isdigit():
                      print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                  elif (int(component_choice) < 1 or int(component_choice) > 6):
                      print('Input Error. Please choose a number between 1 and 6.')
                  else:
                      component_choice = int(component_choice)
                      break  
                if component_choice==1:
                    img=Image.open('HA_using_NAND.jpg')
                    img.show()                
                elif component_choice==2:
                    img=Image.open('HA_using_NOR.jpg')
                    img.show()                                    
                elif component_choice==3:
                    img=Image.open('HA_using_XOR_AND.jpg')
                    img.show()                                    
                elif component_choice==4:
                    img=Image.open('HA_using_DEC2_4.jpg')
                    img.show()                             
                elif component_choice==5:
                    img=Image.open('HA_using_MUX2.jpg')
                    img.show()                              
                elif component_choice==6: 
                    img=Image.open('HA_using_MUX4.jpg')
                    img.show()

            if circuit_choice==2: #Full Adder
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND & OR gates','\n4.Half Adder & OR gate','\n5.MUX 4 ','\n6.DEMUX 8 & OR gate')
                while True:
                  component_choice=input('Select the relevant components: ')
                  if not component_choice.isdigit():
                      print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                  elif (int(component_choice) < 1 or int(component_choice) > 6):
                      print('Input Error. Please choose a number between 1 and 6.')
                  else:
                      component_choice = int(component_choice)
                      break        
                if component_choice==1:
                    img=Image.open('FA_using_NAND.jpg')
                    img.show()              
                elif component_choice==2:
                    img=Image.open('FA_using_NOR.jpg')
                    img.show()                 
                elif component_choice==3:
                    img=Image.open('FA_using_XOR_AND_OR.jpg')
                    img.show()                  
                elif component_choice==4:
                    img=Image.open('FA_using_HA.jpg')
                    img.show()                 
                elif component_choice==5:
                    img=Image.open('FA_using_MUX4.jpg')
                    img.show()                
                elif component_choice==6: 
                    img=Image.open('FA_using_DEMUX8.jpg')
                    img.show()

            if circuit_choice==3: #Half Subtractor
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND & NOT','\n4.MUX2')
                while True:
                  component_choice=input('Select the relevant components: ')
                  if not component_choice.isdigit():
                      print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                  elif (int(component_choice) < 1 or int(component_choice) > 4):
                      print('Input Error. Please choose a number between 1 and 4.')
                  else:
                      component_choice = int(component_choice)
                      break  
                if component_choice==1:
                    img=Image.open('HS_using_NAND.jpg')
                    img.show()      
                elif component_choice==2:
                    img=Image.open('HS_using_NOR.jpg')
                    img.show()       
                elif component_choice==3:
                    img=Image.open('HS_using_XOR_AND_NOT.jpg')
                    img.show()    
                elif component_choice==4:
                    img=Image.open('HS_using_MUX2.jpg')
                    img.show()

            if circuit_choice==4: #Full Subtractor
                print('\n1.NAND gates','\n2.NOR gates','\n3.XOR & AND & OR & NOT','\n4.Half Subtractor','\n5.DEMUX8','\n6.Decoder 3 to 8')
                while True:
                  component_choice=input('Select the relevant components: ')
                  if not component_choice.isdigit():
                      print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                  elif (int(component_choice) < 1 or int(component_choice) > 6):
                      print('Input Error. Please choose a number between 1 and 6.')
                  else:
                      component_choice = int(component_choice)
                      break                  
                if component_choice==1:
                    img=Image.open('FS_using_NAND.jpg')
                    img.show()            
                elif component_choice==2:
                    img=Image.open('FS_using_NOR.jpg') 
                    img.show()                
                elif component_choice==3:
                    img=Image.open('FS_using_XOR_AND_OR_NOT.jpg')
                    img.show()               
                elif component_choice==4:
                    img=Image.open('FS_using_HS.jpg')
                    img.show()                
                elif component_choice==5:
                    img=Image.open('FS_using_DEMUX8.jpg')
                    img.show()              
                elif component_choice==6:
                    img=Image.open('FS_using_DEC3_8.jpg')
                    img.show()

            if circuit_choice==5: #MUX
                print('\n1.2 to 1','\n2.4 to 1','\n3.8 to 1','\n4.16 to 1','\n5.32 to 1')
                while True:
                  mux_choice=input('Select type of Multiplexer to implement ')
                  if not mux_choice.isdigit():
                      print(f"'{mux_choice}' isn't a number. Please enter a valid number.")
                  elif (int(mux_choice) < 1 or int(mux_choice) > 5):
                      print('Input Error. Please choose a number between 1 and 5.')
                  else:
                      mux_choice = int(mux_choice)
                      break                       
                if mux_choice==1: #MUX2
                    print('\n1.NAND gates','\n2.AND & OR & NOT gates')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 2):
                          print('Input Error. Please choose a number between 1 and 2.')
                      else:
                          component_choice = int(component_choice)
                          break                       
                    if component_choice==1:
                       img=Image.open('MUX2_using_NAND.jpg')
                       img.show()                
                    elif component_choice==2:
                       img=Image.open('MUX2_using_AND_OR_NOT.jpg') 
                       img.show()  
                       
                if mux_choice==2: #MUX4             
                    print('\n1.NAND gates','\n2.AND & OR & NOT gates','\n3.MUX2','\n4.Decoder 2 to 4')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 4):
                          print('Input Error. Please choose a number between 1 and 4.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('MUX4_using_NAND.jpg')
                       img.show()                 
                    elif component_choice==2:
                       img=Image.open('MUX4_using_AND_OR_NOT.jpg') 
                       img.show()
                    elif component_choice==3:
                       img=Image.open('MUX4_using_MUX2.jpg') 
                       img.show()         
                    elif component_choice==4:
                       img=Image.open('MUX4_using_DEC2_4.jpg') 
                       img.show()  
                       
                if mux_choice==3: #MUX8
                    print('\n1.AND & OR & NOT gates','\n2.MUX2','\n3.MUX2 & MUX4','\n4.Decoder 3 to 8')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 4):
                          print('Input Error. Please choose a number between 1 and 4.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('MUX8_using_AND_OR_NOT.jpg')
                       img.show()                  
                    elif component_choice==2:
                       img=Image.open('MUX8_using_MUX2.jpg') 
                       img.show()                    
                    elif component_choice==3:
                       img=Image.open('MUX8_using_MUX2_MUX4.jpg') 
                       img.show()                 
                    elif component_choice==4:
                       img=Image.open('MUX8_using_DEC3_8.jpg') 
                       img.show()
                       
                if mux_choice==4: #MUX16
                    print('\n1.AND & OR & NOT gates','\n2.MUX4','\n3.MUX2 & MUX8')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('MUX16_using_AND_OR_NOT.jpg')
                       img.show()                    
                    elif component_choice==2:
                       img=Image.open('MUX16_using_MUX4.jpg') 
                       img.show()                   
                    elif component_choice==3:
                       img=Image.open('MUX16_using_MUX2_MUX8.jpg') 
                       img.show() 
                       
                if mux_choice==5: #MUX32
                    print('\n1.MUX32 using MUX8')
                    img=Image.open('MUX32_using_MUX8.jpg')
                    img.show()

            if circuit_choice==6: #DEMUX
                print('\n1.1 to 2','\n2.1 to 4','\n3.1 to 8','\n4.1 to 16')
                while True:
                  demux_choice=input('Select type of Demultiplexer to implement ')
                  if not demux_choice.isdigit():
                      print(f"'{demux_choice}' isn't a number. Please enter a valid number.")
                  elif (int(demux_choice) < 1 or int(demux_choice) > 4):
                      print('Input Error. Please choose a number between 1 and 4.')
                  else:
                      demux_choice = int(demux_choice)
                      break    
                if demux_choice==1: #DEMUX2
                    print('\n1.AND & NOT gates','\n2.NAND gates','\n3.NOR gates')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('DEMUX2_using_AND_NOT.jpg') 
                       img.show()            
                    elif component_choice==2:
                       img=Image.open('DEMUX2_using_NAND.jpg') 
                       img.show()                    
                    elif component_choice==3:
                       img=Image.open('DEMUX2_using_NOR.jpg') 
                       img.show()
                       
                if demux_choice==2: #DEMUX4
                    print('\n1.NAND & NOT gates','\n2.AND & NOT gates','\n3.DEMUX2')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('DEMUX4_using_NAND_NOT.jpg')
                       img.show()                
                    elif component_choice==2:
                       img=Image.open('DEMUX4_using_AND_NOT.jpg') 
                       img.show()             
                    elif component_choice==3:
                       img=Image.open('DEMUX4_using_DEMUX2.jpg') 
                       img.show() 
                       
                if demux_choice==3: #DEMUX8
                    print('\n1.AND & NOT gates','\n2.DEMUX2','\n3.DEMUX4')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('DEMUX8_using_AND_NOT.jpg')
                       img.show()                    
                    elif component_choice==2:
                       img=Image.open('DEMUX8_using_DEMUX2.jpg') 
                       img.show()                     
                    elif component_choice==3:
                       img=Image.open('DEMUX8_using_DEMUX4.jpg') 
                       img.show() 
                       
                if demux_choice==4: #DEMUX16
                    print('\n1.AND & NOT gates','\n2.DEMUX4','\n3.DEMUX2 & DEMUX8')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('DEMUX16_using_AND_NOT.jpg')
                       img.show()                 
                    elif component_choice==2:
                       img=Image.open('DEMUX16_using_DEMUX4.jpg') 
                       img.show()                  
                    elif component_choice==3:
                       img=Image.open('DEMUX16_using_DEMUX2_DEMUX8.jpg') 
                       img.show()

            if circuit_choice==7: #DECODER
                print('\n1.1 to 2','\n2.2 to 4','\n3.3 to 8','\n4.4 to 16')
                while True:
                  decoder_choice=input('Select type of Decoder to implement: ')
                  if not decoder_choice.isdigit():
                      print(f"'{decoder_choice}' isn't a number. Please enter a valid number.")
                  elif (int(decoder_choice) < 1 or int(decoder_choice) > 4):
                      print('Input Error. Please choose a number between 1 and 4.')
                  else:
                      decoder_choice = int(decoder_choice)
                      break    
                if decoder_choice==1: #DECODER 1to2
                    print('\n1.AND & NOT gates','\n2.NAND gates')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 2):
                          print('Input Error. Please choose a number between 1 and 2.')
                      else:
                          component_choice = int(component_choice)
                          break    
                    if component_choice==1:
                       img=Image.open('DEC1_2_using_AND_NOT.jpg') 
                       img.show()                 
                    elif component_choice==2:
                       img=Image.open('DEC1_2_using_NAND.jpg') 
                       img.show()  
                       
                if decoder_choice==2: #DECODER 2to4
                    print('\n1.AND & NOT gates','\n2.NAND gates','\n3.NOR','\n4.Decoder 1 to 2')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 4):
                          print('Input Error. Please choose a number between 1 and 4.')
                      else:
                          component_choice = int(component_choice)
                          break   
                    if component_choice==1:
                       img=Image.open('DEC2_4_using_AND_NOT.jpg')
                       img.show()                 
                    elif component_choice==2:
                       img=Image.open('DEC2_4_using_NAND.jpg') 
                       img.show()              
                    elif component_choice==3:
                       img=Image.open('DEC2_4_using_NOR.jpg') 
                       img.show()                   
                    elif component_choice==4:
                       img=Image.open('DEC2_4_using_DEC1_2.jpg') 
                       img.show()  
                       
                if decoder_choice==3: #DECODER 3to8
                    print('\n1.AND & NOT gates','\n2.NAND','\n3.Decoder 2 to 4')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break   
                    if component_choice==1:
                       img=Image.open('DEC3_8_using_AND_NOT.jpg')
                       img.show()                 
                    elif component_choice==2:
                       img=Image.open('DEC3_8_using_NAND.jpg') 
                       img.show()                  
                    elif component_choice==3:
                       img=Image.open('DEC3_8_using_DEC2_4.jpg') 
                       img.show()
                       
                if decoder_choice==4: #DEMUX 4to16
                    print('\n1.AND & NOT gates','\n2.Decoder 2 to 4','\n3.Decoder 3 to 8')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 3):
                          print('Input Error. Please choose a number between 1 and 3.')
                      else:
                          component_choice = int(component_choice)
                          break   
                    if component_choice==1:
                       img=Image.open('DEC4_16_using_AND_NOT.jpg')
                       img.show()         
                    elif component_choice==2:
                       img=Image.open('DEC4_16_using_DEC2_4.jpg') 
                       img.show()                  
                    elif component_choice==3:
                       img=Image.open('DEC4_16_using_DEC3_8.jpg') 
                       img.show()

            if circuit_choice==8: #ENCODER
                print('\n1.2 to 1','\n2.4 to 2','\n3.8 to 3','\n4.16 to 4','\n5.Priority','\n6.Decimal to BCD')
                while True:
                  encoder_choice=input('Select type of Encoder to implement: ')
                  if not encoder_choice.isdigit():
                      print(f"'{encoder_choice}' isn't a number. Please enter a valid number.")
                  elif (int(encoder_choice) < 1 or int(encoder_choice) > 6):
                      print('Input Error. Please choose a number between 1 and 6.')
                  else:
                      encoder_choice = int(encoder_choice)
                      break  
                if encoder_choice==1: #ENCODER 2to1
                    img=Image.open('ENC2_1_using_OR_NOT.jpg')
                    img.show() 
                elif encoder_choice==2: #ENCODER 4to2
                    img=Image.open('ENC4_2_using_OR.jpg')
                    img.show()            
                elif encoder_choice==3: #ENCODER 8to3
                    img=Image.open('ENC8_3_using_OR.jpg')
                    img.show()     
                elif encoder_choice==4: #ENCODER 16to4 
                    img=Image.open('ENCPR16_4_using_OR.jpg')
                    img.show()               
                elif encoder_choice==5: #Priority encoder 
                    print('\n1.AND & OR & NOT gates','\n2.Priority 4 to 2')
                    while True:
                      component_choice=input('Select the relevant components: ')
                      if not component_choice.isdigit():
                          print(f"'{component_choice}' isn't a number. Please enter a valid number.")
                      elif (int(component_choice) < 1 or int(component_choice) > 2):
                          print('Input Error. Please choose a number between 1 and 2.')
                      else:
                          component_choice = int(component_choice)
                          break                                
                    if component_choice==1: 
                        img=Image.open('ENCPR4_2_using_AND_OR_NOT.jpg')
                        img.show()                      
                    elif component_choice==2:
                        img=Image.open('ENCPR8_3_using_ENCPR4_2.jpg')
                        img.show()
                elif encoder_choice==6: #Decimal to BCD
                    img=Image.open('ENC_DEC_BCD_using_OR.jpg')
                    img.show()

        elif implementation_choice==3: #-----Sequntial circuit-----
             print('\n1.Flip-flop','\n2.Binary counter','\n3.Frequency divider')
             while True:
              circuit_choice =input('Select the sequential circuit to implement: ')
              if not circuit_choice .isdigit():
                  print(f"'{circuit_choice }' isn't a number. Please enter a valid number.")
              elif (int(circuit_choice ) < 1 or int(circuit_choice ) > 3):
                  print('Input Error. Please choose a number between 1 and 3.')
              else:
                  circuit_choice  = int(circuit_choice )
                  break  
             if circuit_choice ==1: #Flip Flop
                 print('\n1.D-FF','\n2.T-FF','\n3.SR-FF','\n4.JK-FF')
                 while True:
                  flip_flop_choice=input('Select type of Flip-Flop to implement: ')
                  if not flip_flop_choice.isdigit():
                      print(f"'{flip_flop_choice}' isn't a number. Please enter a valid number.")
                  elif (int(flip_flop_choice) < 1 or int(flip_flop_choice) > 4):
                      print('Input Error. Please choose a number between 1 and 4.')
                  else:
                      flip_flop_choice = int(flip_flop_choice)
                      break  
                 if flip_flop_choice==1: #D-FF
                     img=Image.open('D.jpg')
                     img.show()               
                 elif flip_flop_choice==2: #T-FF
                     img=Image.open('T.jpg')
                     img.show()             
                 elif flip_flop_choice==3: #SR-FF
                     img=Image.open('SR.jpg')
                     img.show()         
                 elif flip_flop_choice==4: #JK-FF
                     img=Image.open('JK.jpg')
                     img.show()

             elif circuit_choice ==2: #Binary counter
                 print('\n1.Synchronous','\n2.Asynchronous')
                 while True:
                  counter_type_choice=input('Select type of 4-Bit Binary Counter to implement: ')
                  if not counter_type_choice.isdigit():
                      print(f"'{counter_type_choice}' isn't a number. Please enter a valid number.")
                  elif (int(counter_type_choice) < 1 or int(counter_type_choice) > 2):
                      print('Input Error. Please choose a number between 1 and 2.')
                  else:
                      counter_type_choice = int(counter_type_choice)
                      break             
                 if counter_type_choice==1: #SYNC
                     img=Image.open('4bit_binary_counter.jpg')
                     img.show()        
                 elif counter_type_choice==2: #ASYNC
                     img=Image.open('4bit_binary_counter_asyn.jpg')
                     img.show()

             elif circuit_choice ==3: #Frequency Divider
                 print('\n1.By even','\n2.By 3 33% D.C','\n3.By 3 50% D.C','\n4.By 3 50% D.C using NOR gates','\n5.By 5 50% D.C using NAND')
                 while True:
                  divider_choice=input('Select type of Frequency Divider to implement:  ')
                  if not divider_choice.isdigit():
                      print(f"'{divider_choice}' isn't a number. Please enter a valid number.")
                  elif (int(divider_choice) < 1 or int(divider_choice) > 5):
                      print('Input Error. Please choose a number between 1 and 5.')
                  else:
                      divider_choice = int(divider_choice)
                      break  
                 if divider_choice==1:
                     img=Image.open('FD_by_even.jpg')
                     img.show()               
                 elif divider_choice==2:
                     img=Image.open('FD_by_3_33DC.jpg')
                     img.show()      
                 elif divider_choice==3:
                     img=Image.open('FD_by_3_50DC.jpg')
                     img.show()           
                 elif divider_choice==4:
                     img=Image.open('FD_by_3_NOR_50DC.jpg')
                     img.show()         
                 elif divider_choice==5:
                     img=Image.open('FD_by_5_NAND_50DC.jpg')
                     img.show()