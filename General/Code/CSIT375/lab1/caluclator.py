def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b
def power(a, b): return a ** b
def power10(a, b): return a ** (10*b)

operators = {  '+':lambda a,b : a+b, 
            '-':lambda a,b : a-b, 
            '*':lambda a,b : a*b,
            '/': lambda a,b : a/b,
            '**':lambda a,b : a**b,
            'e':lambda a,b : a * 10 ** b    }

def simpleCal(in_value):
    a=''
    b=''
    break_val = len(in_value) - 1

    for i in range(len(in_value)):   

        if (in_value[i].isnumeric() or in_value[i] == '.') and i < break_val:
            a += in_value[i]     

        if in_value[i] in list(operators.keys()):
            break_val = i

            for j in range(len(operators)):
                if in_value[i:i+1] == list(operators.keys())[4]:
                    operation = list(operators.values())[4]
                    operator = list(operators.keys())[4]
                    break

                elif in_value[i] == list(operators.keys())[j]:
                    operation = list(operators.values())[j]
                    operator = list(operators.keys())[j]
                    break
            
        if (in_value[i].isnumeric() or in_value[i] == '.') and i >= break_val:            
            b += in_value[i]

    return operation(float(a), float(b))

def calculation(value):

    operator_positions = []

    for x in value:
        if x in operators.keys():
            operator_positions.append(x)
    
    if len(operator_positions) == 0:
        value
        exit()

    if len(operator_positions) == 1:
        
        value = str(simpleCal(value))
        print(value)
        exit()
    
    for x in range(len(value)):
        if value[x] == ")":
            for y in range(x-1, -1, -1):
                if value[y] == "(":
                    
                    mutable_list = list(value)
                    mutable_list[y:x+1] = str(simpleCal(value[y+1:x]))
                    value = "".join(mutable_list)
                    
                    calculation(value)
            break
          
        elif value[x] == 'e' or value[x:x+1] =='**':
            for y in range(len(operator_positions)):
                if operator_positions[y] == x:
                    value[operator_positions[y-1]:operator_positions[y+1]-1] = str(simpleCal(value))
                    calculation(value)

        elif value[x] == '/' or value[x:x+1] =='*':
            for y in range(len(operator_positions)):
                if operator_positions[y] == x:
                    value[operator_positions[y-1]:operator_positions[y+1]-1] = str(simpleCal(value))
                    calculation(value)
                    
        elif value[x] == '-' or value[x:x+1] =='+':
            for y in range(len(operator_positions)):
                if operator_positions[y] == x:
                    value[operator_positions[y-1]:operator_positions[y+1]-1] = str(simpleCal(value))
                    calculation(value)
    

in_value = input()  
calculation(in_value)
