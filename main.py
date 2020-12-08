import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print("ready")

@client.event
async def on_message(message):
	if message.content.startswith("hi"):
        	await client.send_message(message.channel, "HI")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
