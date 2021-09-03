import discord
import logging
from self_chat import chatbot_response_b
from random import randint
client = discord.Client()
step=0

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global step
    if message.content.startswith('*'):
        to_send=chatbot_response_b(step=step,user=message.content)
        print(to_send)
        try:
            await message.channel.send(to_send)
        except:
            await message.channel.send("no response...")


    if message.author == client.user:
        return
    if message.content.startswith('$'):
        if message.content == '$spam':
            pass
        print(message.content)



client.run("DISCORD BOT SECRET TOKEN")
