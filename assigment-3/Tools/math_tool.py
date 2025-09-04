from agents import function_tool

@function_tool
def plus(n1:int,n2:int) -> str:
    """
    function for plus
    args:
        n1:int
        n2:int
    return str    
    """
    return f"Your answer is.... {n1 + n2}"

@function_tool
def multiply(n1:int,n2:int) -> str:
    """
    function for multiply
    args:
        n1:int
        n2:int
    return str    
    """
    return f"Your answer is... {n1 * n2}"