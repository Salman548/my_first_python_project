

def save_history(z, result):
    with open('calc_history.txt', 'a') as f:
        content = f'{z[0]} {z[1]} {z[2]} = {result}\n'
        f.write(content)

def show_history():
        with open('calc_history.txt', 'r') as f:
            content = f.read()
            if content == "":
                print('no history found')
            else:
                print(content)

def clear_history():
    with open('calc_history.txt', "w") as f:
        content = ""
        f.write(content)
        print('history cleared')


def calculate(z):
    if len(z) != 3:
        print('invalid input: write in this format (e.g 4 + 2): ')
    else:
        a = int(z[0])
        op = z[1]
        b = int(z[2])

        if (op == '+'):
            result = a + b
        elif (op == '-'):
            result = a - b
        elif (op == '*'):
            result = a * b
        elif (op == '/'):
            if (b == 0):
                print('cannot devide by zero')
                return
            result = a / b
        print(result)
        save_history(z, result)
  

def main():
    while True:
        i = input('Enter two numbers/history/clear/exit: ')
        z = i.split()

        if(i == 'history'):
            show_history()
        elif(i == 'clear'):
            clear_history()
        elif(i == 'exit'):
            break
        else:
            calculate(z)

main()