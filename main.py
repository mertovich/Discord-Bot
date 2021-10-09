import discord
from discord.ext import commands
import sqlite3
from Model import DataManager

bot = commands.Bot(command_prefix='')
# MARK - bot commend
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# MARK - return user avatar
@bot.command()
async def avatar(ctx, member : discord.Member = None):
   await ctx.reply(member.avatar_url)

# MARK - return User registration date
@bot.command()
async def record(ctx, member : discord.Member = None):
    date_format = "%a, %b %d, %Y @ %I:%M %p"
    join = member.created_at.strftime(date_format)
    await ctx.reply(join)
 
# MARK - return the date the user registered on the server
@bot.command()
async def registry(ctx, member : discord.Member = None):
    date_format = "%a, %b %d, %Y @ %I:%M %p"
    join = member.joined_at.strftime(date_format)
    await ctx.reply(join)

# MARK - return Server user registration
@bot.command()
async def userRecord(ctx,*args):
    name, date, age, userId = args[0], args[1], args[2], args[3]
    DataManager.addData(name,date,age,userId)
    await ctx.reply(f'Name : {name} Date : {date} Age : {age} User Id : {userId}')

# MARK - return get user id
@bot.command()
async def getUserId(ctx,member : discord.user.User = None):
    userId = member.id
    await ctx.reply(userId)

# MARK - Shows the information of all registered users in the database
@bot.command()
async def getUserAllData(ctx):
    await ctx.reply(DataManager.getUserData())

# MARK - User id shows the matching user
@bot.command()
async def getUser(ctx,*args):
    await ctx.reply(DataManager.getUser(args[0]))

# MARK - Discord bot TOKEN
bot.run('')