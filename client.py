import discord
import discord.ui
import responses
from discord.ext import commands

async def send_message(message, user_message, is_private):
    #what is async
    try:
        response = responses.handle_response(user_message)
        #if it is private, then send it to the user directly 
        #else send it in the channel
        #But what does await response do?
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



def run_discord_client():
    TOKEN = 'MTEwOTMzNDE2NzEzODg2NTIxNA.G0TbEh.8tEytxkuWSNGz9ZkS37prb0uropJSKqtO0EsQQ'
    #what is discord.client
    #what are intents
    client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())
    
    @client.event
    async def on_ready():
        #what does this mean? (client.tree.sync)
        await client.tree.sync()
        print(f'{client.user} is running')

    class Menu(discord.ui.View):
        def __init__(self):
            super().__init__()

        @discord.ui.button(label="Send Message", style=discord.ButtonStyle.blurple)
        #positioning of the buttons very important, after changing the position of interaction and button it works well now
        async def menu1(self, interaction :discord.Interaction, Button : discord.ui.Button):
            await interaction.response.send_message(content="Hello, you have clicked the blurple button.")

        @discord.ui.button(label="Click me", style=discord.ButtonStyle.grey)
        async def menu2(self, interaction :discord.Interaction, Button : discord.ui.Button):
            await interaction.response.send_message(content="Hello, you clicked the grey button.")

        @discord.ui.button(label="Click me pls", style=discord.ButtonStyle.red)
        async def menu3(self, interaction :discord.Interaction, Button : discord.ui.Button):
            await interaction.response.send_message(content="Hello, you clicked the red button.")


    @client.tree.command(name = 'buttonmenu')
    #button to be clicked
    async def buttonmenu(interaction : discord.Interaction):
        await interaction.response.send_message(content = "Here's my button menu", view = Menu())

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {message} in {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
    @client.event        
    async def doSomething(action):
        print("hello world")

    @client.event
    async def makeSomething(action):
        print("do something pls")

    client.run(TOKEN)






