import random

def handle_response(message, username) -> str:
    #what does -> str do?
    p_message = message.lower()

    if p_message == 'hello':
        return f'hey THEREEEEE @{username}'
    
    if p_message == 'roll':
        return (f'Here is a random integer {random.randint(1,6)}')
    
    if p_message == 'easter egg':
        return ('I love anna!')
    
    if p_message == '!help':
        return "`This is a help message that you can modify.`!"
    
    if p_message == 'amson':
        str = 'I will now show you WHAT is amson\n'
        i=0
        count = 0
        while i <= 10:
            count += 1
            str += 'AMSON IS A FUCKING IDIOT\n'
            str += (f'This is me saying amson is fucking dumb {count} time\n')
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
        return f"https://www.youtube.com/watch?v=xjkWcjeRAN4"
    
    if p_message == 'good morning':
        return f"Heres ur cup of coffee daddy, have a good day - Jamie"
    
    if p_message == 'where is amson now?':
        return f'PRISON PRISON PRISON PRISON PRISON'