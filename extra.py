from discord.ext import commands
import datetime
import discord
import os
start_time = datetime.datetime.utcnow()

class extra(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.group(invoke_without_command=True)
  async def help(self, ctx):
      embed = discord.Embed(description=f"[Click To Add Guardian!](https://discord.com/api/oauth2/authorize?client_id=775144855663804418&permissions=8&scope=bot)")

      embed.add_field(name=f"**Categories:**", value=f"\n``— SETUP``\n``— ADMIN``\n``— FUN``\n``— IMAGE`` - coming soon\n``— SERVER``\n``— ECONOMY`` - coming soon\n``— NSFW`` - coming soon\n``— MISC``\n``— SETTINGS``\n``— OWNER`` \n\n ***>help [category]***\n ***Made with ❤️ by actavis***\n", inline=False)
      embed.set_author(name="Guardian!", url="https://discord.gg/HdjFUJG", icon_url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
      embed.set_footer(text='7 Categories | 6 Commands')

      await ctx.send(embed=embed)

  @help.command()
  async def setup(self, ctx):
      embed = discord.Embed(description=f"**Anti-Nuke Information!**")

      embed.add_field(name=f"**Categories:**", value=f"`— whitelist`\n`— unwhitelist`\n`— whitelisted`\n`— unbanall`\n`— help anti`\n", inline=False)
      embed.set_author(name="Guardian!", url="https://discord.gg/HdjFUJG", icon_url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
      embed.set_footer(text='Category: Anti-Nuke | Commands (5)')

      await ctx.send(embed=embed)
    
  @help.command(aliases = ['antiwizz'])
  async def anti(self, ctx):
  
    embed = discord.Embed()
    embed.add_field(name="**Whitelist Cmd Help:**", value="By whitelisting a user/bot your letting the user/bot able to bypsss the antinuke so they wouldn't be banned. Be Careful who you whitelist & trust.", inline=False)
    embed.add_field(name=f"**Unwhitelist Cmd Help:**", value="By unwhitelisted a user/bot your basically removing them from the bypass, therefore the user/bot aren't able to bypass the antiraid.", inline=False)
    embed.add_field(name=f"**Whitelisted Cmd Help:**", value="The whitelisted command shows every whitelisted user/bot in the exact guild.", inline=False)
    embed.add_field(name=f"**In Category:**", value="Anti-Nuke", inline=False)
    embed.add_field(name=f"**Examples:**", value="``>whitelist User/Bot``", inline=False)
    embed.add_field(name=f"``>unwhitelist User/Bot``", value="``>whitelisted``", inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
    embed.set_footer(text='For any additional help join the support server!')
    await ctx.send(embed=embed)

  @help.command()
  async def fun(self, ctx):
    embed = discord.Embed(description=f"**Fun Information!**")

    embed.add_field(name=f"**Fun Commands:**", value=f"`— kiss`\n`— tickle`\n`— hug`\n`— slap`\n`— pat`\n`— feed`\n`— pet`\n`— howgay`\n`— slots`\n`— penis`\n`— meme`\n`— cat`\n`— snipe`\n`— esnipe`\n", inline=False)
    embed.set_author(name="Protection!", url="https://discord.gg/HdjFUJG", icon_url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/773672592627597352/775776932906139658/giphy_3.gif')
    embed.set_footer(text='Category: Fun | Commands (10)')
    await ctx.send(embed=embed)
