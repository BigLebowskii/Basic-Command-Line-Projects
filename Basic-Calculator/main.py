from art import logo
from replit import clear
print(logo)


def add(n1, n2):
  return n1 + n2
  
def subtract(n1, n2):
  return n1 - n2
  
def multiply(n1, n2):
  return n1 * n2
  
def divide(n1, n2):
  return n1 / n2

operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}
def calculation():
    n1 = float(input("Enter the first number: "))
    op_symbol = input("Enter an operator:  ")
    n2= float(input("Enter the second number: "))
    answer = operations[op_symbol](n1,n2)
    print(f"{n1} {op_symbol} {n2} = {answer} ")
    restart = True

  
    while restart:
      start = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'exit' to exit the program: ")
      if start == 'y':
        op_symbol = input("Pick the next operator: ")
        n3 = float(input("Pick another number: "))
        second_answer = (operations[op_symbol](answer,n3))
        print(f"{answer} {op_symbol} {n3} = {second_answer} ")
        answer = second_answer
      elif start == 'n':
        clear()
        calculation()
      else:
        restart = False
        clear()
calculation()