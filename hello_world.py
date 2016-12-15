def greet(name: str):
    print("Hello " + name)

def test_greet():
    name = 'Chris'
    greet(name)

if __name__ == '__main__':
    name = input("Please enter a name: ")
    greet(name)