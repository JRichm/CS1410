

def get_valid_int(prompt: str, warning: str, low: int = None, high: int = None) -> int:
    while True:
        user_input = input(prompt)
        
        try:    
            num = int(user_input)
            
            if low is not None and num <= low:
                raise ValueError
            
            if high is not None and num >= high:
                raise ValueError
            
            return num

        except (ValueError, TypeError):
            print(warning + "\n")



def get_valid_float(prompt: str, warning: str, low: float = None, high: float = None) -> float:
    while True:
        user_input = input(prompt)
        
        try:    
            num = float(user_input)
            
            if low is not None and num <= low:
                raise ValueError
            
            if high is not None and num >= high:
                raise ValueError
            
            return num

        except (ValueError, TypeError):
            print(warning + "\n")
