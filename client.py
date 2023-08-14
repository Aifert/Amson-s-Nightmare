import discord
import discord.ui
import responses
from discord.ext import commands

async def send_message(message, user_message,username,is_private):
    #what is async
    try:
        response = responses.handle_response(user_message, username)
        #if it is private, then send it to the user directly 
        #else send it in the channel
        #But what does await response do?
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



def run_discord_client():
    TOKEN = '***'
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
        # positioning of the buttons very important, after changing the position of interaction and button it works well now
        async def menu1(self, interaction :discord.Interaction, Button : discord.ui.Button):
            await interaction.response.send_message(content="Hello, you have clicked the blurple button.")

        @discord.ui.button(label="Click me", style=discord.ButtonStyle.grey)
        async def menu2(self, interaction :discord.Interaction, Button : discord.ui.Button):
            await interaction.response.send_message(content="Hello, you clicked the grey button.")

        @discord.ui.button(label="Click me pls", style=discord.ButtonStyle.red)
        async def menu3(self, interaction :discord.Interaction, Button : discord.ui.Button):
            await interaction.response.send_message(content="Hello, you clicked the red button.")


    @client.tree.command(name = 'auspost')
    #button to be clicked
    async def auspost(interaction : discord.Interaction):
        view1 = Menu()
        rick_button = discord.ui.Button(label = "rick roll", url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        # amson_button = discord.ui.Button(label = "This is what amson is doing soon", url = "https://www.youtube.com/watch?v=xjkWcjeRAN4")
        auspost_label_button = discord.ui.Button(label = "Start Making Shipping Label", url = "https://auspost.com.au/mypost-business/shipping-and-tracking/orders/add/retail")
        view1.add_item(auspost_label_button)
        view1.add_item(rick_button)
        # view1.add_item(amson_button)
        await interaction.response.send_message(content = "Here's my button menu", view = view1)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {user_message} in {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, username, is_private=True)
        else:
            await send_message(message, user_message, username, is_private=False)
            
    client.run(TOKEN)






