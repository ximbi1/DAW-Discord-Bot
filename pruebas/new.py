

import discord
from discord import shard
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands.core import command
import random
from datetime import datetime
import requests   
from discord.member import Member
import discord
intents = discord.Intents.default()  
intents.members = True             
bot = commands.AutoShardedBot (shard_count=1,command_prefix ="$", intents=intents, case_insensitive=True)
api_key = "a66b910bd3c8596a07b90052435da25f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@commands.command(help="Play with .rps [your choice]")
async def rps(self,ctx):
        rpsGame = ['rock', 'paper', 'scissors']
        await ctx.send(f"rock, paper, or scissors? Choose wisely...")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

        user_choice = (await bot.wait_for('message', check=check)).content

        comp_choice = random.choice(rpsGame)
        if user_choice == 'rock':
            if comp_choice == 'rock':
                await ctx.send(f'Well, we tied. I will win next time!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Nice try, but I won!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

        elif user_choice == 'paper':
            if comp_choice == 'rock':
                await ctx.send(f'Paper beats rock. You win!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

        elif user_choice == 'scissors':
            if comp_choice == 'rock':
                await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock! Get it. ;)\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'paper':
                await ctx.send(f'Bruh. Rigged. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            elif comp_choice == 'scissors':
                await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")





@commands.command(aliases=['av'],help=" Sends a users avatar")
async def avatar(self, ctx, *,  user : discord.Member=None):
        if user == None: ##if no user is inputted
            user = ctx.author
        user = user.avatar.url
        await ctx.send(user)

    @avatar.error
    async def avatar_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f" {ctx.message.author} please mention a member!")
        else: raise(error)

    @commands.command(help="Random truth or dare")
    async def td(self,ctx):
        truth_items = ['If you could be invisible, what is the first thing you would do?',
        'If a genie granted you three wishes, what would you ask for?',
        'What is the longest you have ever slept?',
        'What animal do you think you most look like?',
        'What was your favorite childhood show?',
        'What person do you text the most?',
        'Who is your celebrity crush?',
        '']
        dare_items = ['Eat A Dry Pack Of Noodles.',
        ' Dance With No Music For 1 Minute.',
        'Give Someone Your Phone And Let Them Send One Text To Anyone In Your Contacts.',
        ' Let The Person To Your Left Draw On Your Face With A Pen.',
        'Attempt To Do A Magic Trick.',
        'Break Two Eggs On Your Head.',
        'Go Outside And Pick Exactly 40 Blades Of Grass With A Pair Of Tweezers.',
        ' Go Outside And Howl, Bark, And Meow All For 2 Minutes.',
        'Make A Sandwich While Blindfolded.']
        await ctx.send("Please type t for truth and d for dare.")
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ("t", "d")
        message = await bot.wait_for("message", check=check)
        choice = message.content.lower()
        if choice == "t":
            await ctx.send(f"{random.choice(truth_items)}")
        if choice == "d":
            await ctx.send(f"{random.choice(dare_items)}")







    @commands.command(help="Create a poll up to 9 choices")
    @commands.has_permissions(administrator=True)
    async def poll(self,ctx, *, text):
        number = {1: ":one:", 2: ":two:", 3: ":three:", 4: ":four:", 5: ":five:", 6: ":six:", 7: ":seven:", 8: ":eight:",9: ":nine:"}
        emoji = {1: "1??????", 2: "2??????", 3: "3??????", 4: "4??????", 5: "5??????", 6: "6??????", 7: "7??????", 8: "8??????", 9: "9??????"}
        count = 1
        countemoji = 1
        split = text.split('" "')
        split[-1] = split[-1].replace("\"", "")
        question = split.pop(0).replace("\"", "")
        if len(split) > 9 or len(split) < 2:
            await ctx.send("> You must have at least 2 answers and at most 9 answers.")
        else:
            descembed = "\n"
            numberRes = len(split)
            while count <= numberRes:
                descembed += number[count] + " " + split[count - 1] + "\n"
                count += 1
            embedpoll = discord.Embed(title="**" + question + ":**", description=descembed, colour=discord.Colour.random()) #You can select another colour by replacing green by another colour. For example: discord.Colour.blue() // Here's the link for the colors: https://discordpy.readthedocs.io/en/latest/api.html?#colour
            embed = await ctx.send(embed=embedpoll)
            while countemoji <= numberRes:
                await embed.add_reaction(emoji[countemoji])
                countemoji += 1
            await ctx.message.delete()
        
    @poll.error
    async def poll_error(self,ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f"`You need ADMINISTARTOR permission to use this command!`")
        else: raise(error)
