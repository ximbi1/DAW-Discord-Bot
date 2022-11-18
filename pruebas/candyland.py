async def candy(self, ctx):

    """Pilla el caramelo antes que nadie!"""

    embed = discord.Embed(description="🍬 | El primero que la coja se lo queda!", colour=0x0EF7E2)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🍬")

    def check(reaction, user):
        return user != self.bot.user and str(reaction.emoji) == '🍬' and reaction.message.id == msg.id

    msg0 = await self.bot.wait_for("reaction_add", check=check)

    embed.description = f"🍬 | {msg0[1].mention} ha ganado y se lo ha comido!"

    await msg.edit(embed=embed)

    with open("candylb.json", "r") as f:

        l = json.load(f)

    try:

        l[str(msg0[1].id)] += 1

    except KeyError:

        l[str(msg0[1].id)] = 1

    with open("candylb.json", "w") as f:

        json.dump(l, f, indent=4)

@client.command(aliases=["lb", "top"])
async def candyboard(self, ctx):

    """El ranking de top candelers!"""

    with open("candylb.json", "r") as f:

        l = json.load(f)

    lb = sorted(l, key=lambda x: l[x], reverse=True)
    print(lb)
    res = ""

    counter = 0

    for a in lb:

        counter += 1

        if counter > 10:

            pass

        else:

            u = self.bot.get_user(int(a))
            res += f"\n**{counter}.** `{u}` - **{l[str(a)]} 🍬**"

    embed = discord.Embed(
            description=res,
            colour=0x0EF7E2
        )
    await ctx.send(embed=embed)
