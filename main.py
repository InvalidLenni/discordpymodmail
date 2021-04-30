import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='-')


def inteam(ctx):
    guild = bot.get_guild(GUILDID)
    role = bot.get_role(ROLEID)
    role in ctx.author.roles # GUILDID = The GuildID from the Support Server and RoleID is the Support RoleID.


@bot.event
async def on_ready():
    print("The Bot is now online!")


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return
    if message.author != message.author.bot:
        if not message.guild:
            guild = bot.get_guild(GUILDID) # The GuildID from the Support Server.
            channel = bot.get_guild(CHANNELID) # The ChannelID where the direct messages are sent.
            embed = discord.Embed(title="New Direct Message", description=f'Author:\n{message.author.mention}\nID:\n{message.author.id}\nMessage Cotent:\n{message.content}', color=discord.Color.green())
            embed.set_thumbnail(url=f'{message.author.avatar_url}')
            await channel.send(embed=embed)
    await bot.process_commands(message)


@bot.command()
@commands.guild_only()
@commands.cooldown(1, 15, commands.BucketType.user)
@commands.check(inteam)
async def dm(ctx, member: discord.Member, *, text):
    embed = discord.Embed(title="New Answer", description=f'Message:\n{text}', color=discord.Color.green())
    embed.set_author(url=f'{ctx.author.avatar_url}')
    await member.send(embed=embed)
    await ctx.send(f'The answer was sent to {member.id}!')


bot.run("TOKEN") # Your Bot Token