def hello_ml(name=None):
    """
    A simple greeting funtion with input validation

    Args:
        name (str, optional): Name to greet
        
    Returns:
        str: Personalized greeting
    """
    
    if not name:
        return "Hello, ML Engineer!"
    return f"Hello {name}, welcome to your ML journey!"

def test_hello_ml():
    """
    Test cases for hello_ml function
    """
    assert hello_ml() == "Hello, ML Engineer!"
    assert hello_ml("Alice") == "Hello Alice, welcome to your ML journey!"
    print("All tests passed!")
    
if __name__ == "__main__":
    test_hello_ml()
    # Interactive test
    name = input("Enter your name: ")
    print(hello_ml(name))