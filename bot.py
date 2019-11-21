import discord
from discord.ext import commands
from private_vars import token
import os
import data
import embeds
import pandas as pd

bot = commands.Bot(command_prefix="fe0?")
cd = data.load_data()

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    await bot.process_commands(msg)

@bot.command()
async def card(ctx, *, card_str):
    card = data.parse_query(card_str, cd)
    if (len(card.index) == 1):
        await ctx.send(embed=embeds.card_embed(card.iloc[0]))
    else:
        await ctx.send(embed=embeds.selection_embed(card, card_str))

@bot.command()
async def image(ctx, *, card_str):
    card = data.parse_query(card_str, cd)
    if (len(card.index) == 1):
        await ctx.send(embed=embeds.image_embed(card.iloc[0]))
    else:
        await ctx.send(embed=embeds.selection_embed(card, card_str))

@bot.command()
async def update(ctx):
    if (await bot.is_owner(ctx.author)):
        cd = data.load_data()
        await ctx.send("Data loaded!")
    else:
        await ctx.send("Message **Sivart#5017** to update the bot's data.")

#todo, override the default help function

# todo, place this externally
bot.run(token)
