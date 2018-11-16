from functools import wraps

def make_blink(function):
    """Defines the decorator"""

    #This makes the decorator transparet in terms of its name and docstring
    @wraps(function)
    
    #Define the inner function
    def decorator():
        #Grab the return value of the function being decorated
        ret = function()
        
        #Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

#Apply the decorator here!
@make_blink
def hello_world():
    """Original function!"""
    return "Hello, World!"

#Check the results od decorating
print(hello_world())

#Chech if the function name is still the same name of the function being decorated
print(hello_world.__name__)

#Check id the docstring is still the same as that of the function being decorated
print(hello_world.__doc__)
