import discord

ROLE = "NoVerify"

client = discord.Client()

@client.event
async def on_ready():
	print(client.user.id)
	print("ready")
	game = discord.Game("Use &help Command!")
	await client.change_presence(statusdiscord.Status.Online, activity=game)

@client.event
async def on_member_join(member):
	role = get(member.guild.roles, name=ROLE)
	await member.add_roles(role)
	channel = discord.utils.get(member.guild.channels, name='환영합니다.')
	await channel.send(f'hey there, {member.mention}, welcome to my server!')

client.run("Nzg1NzczODYyNTQxMzI4Mzg0.X88u7w.UKlQx6DrBmcc5Rey9_DbVZnPOgA")