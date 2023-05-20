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
