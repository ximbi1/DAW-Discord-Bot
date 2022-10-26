import os
import datetime
import random
import aiohttp
import io
import json
import asyncio
import discord
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive
from economy import add_ppl, add_coins, remove_coins, KickCoins, leaderboard
from levelsys import add_ppllvl, add_xp, ActualLevel, leaderboardxp

status = cycle(open("status.txt", "r"))
client = commands.Bot(command_prefix=">", )
#respuestas bot
#troleo de boooooot
ls = [
    "https://tenor.com/view/minecraft-boxer-boxing-minecraft-boxer-gif-18025297",
    "https://tenor.com/view/cry-about-it-gif-22026840",
    "https://tenor.com/view/cry-about-it-gif-22562868",
    "https://tenor.com/view/we-do-a-little-trolling-we-do-a-medium-amount-of-trolling-troll-trolling-peter-griffin-gif-20853348",
    "https://tenor.com/view/troll-trolling-little-trolling-large-trolling-mass-trolling-gif-20639425",
    "https://tenor.com/view/twitter-gif-21485745",
    "https://tenor.com/view/doom-eternal-we-do-a-little-trolling-meme-shitpost-gif-20934549",
    "https://tenor.com/view/cry-about-it-cry-about-it-gif-20003018",
    "https://tenor.com/view/among-us-cry-about-it-go-cry-about-it-sussy-sussy-imposter-gif-23140749",
    "https://tenor.com/view/cry-about-it-gigachad-average-fan-vs-average-enjoyer-average-fan-average-enjoyer-gif-22029021",
    "https://tenor.com/view/cry-about-it-gif-22562868",
    "https://tenor.com/view/lol-gif-22995330",
    "https://tenor.com/view/troll-pilled-gif-19289988",
    "https://tenor.com/view/cry-about-it-madness-combat-hank-mukbang-gif-21834144",
    "https://tenor.com/view/purple-man-dancing-pixels-gif-17422304",
    "https://tenor.com/view/troll-trolled-trollge-troll-success-gif-22597471",
    "https://tenor.com/view/funny-purchase-college-barack-obama-obama-barack-obama-gif-19072900",
    "https://tenor.com/view/rat-make-out-rat-sniff-hey-do-you-want-to-make-out-do-you-want-to-make-out-gif-23560859",
    "https://tenor.com/view/turtle-animal-dance-cute-gif-8300057",
    "https://tenor.com/view/clash-royale-clash-royale-emote-gif-23858585",
    "https://tenor.com/view/cry-about-it-space-engineers-gif-24697313O",
    "https://tenor.com/view/touch-grass-touch-grass-gif-21734295",
    "https://tenor.com/view/geico-geico-commercial-geico-wood-chuck-wood-chuck-chucking-gif-16412432"
    "https://c.tenor.com/kwJ4fEC7W4IAAAAM/pvz-plants.gif",
    "https://tenor.com/view/fail-lawn-mower-dragged-gif-7931983",
    "https://tenor.com/view/no-yes-gif-23115256",
    "https://tenor.com/view/get-off-my-lawn-old-lady-sprinkler-grumpy-angry-gif-19033636",
    "https://tenor.com/view/pvz-plants-vs-zombies-plant-vs-zombie-plant-zombie-pea-gif-19750806",
    "https://c.tenor.com/WwEyrLnTpxQAAAAM/didnt-ask-didnt.gif",
    "https://media.discordapp.net/attachments/895418619666784286/928808807046451240/FE4A1361-C273-4597-BC48-D3431A35E002.gif",
    "https://tenor.com/view/troll-trollface-scary-void-scary-troll-face-gif-19777211",
    "https://www.youtube.com/watch?v=-imBnKqgKQs",
    "https://youtu.be/9eC_dmVemaw",
    "https://c.tenor.com/oSIiS53J_UMAAAAM/cat-dancing.gif",
    # 0 - 27???????? lol
]


#para trolearrrrr esta en fase desarrollooooo
@client.command()
async def troll(ctx):
    x = random.choice(ls)
    await ctx.send(x)


#respuestas del bot a sus pregu taaasss
responses = [
    "No ho sé, demanali al ximbi", "Sisisi (acaba sent que no)",
    "Això ja ho hauries de saber", "Deixa que ho busco _se'n va i no torna_",
    "Ho busques i ens ho dius després, vale?",
    "Segurament, pensa que es llei de vida", "Pueh va a ser que no, kompai",
    "La resposta la tens a les teves mans...",
    "Que fas que no estas estudiant, anda tiraa",
    "Perquè no estàs fent els deures?", "*VALE?*", "mamamela",
    "llueve albondigas"
]
insultos = [
    "¡Increíble! Realmente estás dando lo mejor de ti.",
    "Tienes una deficiencia tan grande de materia gris que seguramente flotas",
    "Te insultaría, pero luego tendría que explicarte el insulto, así que dejémoslo así",
    "Mira tu no sabes nada. De hecho, sabes menos que nada porque si supieras que no sabes nada, eso sería algo",
    "No conseguirías novia ni en un asilo de ciegas"
]
reward = 50

TaskList = []
client.author_id = 244107683475619840  # Change to your discord id!!!


#AÑADIR TAREAS
@client.command(description="para añadir tareas a la lista")
async def tarea(ctx, *args):
    output = ""
    for word in args:
        output += word
        #output += " "
    TaskList.append(output)
    await ctx.send("La tarea '" + output + "' se ha añadido a la lista!")


#para mostrar las tareas pendientes
@client.command(description="para mostrar tareas pendientees")
async def vertareas(ctx):
    await ctx.send(TaskList)


#para borrar las tareas estaria bien borrrar la que se quisiera
@client.command(description="eliminar las tareas de la lista")
async def borrartareas(ctx):
    TaskList[:] = []
    await ctx.send("Se han borrado las tareas pendientes")


#rip veremos que pasa
#@client.command()
#async def rip(ctx):
#    await ctx.message.delete()
#    channel = ctx.channel
#    randomMember = random.choice(channel.members)
#    randomMember1 = random.choice(channel.members)
#    randomMember2 = random.choice(channel.members)
#    await ctx.send(
#        f'{randomMember.mention}{randomMember1.mention}{randomMember2.mention}'
#    )
#await ctx.channel.purge(limit=1)
#    await ctx.kick(limit=1)
#    await asyncio.sleep(5)
#    await ctx.send(">rip")


@client.command(description="paara poner en negrita")
async def sup(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


#para mandar codigo
@client.command()
async def code(ctx, *, message):
    await ctx.message.delete()
    await ctx.send('```' + message + '```')


#para spam
@client.command(description="spam mejor no usar")
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
    print(f"spam cmd done")


#Adivina
@client.command(description="")
async def adivina(ctx):
    await ctx.send(
        "He pensado un numero del 1 al 1000. Tienes 10 intentos para adivinarlo"
    )
    num = random.randint(1, 1000)
    guessed = False
    i = 0
    print(num)
    while not guessed:
        if i == 10:
            await ctx.send(f"te quedaste sin intentos :'( era {num}")
            break
        try:
            msg = await ctx.bot.wait_for(
                "message",
                timeout=20,
                check=lambda message: ctx.author == message.author and message.
                channel == ctx.channel)

            if msg:
                if int(msg.content) > num:
                    await ctx.send("Mi numero és mas pequeño")
                    i += 1
                elif int(msg.content) < num:
                    await ctx.send("Mi numero és mas grande")
                    i += 1
                else:
                    await ctx.send(
                        f"¡¡¡Lo has adivinado!!!  Era {num} y lo has echo con un total de {i} intentos"
                    )
                    guessed = True
        except asyncio.TimeoutError:
            await ctx.send("Bro tardaste la vida y media")
            break


@client.command(name='meme',
                description="envia un meme divertido",
                brief="envia un meme divertido",
                aliases=[],
                pass_context=True)
async def meme(ctx, ):
    possible_responses = [
        'https://i.imgflip.com/251f7h.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEZxK3w0nw35bZwTMRBUwHh4I3-7AM_E4s7w&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfvXgAyT-ilyk_VONcE3Wlh4D2-t8OjcFzyw&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1tOhXmqBEIc__Etm68CPOrhcIu7_UBi0qQg&usqp=CAU',
        'https://i.chzbgr.com/full/9347194368/h7E289472/meme-cartoon-me-how-many-viruses-doi-have-free-anti-virus-yes',
    ]
    await ctx.send(random.choice(possible_responses))


#Shoot
@client.command(description="RULETA RUSSAAAAAAAA")
async def shoot(ctx, chamber):
    '''RULETA RUSSAAAAAAAA'''
    shoot = random.randint(1, 6)  #fail
    cowboy = ctx.author
    cowboyName = f"{cowboy}"
    if (int(chamber) <= 0) or (int(chamber) >= 7):
        await ctx.send("Elije un numero entre el 1 y el 6")
    elif shoot == int(chamber):
        await ctx.send(
            f"Españoles, {cowboyName[:-5]} ha muerto. GGWP. Ha disparado la ranura {chamber}, y la bala estaba ahí. F"
        )
        await cowboy.kick(reason="unlucky")
        try:
            await cowboy.kick(reason="unlucky")
        except discord.Forbidden:
            add_coins(ctx.author, reward)
    elif shoot != int(chamber):
        await ctx.send(
            f"{cowboyName[:-5]} ha sobrevivido. Ha disparado la ranura {chamber}, pero la bala estaba en la ranura {shoot}. Un cabron con suerte."
        )


# Ban User ojo con este que es curioso
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1
                            ) @ commands.has_permissions(administrator=True)

    await member.ban(reason=reason)
    await ctx.send(f"Baneado {member.mention}")


# UnBan User
@client.command()
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban(user)
        await ctx.send(f"Desbaneado  {user.mention}")

        return


#apuesta
@client.command(description="o apuestas o eres un noob")
async def gamble(ctx, ammount, arg=None):
    '''Apuesta tu dinero para ganar (o perder ;) )la misma cantidad '''

    if ammount == "all":
        ammount = KickCoins(ctx.author)
    else:
        ammount = int(ammount)
    if ammount <= 0:
        await ctx.send("Buen intento maquina")
        return
    if KickCoins(ctx.author) >= ammount:
        num = random.randint(1, 2)
        await ctx.send(f"Acabas de apostar {ammount} KC...")
        await asyncio.sleep(3)
        if num == 1:
            await ctx.send(f"¡¡¡Has ganado {ammount}KC!!!")
            add_coins(ctx.author, ammount)
        else:
            await ctx.send(f"Has perdido {ammount}KC :(. F")
            remove_coins(ctx.author, ammount)
    else:
        await ctx.send(
            f"No tienes tantos KC!! te faltan {ammount - KickCoins(ctx.author)}"
        )


####RALL COMMAND####para cambiar nombe del bot
@client.command(pass_context=True)
async def rall(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
            print(f"{member.name} has been renamed to {rename_to}")
        except:
            print(f"{member.name} has NOT been renamed")
        print("Action completed: Rename all")


####INFO COMMAND####
@client.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    await ctx.message.delete()
    member = ctx.message.author
    channel = ctx.message.channel
    if member is None:
        pass
    else:
        await channel.send(
            "**El nombre de usuario es: {}**".format(member.name) +
            "\n**La id d'usuario es: {}**".format(member.id) +
            "\n**El estado del miembro es: {}**".format(member.status) +
            "\n**El usuario con mayor rol es: {}**".format(member.top_role) +
            "\n**el usuario que se ha unido al discord: {}**".format(
                member.joined_at))
    print("Action completed: User Info")


#rank
@client.command()
async def rank(ctx, arg=None):
    embed = discord.Embed(title="LEADERBOARD",
                          description="the top 10 most mone pep",
                          color=0xfbff00,
                          timestamp=datetime.datetime.utcnow())
    if arg == "fekas":
        fekas = True
    else:
        fekas = False
    ricos = [
        810735914782818354, 823886106725711922, 815423482966835220,
        272021299772129281
    ]
    i = 0
    for user in leaderboard(ctx.guild):
        if not fekas:
            embed.add_field(name=f"{i+1}. {user.name}",
                            value=f"BALANCE = {KickCoins(user)}",
                            inline=False)
            i += 1
        else:
            if not user.id in ricos:
                embed.add_field(name=f"{i+1}. {user.name}",
                                value=f"BALANCE = {KickCoins(user)}",
                                inline=False)
                i += 1
        if i == 10:
            break

    await ctx.send(embed=embed)


#Transfer
@client.command()
async def transfer(ctx, coins, user: discord.Member):
    coins = int(coins)
    if coins <= 0:
        await ctx.send("Nope")
        return

    if KickCoins(ctx.author) >= coins:
        add_coins(user, coins)
        remove_coins(ctx.author, coins)
        await ctx.send("Done!")
    else:
        ctx.send(
            f"No tienes KickCoins suficientes. Te faltan {coins - KickCoins(user)}"
        )


# Kick User
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'a tu puta casa  {member.mention}')


#fuck
@client.command()
async def fuck(ctx, user: discord.Member):
    if KickCoins(ctx.author) >= 500:
        try:
            await user.kick()
            remove_coins(ctx.author, 500)
            await ctx.send(
                f"{user.name} ha sido kickeado. Se te han restado 500 KickCoins"
            )
        except discord.Forbidden:
            add_coins(ctx.author, 2000)
    else:
        await ctx.send("No tienes suficientes KickCoins. Necessitas 500")


#tax##vamoonoooooh
@client.command()
@commands.has_role("admin")
async def tax(ctx, ammount, user: discord.Member):
    if ammount == "all":
        ammount = KickCoins(user)
        remove_coins(user, ammount)
    else:
        ammount = ammount
        remove_coins(user, ammount)
        await ctx.send(f"se han restado {ammount} de tu cuenta ")


#duelo
@client.command()
async def duelo(ctx, named: discord.Member):
    '''Duel 1vs1 del oeste que a la conta de 3 qui apreti avans l'espai guanya, qui perd,es expulsat.'''
    namer = ctx.author
    if named.bot == True:
        await ctx.send("No puedes retar a bots, bakka")
        return
    await ctx.send(
        f"{named.mention}, aceptas el duelo? Tienes un minuto para responder [Escribe si para aceptar]"
    )
    try:
        msg = await ctx.bot.wait_for("message",
                                     timeout=60,
                                     check=lambda message: message.author ==
                                     named and message.channel == ctx.channel)
        if msg:
            if msg.content.lower() == "si":
                await ctx.send(
                    "Preparados? (bang para disparar. Si disparas antes de mi señal la cagas ;)"
                )
                await asyncio.sleep(2)
                await ctx.send("Listos?")
                try:
                    msg = await ctx.bot.wait_for(
                        "message",
                        timeout=random.randint(4, 10),
                        check=lambda message:
                        (message.author == named or message.author == namer)
                        and message.channel == ctx.channel and message.content.
                        lower() == "bang" and (message.author.bot == False))
                    if msg:
                        await ctx.send(
                            f"{msg.author.mention} es un noob y se ha disparado a la cabeza el muy subnormal"
                        )
                        try:
                            await msg.author.kick(reason="N00b")
                        except discord.Forbidden:
                            if msg.author == namer:
                                add_coins(named, reward)
                            else:
                                add_coins(namer, reward)
                except asyncio.TimeoutError:
                    try:
                        await ctx.send("DISPAREN!")
                        msg = await ctx.bot.wait_for(
                            "message",
                            timeout=10,
                            check=lambda message:
                            (message.author == namer or message.author == named
                             ) and message.channel == ctx.channel and message.
                            content.lower() == "bang")
                        if msg:
                            if msg.author == namer:
                                await ctx.send(
                                    f"{namer.mention} ha ganado! Que te jodan {named.mention}"
                                )
                                try:
                                    await named.kick(reason="noob")
                                except discord.Forbidden:
                                    add_coins(namer, reward)
                            else:
                                await ctx.send(
                                    f"{named.mention} ha ganado! Que te jodan {namer.mention}"
                                )
                                try:
                                    await namer.kick(reason="noob")
                                except discord.Forbidden:
                                    add_coins(named, reward)
                    except asyncio.TimeoutError:
                        await ctx.send(
                            "Estos gilipollas se han largado del duelo wtf")

    except asyncio.TimeoutError:
        await ctx.send(f"Demasiado lento {named.mention}.")


#balance
@client.command()
async def balance(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    embed = discord.Embed(title="COINS",
                          color=0x00ff33,
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="BALANCE --------->", value=":D", inline=True)
    embed.add_field(name=KickCoins(user), value=":D", inline=True)
    embed.set_footer(text=user)
    await ctx.send(embed=embed)


#Sayd
@client.command(
    description=
    "Esto es para admins, no deberias haber visto esta descripcion lol")
@commands.has_role("admin")
async def sayd(ctx, *, text):
    '''Esto es para admins, no deberias haber visto esta descripcion lol'''
    print("sayd author:", ctx.author, "Message:", text)
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{text}")


#########TRESENRALLA#######################################

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]


@client.command()
async def tresenralla(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # muestra la tabla
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determina quien va primero
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("Es el turno de <@" + str(player1.id) + "> .")
        elif num == 2:
            turn = player2
            await ctx.send("Es el turno de <@" + str(player2.id) + "> .")
    else:
        await ctx.send(
            "El juego esta en progreso!espera a que acabe para empezar otro.")


@client.command()
async def lugar(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                # muestra la tabla
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " gana!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("Es un empate!")

                # cambia turnos
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Asegurate de poner un numero entre el 1 y el 9"
                               )
        else:
            await ctx.send("No es tu turno.")



    else:
        await ctx.send("Empieza una nueva partida con >tresenralla .")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
                condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@tresenralla.error
async def tictactoe_error(ctx, error):
    print(error)


###############################################
#Si
#@client.command()
#async def si(ctx):
#    '''si'''
#    await ctx.send("si")

#no
#@client.command()
#async def no(ctx):
#    '''si'''
#    await ctx.send("no es no")


@client.event
async def on_ready():  # When the bot is ready
    print("estamos listos chicos")
    print(client.user)  # Prints the bot's username and identifier


extensions = [
    'cogs.cog_example'  # Same name as it would be if you were importing it
]


################FUNCTIONS###################
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def all_accounts(server):
    for user in server.users:
        add_ppl(user)


def all_accounts_level(server):
    for user in server.users:
        add_ppllvl(user)


###################EVENTS###################
#BotStartup
@client.event
async def on_ready():
    change_status.start()
    print("Marible is Ready to kick ass")


#MemberJoin log and Auto Permisos
@client.event
async def on_member_join(member):
    print(f"{member} ha entrado al servidor")
    await CFUE(member, member.avatar_url, "Se a unido al server")
    rank = discord.utils.get(member.guild.roles, name="Admin")
    await member.add_roles(rank)
    print(f"{member} was given the {rank} role.")


#MemberRemove log
async def CFUE(NAME, AVATAR, WHAT):
    channelID = client.get_channel(831127435189157908)
    embed = discord.Embed(title=f"{NAME}",
                          color=0x00ff2a,
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=AVATAR)
    embed.add_field(name=f"{WHAT}", value="PARADOX se aburre", inline=True)
    embed.set_footer(text="F")
    await channelID.send(embed=embed)


@client.event
async def on_member_remove(member):
    print(f"{member} c fue")
    await CFUE(member, member.avatar_url, "Se a ido a la puta")


####################LOOPS###################
#Status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


###################COMMANDS#################
#SUMAR
@client.command()
async def sumar(ctx, numOne: int, numTwo: int):
    await ctx.send(f"The result is: {numOne + numTwo}")


#restar
@client.command()
async def restar(ctx, numOne: int, numTwo: int):
    await ctx.send(f"The result is: {numOne - numTwo}")


#divide
@client.command()
async def divide(ctx, numOne: int, numTwo: int):
    await ctx.send(f"The result is: {numOne / numTwo}")


#multiplica
@client.command()
async def multiplica(ctx, numOne: int, numTwo: int):
    await ctx.send(f"The result is: {numOne * numTwo}")


#Clear
@client.command(
    description="Clears the amount of messages specified (default = 1)")
@commands.has_role("admin")
async def clear(ctx, amount=1):
    '''Clears the amount of messages specified (default = 1)'''
    print(ctx.author, "has cleared", amount, "messages")
    await ctx.channel.purge(limit=amount + 1)


#Ping
@client.command(description="Pingea al bot y devuelve pong y los ms")
async def ping(ctx):
    '''Pingea al bot y devuelve pong y los ms'''
    await ctx.send(f"Pong! ({int(client.latency * 1000)}ms)")


#mejor no lo abras xd F POR BLAI XD
@client.command()
async def sorpresa(ctx):
    embed = discord.Embed(
        title="regalito zip",
        url="https://www.bamsoftware.com/hacks/zipbomb/zbxl.zip")
    await ctx.send(embed=embed)


####################LEVEL SYSTEM ######################


async def levelupembed(NAME, LEVEL):
    channelID = client.get_channel(831671210386522183)
    embed = discord.Embed(title="HAS SUBIDO DE NIVEL!",
                          color=0xffee00,
                          timestamp=datetime.datetime.utcnow())
    embed.set_author(name=f"{NAME}")
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/816638769818107924/831670376789573642/aa02d477025b498c0e6a462c5c156f29.gif"
    )
    embed.add_field(name="nivel", value=f"{LEVEL}", inline=False)

    await channelID.send(embed=embed)


@client.command()
async def level(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    embed = discord.Embed(title="Level",
                          color=0x006eff,
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Your level --------->", value="Real XP", inline=True)
    embed.add_field(name=int(ActualLevel(user) / 100),
                    value=ActualLevel(user),
                    inline=True)
    embed.set_footer(text=user)
    await ctx.send(embed=embed)


@client.command()
async def levelboard(ctx, arg=None):
    embed = discord.Embed(title="LEADERBOARD",
                          description="the top 10 level",
                          color=0x006eff,
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/attachments/816638769818107924/831596236687015936/dd27nmj-26102f1f-2fda-446a-b69a-b26a48e2ab10.gif"
    )
    if arg == "bots":
        bots = True
    else:
        bots = False
    justbots = [815423482966835220, 823886106725711922, 234395307759108106]
    i = 0
    for user in leaderboardxp(ctx.guild):
        if not bots:
            if not user.id in justbots:
                embed.add_field(name=f"{i+1}. {user.name}",
                                value=f"Level = {int(ActualLevel(user)/100)}",
                                inline=False)
                i += 1
        else:
            embed.add_field(name=f"{i+1}. {user.name}",
                            value=f"Level  = {int(ActualLevel(user)/100)}",
                            inline=False)
            i += 1
        if i == 10:
            break

    await ctx.send(embed=embed)


@client.command()
async def DESPIERTA(ctx):
    await ctx.send(f"BUENOS DIAS ({round(client.latency*1000)}ms)")


##insultator
@client.command(description="El educado bot te va a insultar",
                aliases=["r/insulto"])
async def insultame(ctx, *, question):
    '''le dices algo y te va a devolver el insulto'''
    respost = random.choice(insultos)
    await ctx.send(f"Resposta: {respost}")


#AskMarible
@client.command(description="Le haces una pregunta al bot",
                aliases=["r/pregunta"])
async def pregunta(ctx, *, question):
    '''Le haces una pregunta a Marible'''
    resposta = random.choice(responses)
    await ctx.send(f"Resposta: {resposta}")


####


#Coinflip
@client.command()
async def coinflip(ctx, user: discord.Member):
    await ctx.send(
        f"{user.mention} has sido retado a un coinflip. Escribe si para aceptar. Tienes un minuto"
    )
    try:
        msg = await ctx.bot.wait_for("message",
                                     timeout=60,
                                     check=lambda message: message.author ==
                                     user and message.channel == ctx.channel)
        if msg:
            if msg.content == "dale" or msg.content == "si" or msg.content == "Si":
                result = random.randint(1, 4)
                if result == 2:
                    await ctx.send("INCREIBLE, LA MONEDA HA CAIDO DE LADO")
                    await asyncio.sleep(2)
                    await ctx.send("Tecnicamente...")
                    await asyncio.sleep(2)
                    await ctx.send("se ven las dos caras...")
                    await asyncio.sleep(2)
                    await ctx.send("Adios a los dos ;)")
                    await ctx.author.kick()
                    await user.kick()
                #si sale mas peque de dos ml
                elif result > 2:
                    await ctx.send(
                        f"{ctx.author.mention}, las cosas no pintan muy bien para ti..."
                    )
                    await asyncio.sleep(random.randint(0, 3))
                    await ctx.send("Chao!")
                    try:
                        await ctx.author.kick()
                    except discord.Forbidden:
                        add_coins(user, reward)
                    #si sale mas peque de dos ml
                else:
                    await ctx.send(
                        f"{user.mention}, las cosas no pintan muy bien par ti..."
                    )
                    await asyncio.sleep(random.randint(0, 3))
                    await ctx.send("Chao")
                    try:
                        await user.kick()
                    except discord.Forbidden:
                        add_coins(ctx.author, reward)
            else:
                await ctx.send("f")

    except asyncio.TimeoutError:
        await ctx.send("nah de locos")


#Say
@client.command(description="Haces que el bot diga algo")
async def say(ctx, *, text):
    '''Haces que el bot diga algo'''
    print("say author:", ctx.author, "Message:", text)
    await ctx.send(f"{text}")


########
#Lee
@client.command(description="beemovie.txt")
@commands.has_role("admin")
async def lee(ctx):
    '''beemovie.txt'''
    stopper.stoped = False
    f = open("beemovie.txt", "r")
    for word in f:
        await ctx.send(word, tts=True)
        if stopper.stopped == True:
            break
    try:
        msg = await ctx.bot.wait_for(
            "message",
            check=lambda message:
            (message.author.id == 244107683475619840 or message.author.id ==
             1032594817022177310) and message.channel == ctx.channel)
        if msg:
            #if msg.content == "stop":
            print("stopping")
            stopper.stopped = True

    except asyncio.TimeoutError:
        await ctx.send("Este mensaje no deberia verse.")


class stopper:
    stopped = False


#############################################SEGUNDA PARTE DEL BOT#################################3ç

#TIENDA DE COMPRA DE COSAS
mainshop = [{
    "nombre": "esclavo",
    "precio": 0,
    "descripcion": "regalau"
}, {
    "nombre": "Rolex",
    "precio": 1000,
    "descripcion": "Hi-Class"
}, {
    "nombre": "KgMaria",
    "precio": 900,
    "descripcion": "Good Life"
}, {
    "nombre": "MacBook",
    "precio": 1500,
    "descripcion": "Trabajo"
}, {
    "nombre": "PCUltra",
    "precio": 5000,
    "descripcion": "Gaming"
}, {
    "nombre": "Ferrari",
    "precio": 1000000,
    "descripcion": "Cochazo"
}, {
    "nombre": "resortPrivado",
    "precio": 1709900,
    "descripcion": "Lujazo"
}, {
    "nombre": "Bugatti",
    "precio": 12500800,
    "descripcion": "Cochazo"
}, {
    "nombre": "jetPrivado",
    "precio": 40700000,
    "descripcion": "Viajes rapidos"
}, {
    "nombre": "DiamanteAzul",
    "precio": 48390000,
    "descripcion": "Luna azul"
}, {
    "nombre": "Ferrari_250_GTO",
    "precio": 70000000,
    "descripcion": "Classico 1963 39Uni"
}, {
    "nombre": "islaPrivada",
    "precio": 412600500,
    "descripcion": "Vida de ricos"
}, {
    "nombre": "YateSupreme",
    "precio": 4800000000,
    "descripcion": "10.900kg chapado de Oro18k"
}, {
    "nombre": "Estacion_Espacial",
    "precio": 8900000000,
    "descripcion": "NASA member"
}, {
    "nombre": "Antimateria",
    "precio": 100000000000000,
    "descripcion": "Gramo potensia"
}]


#big pot con el dinero que se usa al comprar
#BALANCE DE DINERO EFECTIVO Y DEL BANCO
@client.command(aliases=['bal'])
async def balanse(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f'{ctx.author.name} Balance',
                       color=discord.Color.red())
    em.add_field(name="Dinero en la cartera", value=wallet_amt)
    em.add_field(name='Dinero en el banco', value=bank_amt)
    await ctx.send(embed=em)


#SOLICITAR DINERO EN EL BANCO
@client.command()
async def soli(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'{ctx.author.mention} Has conseguido {earnings} coins!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json", 'w') as f:
        json.dump(users, f)


#RETIRAR DINERO DEL BANCO Y PINERLO EN LA CARTRRA
@client.command(aliases=['rt'])
async def retirar(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Porfavor pon la cantidad a retirar: ")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[1]:
        await ctx.send('No dispones de suficientes coins')
        return
    if amount < 0:
        await ctx.send('El numero debe ser positivo!')
        return

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1 * amount, 'bank')
    await ctx.send(f'{ctx.author.mention} Has retirado {amount} coins')


#DEPOSITAR DINERO EN EL BANCO DE LA CARTERA
@client.command(aliases=['dp'])
async def deposit(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Porfavor pon la cantidad a depositar")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('No dispones de suficientes coins')
        return
    if amount < 0:
        await ctx.send('El numero debe de ser positivo!')
        return

    await update_bank(ctx.author, -1 * amount)
    await update_bank(ctx.author, amount, 'bank')
    await ctx.send(f'{ctx.author.mention} Has depositado {amount} coins')


#ENVIAR DINERO A OTRA PERSONA
@client.command(aliases=['en'])
async def enviar(ctx, member: discord.Member, amount=None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        await ctx.send("Porfavor especifica una cantidad")
        return

    bal = await update_bank(ctx.author)
    if amount == 'all':
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('No tienes suficiente dinero en la cuenta')
        return
    if amount < 0:
        await ctx.send('La cifra debe ser positiva!')
        return

    await update_bank(ctx.author, -1 * amount, 'bank')
    await update_bank(member, amount, 'bank')
    await ctx.send(
        f'{ctx.author.mention} Has enviado a {member} {amount} coins')


#robar coinss a los demas
@client.command(aliases=['rb'])
async def robar(ctx, member: discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    bal = await update_bank(member)

    if bal[0] < 100:
        await ctx.send('Es inutil robarle :(')
        return

    earning = random.randrange(0, bal[0])

    await update_bank(ctx.author, earning)
    await update_bank(member, -1 * earning)
    await ctx.send(
        f'{ctx.author.mention} Le has robado a {member} y has conseguido {earning} coins'
    )


#MAQUINAS TRAGAPERRASSSSS editar para poner mas cantidad de numeros
@client.command()
async def slots(ctx, amount=None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Porfavor especifica una cantidad. ")
        return

    bal = await update_bank(ctx.author)

    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('No dispones de suficiente dinero en la cuenta')
        return
    if amount < 0:
        await ctx.send('La cantidad debe ser positiva!')
        return
    final = []
    for i in range(3):
        a = random.choice(['💎', '💸', '💰'])

        final.append(a)

    await ctx.send(str(final))
    #modificar esta parte para que no este tan roto
    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        await update_bank(ctx.author, 1.5 * amount)
        await ctx.send(
            f'Asi me gusta campeon haciendo moneyy :) {ctx.author.mention}')
#    if final[0] == final[1] and final[1] == final[2] and #final[0] == final[2]:
#        await update_bank(ctx.author,2*amount)
#        await ctx.send(f'Enhorabuena! las clavado! sigue asi #{ctx.author.mention}')
    else:
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f'Has perdido :( {ctx.author.mention}')


#TIENDA PARA COMPRAR OBJETOSSS
@client.command()
async def tienda(ctx):
    em = discord.Embed(title="Tienda exclusiva")

    for item in mainshop:
        name = item["nombre"]
        price = item["precio"]
        desc = item["descripcion"]
        em.add_field(name=name, value=f" ${price} | {desc} ")

    await ctx.send(embed=em)


#PARA COMPRAR EN LA TIENDA
@client.command()
async def comprar(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await comprar_esto(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("Este objeto no esta aqui!")
            return
        if res[1] == 2:
            await ctx.send(
                f"No tienes suficiente dinero en la cartera para comprar esto.. {amount} {item}"
            )
            return

    await ctx.send(f"Acabas de comprar {amount} {item}")


#BOLSA DE OBJETOS
@client.command()
async def bienes(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []

    em = discord.Embed(title="Bienes Personales")
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name=name, value=amount)

    await ctx.send(embed=em)


async def comprar_esto(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["nombre"].lower()
        if name == item_name:
            name_ = name
            price = item["precio"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0] < cost:
        return [False, 2]

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["bag"] = [obj]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost * -1, "wallet")

    return [True, "Worked"]


##VENDER OBJETOS COMPRADOS
@client.command()
async def vender(ctx, item, amount=1):
    await open_account(ctx.author)

    res = await vender_esto(ctx.author, item, amount)

    if not res[0]:
        if res[1] == 1:
            await ctx.send("Este objeto no se encuentra aqui!")
            return
        if res[1] == 2:
            await ctx.send(f"No tienes {amount} {item} en tus bienes.")
            return
        if res[1] == 3:
            await ctx.send(f"No tienes {item} en tus bienes.")
            return

    await ctx.send(f"Acabas de vender {amount} {item}.")


#definicion vende esto
async def vender_esto(user, item_name, amount, price=None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["nombre"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.7 * item["precio"]
            break

    if name_ == None:
        return [False, 1]

    cost = price * amount

    users = await get_bank_data()

    bal = await update_bank(user)

    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False, 2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    await update_bank(user, cost, "wallet")

    return [True, "Worked"]


@client.command(aliases=["lb"])
async def monopolio(ctx, x=1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(
        title=f"Top {x} Gente mas Rica",
        description="Eso se decide con el total de la cartera y el banco",
        color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed=em)


#para abrir una cuenta de banco
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)

    return True


#para coger ata del banco
async def get_bank_data():
    with open('mainbank.json', 'r') as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode='wallet'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('mainbank.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['wallet'], users[str(user.id)]['bank']
    return bal


########

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        client.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)  # Starts the bot
