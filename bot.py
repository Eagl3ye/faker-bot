import discord
from discord.ext import commands
import os
import random
import asyncio

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game("with the Events | r!help"))
	print('Logged on as')
	print(client.user.name)
	print(client.user.id)


@client.command()
async def ma(ctx):
	if ctx.message.author.id == 336068309789310979:
		await ctx.send('Wished by <@487935377219256343>')
		embed = discord.Embed(
			description='**Monkey D. Luffy** \n\nOne Piece\n**565**<:kakera:748810456671453296>',
			colour=discord.Colour.green()
			)
		embed.set_image(url='https://i.imgur.com/9UVKIr1.png')
		msg = await ctx.send(embed=embed)
		await msg.add_reaction('\U0001F496')
		
		new_embed = discord.Embed(
			description='**Monkey D. Luffy** \n\nOne Piece\n**565**<:kakera:748810456671453296>',
			colour=discord.Colour.red()
			)
		new_embed.set_image(url='https://i.imgur.com/9UVKIr1.png')
		new_embed.set_footer(text='Belongs to Reinn_sama', icon_url='https://cdn.discordapp.com/avatars/487935377219256343/2656f554ae5e6ff7d703512f29414984.png')

		def check(reaction, user):
			print(str(user.id))
			id_list = [336068309789310979,487935377219256343]
			return (reaction.message.id == msg.id and user.id in id_list) #487935377219256343
		try:
			reaction, user = await client.wait_for("reaction_add", check=check, timeout=15)
		except asyncio.TimeoutError:
			print('Timeout')
		else:
			print('Rheana reacted')
			await msg.edit(embed=new_embed)
			await ctx.send('Welcome to the Kingdom of ♕ **Reinn_sama, Monkey D. Luffy**! :european_castle:')

@client.command()
async def wa(ctx):	
	if ctx.message.author.id == 336068309789310979:
		await ctx.send('Wished by <@487935377219256343>, <@336068309789310979>, <@730968136219885608>')
		embed = discord.Embed(
			description='**Origami Tobiichi** \n\nDate A Live\n**389**<:kakera:748810456671453296>',
			colour=discord.Colour.green()
			)
		embed.set_image(url='https://media.discordapp.net/attachments/472313197836107780/532751155973849088/lqVUpA2.png')
		msg = await ctx.send(embed=embed)
		await msg.add_reaction('\U0001F496')
		
		new_embed = discord.Embed(
			description='**Origami Tobiichi** \n\nDate A Live\n**389**<:kakera:748810456671453296>',
			colour=discord.Colour.red()
			)
		new_embed.set_image(url='https://media.discordapp.net/attachments/472313197836107780/532751155973849088/lqVUpA2.png')
		new_embed.set_footer(text='Belongs to Eagl3yeD', icon_url='https://cdn.discordapp.com/avatars/336068309789310979/1b55c58deb626315462eac731d5716c8.png')

		def check(reaction, user):
			print(str(user.id))
			id_list = [336068309789310979]
			return (reaction.message.id == msg.id and user.id in id_list) #487935377219256343
		try:
			reaction, user = await client.wait_for("reaction_add", check=check, timeout=15)
		except asyncio.TimeoutError:
			print('Timeout')
		else:
			print('Vince reacted')
			await msg.edit(embed=new_embed)
			await ctx.send('<:rinshoc:744158260696842291>**Origami Tobiichi** ay na sa harem na RIN ni **Eagl3yeD**<:rinshoc:744158260696842291>')

client.run(os.environ['TOKEN'])