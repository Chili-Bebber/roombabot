import discord
TOKEN = 'NTA2NjAzMjI0Mjc5Njc4OTg4.Drki5w._GYIGgKS3b5C6aKir_MFtnpvJ4Y'
client = discord.Client()
channel = {}
owner = {}
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!room '):
		print(client.get_all_channels())
		serv = message.server
		command = message.content.replace("!room ", "")

		if command.startswith('create '):
			name = command.replace("create ", "")
			if message.author not in owner:
				owner[message.author] = 1
				await client.create_channel(serv, name, type=discord.ChannelType.voice)
				cID = discord.utils.get(serv.channels, name=name, type="ChannelType.voice")
				cID = discord.utils.find(lambda c: c.name == name and c.type == 'voice', client.get_all_channels())
				channel[message.author] = name
			else:
				await client.send_message(message.channel, "Sorry, something went wrong. Maybe you already have a channel?")

		if command.startswith('destroy') and message.author in channel:
			for ch in serv.channels:
				if ch.name == channel[message.author]:
					await client.delete_channel(ch)
					del owner[message.author]
client.run(TOKEN)
