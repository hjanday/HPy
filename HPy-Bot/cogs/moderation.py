import discord
from discord.ext import commands
from discord.ext.commands import *
class moderation():
    def __init(self, client):
        self.client = client

    #Moderation Commands
@client.command()
async def delmsg (context, userarg):
    await context.channel.purge(limit = int(userarg))


@client.command()
async def kickuser(context, user: discord.Member, *, userarg):
    await user.kick(reason = userarg)
    await context.send(f'Kicked {user.mention}')


@client.command()
async def banuser(context, user: discord.Member, *, userarg):
    await user.ban(reason = userarg)
    await context.send(f'Banned {user.mention}')

def setup(client):
    client.add_cog(moderation(client))