"""String to Integer (atoi)
   Explanation: Parse with sign and bounds.
   Example: '-42' → -42
   """

def atoi(s):
    if not s:
        return
    neg = True if s[0] == '-' else False
    if neg:
        s = s[1:] 
    
    i = int(s)

    return i if not neg else -i