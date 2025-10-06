def infix_to_postfix(infix):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}
    stack = []
    postfix = ''
    
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack:
                stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   ((precedence.get(stack[-1], 0) > precedence[char]) or
                    (precedence.get(stack[-1], 0) == precedence[char] and associativity[char] == 'left'))):
                postfix += stack.pop()
            stack.append(char)
    
    while stack:
        postfix += stack.pop()
    
    return postfix

def infix_to_prefix(infix):
    rev_infix = ''
    for char in reversed(infix):
        if char == '(':
            rev_infix += ')'
        elif char == ')':
            rev_infix += '('
        else:
            rev_infix += char
    
    prefix_rev = infix_to_postfix(rev_infix)
    prefix = prefix_rev[::-1]
    return prefix

def main():
    print("=== Conversor de Notaciones Algebraicas ===")
    infix = input("Ingrese la expresión en notación infija: ").replace(' ', '')
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar en notación INFija")
        print("2. Convertir a notación PREfija")
        print("3. Convertir a notación POSfija")
        print("4. Cambiar expresión infija")
        print("5. Salir")
        
        choice = input("Elija una opción (1-5): ").strip()
        
        if choice == '1':
            print(f"Infija: {infix}")
        elif choice == '2':
            prefix = infix_to_prefix(infix)
            print(f"Prefija: {prefix}")
        elif choice == '3':
            postfix = infix_to_postfix(infix)
            print(f"Posfija: {postfix}")
        elif choice == '4':
            infix = input("Ingrese la nueva expresión en notación infija: ").replace(' ', '')
            print(f"Expresión actualizada: {infix}")
        elif choice == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
