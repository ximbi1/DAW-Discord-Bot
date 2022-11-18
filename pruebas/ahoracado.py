from discord.ext import commands
import discord
import random
import asyncio
class HangCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hang")
    async def ajsdlkjkasdjsaaaaa(self, ctx):
        try:
            wrongGuesses = []

            sonad = []
            with open('hangman_words.txt', 'r') as txtfile:
                for line in txtfile:
                    xline = line.strip("\n")
                    sonad.append(xline)
            ranwordd = random.choice(sonad)
            ranword = []
            print(ranwordd)
            for i in ranwordd:
                ranword.append(i)
            bury = []
            for ass in range(len(ranwordd)):
                bury.append("_")
            await ctx.send(f"This word has {len(ranwordd)} letters")
            await ctx.send("Pick a letter")
            tries = 5
            while tries > 0:

                def check(msg):
                    return msg.author == ctx.author and ctx.channel == msg.channel

                print(bury)
                msg = await self.bot.wait_for("message", check=check, timeout=60)

                c = msg.content
                if len(msg.content) != 1:
                    await ctx.send("Please only put 1 letter at a time")
                if c in ranwordd:
                    if ranwordd.count(c) >= 2:
                        indexes = [i for i, e in enumerate(ranwordd)
                                   if e == c]
                        bury[indexes[0]] = c
                        bury[indexes[1]] = c

                    await ctx.send(f'Wrong guesses: {wrongGuesses}')
                    a = ranwordd.index(c)
                    bury[a] = c
                    print(bury)
                    unbury = " ".join(bury)
                    the_final = "".join(bury)
                    print(unbury)
                    heyy = discord.Embed(title=discord.utils.escape_markdown(unbury))
                    await ctx.send(embed=heyy)
                    if the_final == ranwordd:
                        emb = discord.Embed(title="Hangman")
                        emb.add_field(name="Outcome", value="YOU WON!")
                        return await ctx.send(embed=emb)
                    else:
                        pass
                else:
                    wrongGuesses.append(c)
                    tries -= 1
                    await ctx.send(f"The letter {c} is not in the word")
                    await ctx.send(f'Wrong guesses: {wrongGuesses}')
            await ctx.send(f"You lost!\nThe word was {ranwordd}")
        except asyncio.TimeoutError:
            return await ctx.send("You took to long!")


async def setup(bot):
    await bot.add_cog(HangCog(bot))