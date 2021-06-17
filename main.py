import os
import discord 
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
  channel = await member.create_dm()
  await channel.send("You were kicked from CoderIntuition. \n " + f"Reason: {reason}")
  await member.kick(reason = reason)
  await ctx.send(f"User {member} has been kicked from this server.")

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
  channel = await member.create_dm()
  await channel.send("You were banned from CoderIntuition \n" + f"Reason: {reason}")
  await member.ban(reason = reason)
  await ctx.send(f"User {member} has been banned from this server.")

@client.command()
async def warn(ctx, member : discord.Member, *, reason = None):
  channel = await member.create_dm()
  await channel.send("You have been warned in CoderIntuition \n" + f"Reason: {reason}")
  await member.warn(reason = reason)
  await ctx.send(f"User {member} has been warned for {reason}")

client.run("ODQzNTY3NjQwMDM0NjcyNjQw.YKFvlg.L0vHOVG15kr1KvkFuMaadgS1Kms")