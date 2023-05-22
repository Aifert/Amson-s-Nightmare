import random

def handle_response(message) -> str:
    #what does -> str do?
    p_message = message.lower()

    if p_message == 'hello':
        return 'hey THEREEEEE'
    
    if p_message == 'roll':
        return (f'Here is a random integer {random.randint(1,6)}')
    
    if p_message == 'easter egg':
        return ('I love anna!')
    
    if p_message == '!help':
        return "`This is a help message that you can modify.`!"
    
    if p_message == 'amson':
        str = ''
        i=0
        while i <= 10:
            str += 'AMSON IS A FUCKING IDIOT\n'
            i+=1
        return str
    
    if p_message == "suck my cock":
        return 'Holoq Holoq slurp slurp'
    
    if p_message == 'can you please tell amson to shut up':
        str = 'Yes Sure!\n' 
        i = 0
        while i <= 10:
            str += 'DIAM PLEASE\n'
            i+=1
        return str
    
    if p_message == 'describe avril':
        return f"she is a fat pig"
    
    if p_message == 'what is amson doing soon?':
        return f"eahttps://www.youtube.com/watch?v=xjkWcjeRAN4"