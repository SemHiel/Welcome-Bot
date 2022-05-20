import datetime
import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=".", intents=intents, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching the server'))
    print('Success! Bot has launched!')
    

@client.event
async def on_member_join(member):
    channel = client.get_channel(973166560023810089)
    embed=discord.Embed(title="Welcome to The!", description=f"{member.mention} has joined the server!!", color=0xd4af37) # < Color code
    embed.set_thumbnail(url="") # thumbnail
    embed.set_footer(text='Server © 2022',icon_url="") # thumbnail Footer
    await channel.send(embed=embed)
    await member.send(f'Welcome to the Server! If you have any questions, please contact one of our staff members')
    for channel in member.guild.channels:
        if channel.name.startswith('Members:'):
            await channel.edit(name=f'Members: {member.guild.member_count}')
            break

@client.event
async def on_member_remove(member):
    channel = client.get_channel(973166560023810089)
    embed=discord.Embed(title="Thanks for your time on Server Name!", description=f"{member.mention} has left the server!", color=0xd4af37)
    embed.set_thumbnail(url="")
    embed.set_footer(text='The server © 2022',icon_url="")
    await channel.send(embed=embed)
    await member.send(f'Sad to see you leave the Discord!')
    for channel in member.guild.channels:
        if channel.name.startswith('Members: '):
            await channel.edit(name=f'Members: {member.guild.member_count}')
            break
    

client.run("token")