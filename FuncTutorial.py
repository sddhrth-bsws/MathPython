#defining main determines the flow of the program
def hello(to="World"): #default parameter
    print("Hello,",to)

def main():
    hello()
    name = input("Enter the name: ")
    hello(name)

main()