import os
import datetime
import random
#####opcional####

###################
import aiohttp
import io
import utils
from random import randint, sample, shuffle
from collections import defaultdict
import pyfiglet
import json
import numpy as np
from warnings import filterwarnings
from typing import Optional
import time
import re
from replit import db
from game import *
import time
filterwarnings("ignore", category=np.VisibleDeprecationWarning)
from urllib.parse import quote
from translate import Translator
import asyncio
import requests, urllib.parse, random, json, base64, asyncio
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
################PARTE PARA el RPG####################
# Helper functions
def load_character(user_id):
    return Character(**db["personajes"][str(user_id)])


MODE_COLOR = {
    GameMode.BATTLE: 0xDC143C,
    GameMode.ADVENTURE: 0x005EB8,
}


def status_embed(ctx, character):

    # Current mode
    if character.mode == GameMode.BATTLE:
        mode_text = f"Actualmente luchando contra  {character.battling.name}."
    elif character.mode == GameMode.ADVENTURE:
        mode_text = "Actualmente de aventura."

    # Create embed with description as current mode
    embed = discord.Embed(title=f"{character.name} estado",
                          description=mode_text,
                          color=MODE_COLOR[character.mode])
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)

    # Stats field
    _, xp_needed = character.ready_to_level_up()

    embed.add_field(name="Estadisticas",
                    value=f"""
**HP:**    {character.hp}/{character.max_hp}
**ATAQUE:**   {character.attack}
**DEFENSA:**   {character.defense}
**MANA:**  {character.mana}
**NIVEL:** {character.level}
**XP:**    {character.xp}/{character.xp+xp_needed}
    """,
                    inline=True)

    # Inventory field
    inventory_text = f"Oro: {character.gold}\n"
    if character.inventory:
        inventory_text += "\n".join(character.inventory)

    embed.add_field(name="Inventario", value=inventory_text, inline=True)

    return embed
  # Commands
@client.command(name="crear", help="Crea un personaje.")
async def crear(ctx, name=None):
    user_id = ctx.message.author.id

    # if no name is specified, use the creator's nickname
    if not name:
        name = ctx.message.author.name

    # create personajes dictionary if it does not exist
    if "personajes" not in db.keys():
        db["personajes"] = {}

    # only create a new character if the user does not already have one
    if user_id not in db["personajes"] or not db["personajes"][user_id]:
        character = Character(
            **{
                "name": name,
                "hp": 16,
                "max_hp": 16,
                "attack": 2,
                "defense": 1,
                "mana": 0,
                "level": 1,
                "xp": 0,
                "gold": 0,
                "inventory": [],
                "mode": GameMode.ADVENTURE,
                "battling": None,
                "user_id": user_id
            })
        character.save_to_db()
        await ctx.message.reply(
            f"Nuevo personaje de nivel 1 creadod: {name}. Escribe `>statusp` para ver tus estadisticas."
        )
    else:
        await ctx.message.reply("ya has creado tu personaje.")


@client.command(name="statusp", help="Para ver informacion de tu personaje.")
async def statusp(ctx):
    character = load_character(ctx.message.author.id)

    embed = status_embed(ctx, character)
    await ctx.message.reply(embed=embed)


@client.command(name="cazar", help="Busca un enemigo para luchar.")
async def cazar(ctx):
    character = load_character(ctx.message.author.id)

    if character.mode != GameMode.ADVENTURE:
        await ctx.message.reply("Solo puedes ejecutar este comando fuera de peleas!"
                                )
        return

    enemy = character.hunt()

    # Send reply
    await ctx.message.reply(
        f"Te has encontrado a {enemy.name}. Quieres `>luchar` or `>huir`?")


@client.command(name="luchar", help="Luchas con la criatura.")
async def luchar(ctx):
    character = load_character(ctx.message.author.id)

    if character.mode != GameMode.BATTLE:
        await ctx.message.reply("solo puedes ejecutar este comando en un encuentro!")
        return

    # Simulate battle
    enemy = character.battling

    # Character attacks
    damage, killed = character.fight(enemy)
    if damage:
        await ctx.message.reply(
            f"{character.name} ataco {enemy.name}, infingiendo {damage} de daño!")
    else:
        await ctx.message.reply(
            f"{character.name} Intento atacar a {enemy.name}, pero ha fallado!")

    # End battle in victory if enemy killed
    if killed:
        xp, gold, ready_to_level_up = character.defeat(enemy)

        await ctx.message.reply(
            f"{character.name} ha liquidao a {enemy.name}, consiguiendo {xp} XP y {gold} de Oro. HP: {character.hp}/{character.max_hp}."
        )

        if ready_to_level_up:
            await ctx.message.reply(
                f"{character.name} Ha conseguido suficiente experiencia como para subir a nivel {character.level+1}. Escribe `>subirnivel` con la estadistica (HP, ATTACK, DEFENSE) Que quieres mejorar. ejemplo `>subirnivel hp` o `>subirnivel attack`."
            )

        return

    # Enemy attacks
    damage, killed = enemy.fight(character)
    if damage:
        await ctx.message.reply(
            f"{enemy.name} ataco a {character.name}, infingiendo {damage} de daño!")
    else:
        await ctx.message.reply(
            f"{enemy.name} intento atacar a {character.name}, pero fallo!")

    character.save_to_db()  #enemy.fight() does not save automatically

    # End battle in death if character killed
    if killed:
        character.die()

        await ctx.message.reply(
            f"{character.name} ha sido derrotado por {enemy.name}. Descansa en paz,Pequeño aventurero."
        )
        return

    # No deaths, battle continues
    await ctx.message.reply(f"Las batallas continuan! Quieres `>luchar` o `>huir`?"
                            )


@client.command(name="huir", help="Huir del enemigo.")
async def huir(ctx):
    character = load_character(ctx.message.author.id)

    if character.mode != GameMode.BATTLE:
        await ctx.message.reply("Solo pudes llamar este comadno en batalla!")
        return

    enemy = character.battling
    damage, killed = character.flee(enemy)

    if killed:
        character.die()
        await ctx.message.reply(
            f"{character.name} fue assesinado huyendo por {enemy.name}, Descansa en paz pequeño aventurero."
        )
    elif damage:
        await ctx.message.reply(
            f"{character.name} huyo de {enemy.name}, recibiendo {damage} de daño. HP: {character.hp}/{character.max_hp}"
        )
    else:
        await ctx.message.reply(
            f"{character.name} huyo de {enemy.name} con toda su vida pero no con con la dignidad intacta. HP: {character.hp}/{character.max_hp}"
        )


@client.command(
    name="subirnivel",
    help=
    "Mejora el siguiente nivell (HP, ATTACK, DEFENSE)."
)
async def subirnivel(ctx, increase):
    character = load_character(ctx.message.author.id)

    if character.mode != GameMode.ADVENTURE:
        await ctx.message.reply("Solo se puede llamar este comando fuera de batalla!"
                                )
        return

    ready, xp_needed = character.ready_to_level_up()
    if not ready:
        await ctx.message.reply(
            f"Aun necessitas {xp_needed} Para avanzar al nivel {character.level+1}"
        )
        return

    if not increase:
        await ctx.message.reply(
            "Porfavor especifica la estadistica que quieres mejorar (HP, ATTACK, DEFENSE)")
        return

    increase = increase.lower()
    if increase == "hp" or increase == "hitpoints" or increase == "max_hp" or increase == "maxhp":
        increase = "max_hp"
    elif increase == "attack" or increase == "att" or increase == "ataque":
        increase = "attack"
    elif increase == "defense" or increase == "def" or increase == "defence" or increase == "defensa" :
        increase = "defense"

    success, new_level = character.level_up(increase)
    if success:
        await ctx.message.reply(
            f"{character.name} Paso al nivel {new_level}, ganando 1 {increase.upper().replace('_', ' ')}."
        )
    else:
        await ctx.message.reply(f"{character.name} Intento fallido de subida de nivel.")


@client.command(name="autodestruccion", help="Destruir tu caracter.")
async def autodestruccion(ctx):
    character = load_character(ctx.message.author.id)

    character.die()

    await ctx.message.reply(
        f"El personaje {character.name} ha sido destruido por su creador,Una pena :( crea uno nuevo con `>crear`."
    )


@client.command(name="reset",
             help="[DEV] destruir y recrear el propio personaje.")
async def reset(ctx):
    user_id = str(ctx.message.author.id)

    if user_id in db["personajes"].keys():
        del db["personajes"][user_id]

    await ctx.message.reply(f"Character deleted.")
    await create(ctx)



########################################
#Channels


@client.command()
async def canales(ctx):
    for guild in client.guilds:
        for channel in guild.text_channels:
            await ctx.send(channel)


##########info spoty#################
@client.command()
async def spotify(ctx, user: discord.Member = None):
    '''para saber info de spotify de alguien'''
    user = user or ctx.author
    spot = next((activity for activity in user.activities
                 if isinstance(activity, discord.Spotify)), None)
    if spot is None:
        await ctx.send(f"{user.name} no esta escuchando Spotify")
        return
    embed = discord.Embed(title=f"Spotify de {user.name}", color=spot.color)
    embed.add_field(name="Cancion", value=spot.title)
    embed.add_field(name="Artista", value=spot.artist)
    embed.add_field(name="Album", value=spot.album)
    embed.add_field(
        name="Link del Track",
        value=f"[{spot.title}](https://open.spotify.com/track/{spot.track_id})"
    )
    embed.set_thumbnail(url=spot.album_cover_url)
    await ctx.send(embed=embed)


###########################################
#########para paginas de revista o algo##########
@client.command()
async def revista(ctx):
    contents = [
        "**Esto es la pagina 1!**\nhttps://tenor.com/view/minecraft-boxer-boxing-minecraft-boxer-gif-18025297",
        "**Esto es la pagina 2!**", "**Esto es la pagina 3!**",
        "**Esto es la pagina 4!**", "**Esto es la pagina 5!**",
        "**Esto es la pagina 6!**"
    ]
    pages = 6
    cur_page = 1
    message = await ctx.send(
        f"Pagina {cur_page}/{pages}:\n{contents[cur_page-1]}")

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add",
                                                   timeout=60,
                                                   check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(
                    content=f"Pagina {cur_page}/{pages}:\n{contents[cur_page-1]}"
                )
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(
                    content=f"Pagina {cur_page}/{pages}:\n{contents[cur_page-1]}"
                )
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except asyncio.TimeoutError:
            await message.delete()
            break


#####################para echar a alguien###################
password = '2203021022'


@client.command()
async def fuera(ctx, member: discord.Member, *, password_check=None):
    '''puedes echar a alguien pero con contra'''
    if password_check and password_check == password:
        await ctx.message.channel.purge(limit=1)
        await ctx.send('contrasseña correcta!')
        await member.kick()
    elif not password_check:
        await ctx.send('sin contra no puedes compa!')
    else:
        await ctx.message.delete()
        await ctx.send('error 404 contrasseña incorrecta.')


#######para suicidarseeeee##############
@client.command()
async def morir(ctx):
    '''para suicidarse'''
    suicideembed = discord.Embed(title=f'{ctx.author} se ha suicidado',
                                 description="Probablemente este triste",
                                 color=0x000000)
    suicideembed.set_image(
        url='https://media1.giphy.com/media/c6DIpCp1922KQ/giphy.gif')
    suicideembed.set_footer(text='*No hagan esto en sus casas xd*')
    suicideembed2 = discord.Embed(title=f'{ctx.author} se ha suicidado',
                                  description="Probablemente este triste",
                                  color=0x000000)
    suicideembed2.set_image(
        url=
        'https://media1.tenor.com/images/041dddf7d24b9ba3d591e0bed2ce38c7/tenor.gif?itemid=4524247'
    )
    suicideembed2.set_footer(text='*No hagan esto en sus casas xd*')
    suicideembed3 = discord.Embed(title=f'{ctx.author} se ha suicidado',
                                  description="Probablemente este triste",
                                  color=0x000000)
    suicideembed3.set_image(
        url='https://i.makeagif.com/media/9-14-2015/vyNnjt.gif')
    suicideembed3.set_footer(text='*No hagan esto en sus casas xd*')
    suicideembed4 = discord.Embed(title=f'{ctx.author} se ha suicidado',
                                  description="Probablemente este triste",
                                  color=0x000000)
    suicideembed4.set_image(
        url='https://thumbs.gfycat.com/SnarlingTameEquine-max-1mb.gif')
    suicideembed4.set_footer(text='*No hagan esto en sus casas xd*')
    suicideembed6 = discord.Embed(title=f'{ctx.author} se ha suicidado',
                                  description="Probablemente este triste",
                                  color=0x000000)
    suicideembed6.set_image(
        url='https://tenor.com/view/epic-meme-kermit-suicide-gif-20626092')
    suicideembed6.set_footer(text='*No hagan esto en sus casas xd*')
    suicideembed5 = discord.Embed(title=f'{ctx.author} se ha suicidado',
                                  description="Probablemente este triste",
                                  color=0x000000)
    suicideembed5.set_image(
        url='https://media2.giphy.com/media/13kJc5CTOnqdQk/giphy.gif')
    suicideembed5.set_footer(text='*No hagan esto en sus casas xd*')
    suicidio = [
        suicideembed, suicideembed2, suicideembed3, suicideembed4,
        suicideembed5, suicideembed6
    ]
    await ctx.send(embed=random.choice(suicidio))


##############################################
#####para tomar chupitoooosss########
@client.command()
async def fumeteo(ctx):
    '''aver quantos calos aguantas campeeon'''
    salve = random.randint(1, 15)
    boss = [
        f'{ctx.author} se mantiene en pie despues de {salve} calos!',
        f'{ctx.author} empezo a ir ciego despues de {salve} calazos!'
    ]
    poo = random.choice(boss)
    deshqiperine = [
        'https://media.tenor.com/lWYKkXN2tasAAAAM/smoke-cigarette.gif',
        'https://media.tenor.com/zoglollWU_8AAAAM/smoke-cigarette.gif',
        'https://media.tenor.com/KCDaAubmS4YAAAAM/smoke-shrug.gif'
    ]
    if salve > 7:
        embed = discord.Embed(
            title=
            f'{ctx.author} como se nota que te gusta la hierbita eeh jajajaja!',
            description=
            f'{ctx.author.mention} sa fumao unos petas como un misil y sigue en pie!',
            color=0x000000)
        embed.add_field(name='Epico,este es immortal seguro',
                        value=poo,
                        inline=False)
        embed.set_image(url=random.choice(deshqiperine))
        embed.set_footer(text='en la real life es pegriloso xd')
    else:
        embed = discord.Embed(
            title=f'{ctx.author} te falta practica...que la palmas!',
            description=
            f'{ctx.author.mention} intento ser un pro...y el blancazo se llevo!JAJJAJA',
            color=0x000000)
        embed.add_field(
            name=f'{ctx.author} le dio blanca despues de {salve} calazos!',
            value='que lastima...',
            inline=False)
        embed.set_image(url=random.choice(deshqiperine))
        embed.set_footer(text='en la rial life es pegriloso xd')
    await ctx.send(embed=embed)


#####para tomar chupitoooosss########
@client.command()
async def shot(ctx):
    '''para tomar ronda de chupitos'''
    salve = random.randint(1, 15)
    boss = [
        f'{ctx.author} se mantiene sobrio despues de {salve} shots!',
        f'{ctx.author} se emborracho despues de {salve} shots!'
    ]
    poo = random.choice(boss)
    deshqiperine = [
        'https://media1.tenor.com/images/4a6e5632592a753d5ddd4ecef30357e6/tenor.gif?itemid=3558432',
        'https://media1.tenor.com/images/8e830da5d0e3e08ae2469e9bf6afc5c9/tenor.gif?itemid=8561333',
        'https://media.tenor.com/d78OPdbdfKoAAAAC/alcohol-shots.gif'
    ]
    if salve > 7:
        embed = discord.Embed(
            title=f'{ctx.author} se bebio el chupito como un ruso!',
            description=
            f'{ctx.author.mention} bebio el chupito como un verdadero ruso!',
            color=0x000000)
        embed.add_field(name='Epico,este es ruso fijo',
                        value=poo,
                        inline=False)
        embed.set_image(url=random.choice(deshqiperine))
        embed.set_footer(text='en la real life es pegriloso xd')
    else:
        embed = discord.Embed(
            title=f'{ctx.author} se bebio el chupito como un ruso!',
            description=
            f'{ctx.author.mention} se bebio el chupito como un verdadero rusp',
            color=0x000000)
        embed.add_field(
            name=f'{ctx.author} se emborracho despues de {salve} shots!',
            value='que lastima...',
            inline=False)
        embed.set_image(url=random.choice(deshqiperine))
        embed.set_footer(text='en la rial life es pegriloso xd')
    await ctx.send(embed=embed)


######################encriptar mensajeeee#########################
@client.command(aliases=["enc"])
@commands.has_role(1032272403893596260)
async def encriptar(ctx, *args):
    '''para encriptar el mensaje'''
    shift_pattern = 4
    text = ""
    for i in args:
        text += i
    print(text)
    message = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + shift_pattern) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    print(f"Mensaje Encriptado: `{result}`")
    await ctx.message.delete()
    await ctx.send(f"Mensaje Encriptado: `{result}`")


###############################################
######para pescarrrr pero no me lo detectaaaaaaa
@client.command(description="de pesca chavaless")
async def pescar(ctx):
    '''nos vamos de pesca'''
    num = random.randint(1, 100)
    special = 0
    if num < 95:
        _catch = await catch()
    else:
        _catch = await special_catch()
        special = 1
    e = discord.Embed(title="A Pescar!",
                      description="Te fuiste a pescar!",
                      colour=0xf54242)
    e.set_thumbnail(url="https://i.imgur.com/3Q3VDp9.jpg")
    msg = await ctx.send(embed=e)
    await asyncio.sleep(3)
    e = discord.Embed(title="Pescando",
                      description="Algo ha picado!",
                      colour=0xd4f542)
    e.set_thumbnail(url="https://i.imgur.com/Y3mpQhm.jpg")
    await msg.edit(embed=e)
    await asyncio.sleep(3)
    e = discord.Embed(title="Pescando",
                      description=f"Has conseguido {_catch[0]}!",
                      colour=0x919191)
    e.set_thumbnail(url="https://i.imgur.com/59TKpfE.jpg")
    if special == 0:
        basePrice = _catch[2]
        minWeight = _catch[3]
        maxWeight = _catch[4]
        goldWeight = _catch[5]
        weight = round(random.uniform(minWeight, maxWeight), 3)
        # PRECIO
        price = 0
        a = ""
        if weight >= goldWeight:
            price = round(basePrice + ((basePrice / 50) * weight * 3), 2)
            a = "\nEste pez es extraordinariamente largo!"
        else:
            price = round(basePrice + ((basePrice / 100) * weight), 2)
        if _catch[0] == "Nada":
            e.add_field(name=_catch[0], value="Has perdido el tiempo!")
            e.set_thumbnail(url="https://i.imgur.com/C6rQmPZ.gif")
        else:
            e.add_field(name=_catch[0],
                        value=f"**Peso**: `{weight}kg`\n" +
                        f"**Valor**: `{price}$ `" + a)
    else:
        price = _catch[2]
        description = _catch[3]
        icon = _catch[4]
        e.set_thumbnail(
            url="https://live.staticflickr.com/22/25807800_4f776527bb_b.jpg")
        e = discord.Embed(
            title="Pescando",
            description=f"**Item Especial! Has conseguido {_catch[0]}!!!**",
            colour=0xcc00ff)
        e.add_field(name=icon + " " + _catch[0],
                    value=f"**Descripcion**: `{description}`\n" +
                    f"**Valor**: `{price}$`")

    await msg.edit(embed=e)


fishes = (
    # 0Name, 1Weight (Chance), 2Base Price, 3minWeight, 4maxWeight, 5goldWeight
    ("Nada", 30, 0, 0, 0, 1),
    ("sardina", 10, 10, 1, 22.4, 16),
    ("Pececillo", 17, 5, 0.3, 4, 25),
    ("Trucha", 10, 12, 8, 48, 35),
    ("bacalao", 10, 10, 3, 212, 180))
special = (
    # Name, Weight, Price, Description, Icon
    ("Tu gracia", 1, 6969, "Muy raro de encontrar", ":monkey:"),
    ("Bota", 4, 3, "Vieja bota usada ", ":boot:"),
    ("Prostituta", 2, 200, "Dios te escucha.", ":dancer:"),
    ("Dildo", 3, 23, "humedo y usado (por el agua xd)", ":baby_bottle:"),
    ("Skateboard", 3, 200, "Muy raro y dificil de encontrar", ":skateboard:"),
    ("Invitacion a patinar", 0.0001, 99999, "%skrt%", ":skateboard:"),
    ("Mierda de perro", 6, 1, "Huele a mierda por aqui.", ":poop:"),
    ("Tu madre", 0.005, 2, "Es gorda pero no vale la pena.", ":cap:"))


async def catch():

    pr = []
    for i in range(0, len(fishes)):
        pr.append(fishes[i][1])
    pr = round_to_100_percent(pr)
    return fishes[np.random.choice(len(fishes), p=pr)]


async def special_catch():
    pr = []
    for i in range(0, len(special)):
        pr.append(special[i][1])
    pr = round_to_100_percent(pr)
    return special[np.random.choice(len(special), p=pr)]


def round_to_100_percent(number_set, digit_after_decimal=2):
    unround_numbers = [
        x / float(sum(number_set)) * 100 * 10**digit_after_decimal
        for x in number_set
    ]
    decimal_part_with_index = sorted(
        [(index, unround_numbers[index] % 1)
         for index in range(len(unround_numbers))],
        key=lambda y: y[1],
        reverse=True)
    remainder = 100 * 10**digit_after_decimal - sum(
        [int(x) for x in unround_numbers])
    index = 0
    while remainder > 0:
        unround_numbers[decimal_part_with_index[index][0]] += 1
        remainder -= 1
        index = (index + 1) % len(number_set)
    return [(int(x) / float(10**digit_after_decimal)) / 100
            for x in unround_numbers]


#############################################
#########para desencriptar el mensaje#########
@client.command(aliases=["dec"])
@commands.has_role(1032272403893596260)
async def desencriptar(ctx, *args):
    '''para desencriptar mensajes encriptados'''
    shift_pattern = 4  #mueve 4 en el abecedario de letras
    text = ""
    for i in args:
        text += i
    print(text)
    message = text.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:  #si la letra es una letra
            #encuentra la letra en el alfabeto
            letter_index = (alpha.find(letter) - shift_pattern) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    print(f"Mensaje Decriptado: `{result}`")
    await ctx.message.delete()
    await ctx.send(f"Mensaje Decriptado: `{result}`")


###############################################
#######para practicar operaciones de mates#######
@client.command()
async def op(ctx):
    primero = random.randint(1, 100)
    segundo = random.randint(1, 100)
    operandacio = random.randint(1, 100)
    oper = "+"
    bonus = 1
    if operandacio < 9:
        oper = "*"
        respuestaa = str(primero * segundo)
        tiempo = 40
        bonus = 4
    elif operandacio < 40:
        oper = "-"
        respuestaa = str(primero - segundo)
        tiempo = 30
        bonus = 2
    else:
        tiempo = 20
        respuestaa = str(primero + segundo)
    timepo = int(tiempo)

    pregunta = "Cuanto es " + str(primero) + " " + oper + " " + str(
        segundo) + "?"
    embed = discord.Embed(title=pregunta,
                          description="tienes " + str(tiempo) +
                          " segundos para resolverlo y una unica oportunidad.",
                          color=discord.Colour.blue())
    await ctx.send(embed=embed)

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        mensajeRespuesta = await ctx.bot.wait_for("message",
                                                  timeout=tiempo,
                                                  check=check)
        contenidoMensaje = mensajeRespuesta.content

        if contenidoMensaje == respuestaa:
            embed = discord.Embed(
                title="Tu respuesta: " + respuestaa + " es correcta!",
                description=f"Eres un celebrito te ganaste x dinero",
                color=discord.Colour.blue())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Tu respuesta no fue correcta!",
                description="deja los porros y ponte a estudiar.",
                color=discord.Colour.red())
            await ctx.send(embed=embed)

    except discord.Forbidden:
        await ctx.send("demasiado tiempo esperando..")


#######apiiiiii del tiemmpo###########
@client.command()
async def tiempo(ctx, location):
    '''sirve para mostrar el tiempo de la ciudad'''
    mykey = 'a2fad8b8ac4387388969c71bb664d785'  #get your api key from https://openweathermap.org/
    link = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + mykey
    api_link = requests.get(link)
    api_data = api_link.json()

    #crear variables para almacenar y mostrar datos
    temp_city = ((api_data['main']['temp']) - 273.15)  #para que sean grados
    feelslike_temp = ((api_data['main']['feels_like']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    visibility = api_data['visibility']
    #date_time = datetime.date().strftime("%d %b %Y | %I:%M:%S %p") {round(client.latency * 1000)}

    title = f'⛅ El tiempo para {location}.'

    description = f'🌡️ Temperatura: {round(temp_city * 1)}°C \n \n 🔥 Sensacion Termica: {round(feelslike_temp * 1)}°C \n \n☁️ Tipo: {weather_desc}. \n \n 🥵 Humedad: {hmdt}% \n \n 💨 Velocidad del viento: {wind_spd} km/h \n \n 👀 Visibilidad: {visibility} Metros'
    embed = discord.Embed(title=title,
                          description=description,
                          color=discord.Colour.orange())
    await ctx.send(embed=embed)


#para trolearrrrr esta en fase desarrollooooo
@client.command()
async def troll(ctx):
    '''para trolear (en desarrollo)'''
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


#################para saltar a otro mensaje buscado########
@client.command()
async def buscar(ctx, word: str):
    '''para buscar contendio especifico'''
    channel = ctx.message.channel
    messages = await ctx.channel.history(limit=200).flatten()

    for msg in messages:
        if word in msg.content:
            embed = discord.Embed(title="Buscador de contenido!",
                                  description=f"Busquedas: " + msg.jump_url,
                                  color=0x00FFFF)
            await ctx.message.delete()
            await ctx.send(embed=embed)


#############################################
#bola de la fortunaaaaaaa################################
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    '''la bola de la verdad!'''
    responses = [
        'seguramente', 'sigue soñando!', 'tu lo flipas verdad?', 'wtf',
        'que te jodan', 'oye no me molestes que tengo mucho que hacer',
        'dejame mirar! \n8ball' + question + '\n...\nNop',
        'tal como lo veo yo,Si.', 'preguntamelo mas tarde',
        'de verdad ' + question + ' es tu pregunta?que aburrido..',
        'possiblemente pero no te confies', 'ahora mismo no puedo predecirlo',
        'mis fuentes me dicen que no', 'eso es cierto', 'sin duda alguna',
        'muy dudosos la verdad.', 'concreta y preguntamelo de nuevo',
        'mejor no te lo digo..',
        'rezale a dios que tiene pinta que obtendras la respuesta de el',
        'no estoy seguro,mira en tu corazon', 'ni de flais ',
        'tu que crees?pues esa es la respiesta', 'nop', 'sip',
        'ni en el futuro se sabe'
    ]
    embed = discord.Embed(
        title="La bola de la verdad!",
        description=
        f"Pregunta: {question}\nRespuesta: {random.choice(responses)}",
        color=0x00FFFF)
    await ctx.message.delete()
    await ctx.send(embed=embed)


#para hacer las cajas de informacion#########
#@client.command()
#@commands.is_owner()
#async def embed(ctx):
#  embed = discord.Embed(
#    title = 'Title',
#    url = "https://www.google.com",
#    description = 'Test',
#    colour = discord.Colour.blue()
#  )
#  embed.set_footer(text = 'Test2')
#  embed.set_author(name='Bot')
#  await ctx.send(embed = embed)
###############################################################
#para mandar dm##############################
@client.command(description="para hacer que el bot mande dm a alguien")
async def dm(ctx, member: discord.Member, *, msg):
    '''para mandar dm a alguien'''
    author2 = ctx.author.mention
    author = ctx.author
    await ctx.send(f"Enviando tu mensaje a {author2}")

    await member.send(
        embed=discord.Embed(title=f"**Nuevo mensaje de {author} !**",
                            description=f"{msg}",
                            colour=discord.Colour.blue()))


#para mostrar los miembros del grupo
@client.command()
async def miembros(ctx):
    '''para mostrar el total de miembros en el canal'''
    embed = discord.Embed(title="", description="", color=0x00FFFF)
    embed.add_field(
        name="Numero de Miembros:",
        value=
        f"Actualmente hay: **{ctx.guild.member_count}** in **{ctx.guild.name}**!",
        inline=False)
    await ctx.send(embed=embed)
    await ctx.message.delete()


###############ahorcado#######################
@client.command()
async def ahorcado(ctx):
    '''ahorcado'''
    try:
        wrongGuesses = []

        sonad = []
        with open('palabras_ahorcado.txt', 'r') as txtfile:
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
        await ctx.send(f"Esta palabra tiene  {len(ranwordd)} letras")
        await ctx.send("Escoje una letra")
        tries = 5
        while tries > 0:

            def check(msg):
                return msg.author == ctx.author and ctx.channel == msg.channel

            print(bury)
            msg = await ctx.bot.wait_for("message", check=check, timeout=60)

            c = msg.content
            if len(msg.content) != 1:
                await ctx.send("porfa pon solo una letra por envio")
            if c in ranwordd:
                if ranwordd.count(c) >= 2:
                    indexes = [i for i, e in enumerate(ranwordd) if e == c]
                    bury[indexes[0]] = c
                    bury[indexes[1]] = c

                await ctx.send(f'letras incorrectas: {wrongGuesses}')
                a = ranwordd.index(c)
                bury[a] = c
                print(bury)
                unbury = " ".join(bury)
                the_final = "".join(bury)
                print(unbury)
                heyy = discord.Embed(
                    title=discord.utils.escape_markdown(unbury))
                await ctx.send(embed=heyy)
                if the_final == ranwordd:
                    emb = discord.Embed(title="Ahorcado")
                    emb.add_field(name="Ole Ole caracole", value="Has ganado!")
                    return await ctx.send(embed=emb)
                else:
                    pass
            else:
                wrongGuesses.append(c)
                tries -= 1
                await ctx.send(f"La letra {c} no se encuentra en la palabra")
                await ctx.send(f'Letras incorrectas: {wrongGuesses}')
        await ctx.send(f"Has perdido!\nLa palabra era  {ranwordd}")
    except asyncio.TimeoutError:
        return await ctx.send("Has tardado demasiado bro..")


######################################################
#########bot para matar a alguien
@client.command(description="para matar a alguien")
async def matar(ctx, user: discord.Member):
    '''para matar a alguien'''
    matar = await ctx.send("🤡😄")
    await asyncio.sleep(0.6)
    await matar.edit(content="🤡🎁😳")
    await asyncio.sleep(1)
    await matar.edit(content="🤡🔪😱")
    await asyncio.sleep(0.3)
    await matar.edit(content="🤡🔪💥")
    await asyncio.sleep(0.3)
    await matar.edit(content="🤡🔪😵")
    embed = discord.Embed(
        title="Bienvenido al cielo!",
        description=
        f"{user.mention} ha sido assesinado por {ctx.author.mention} \nNoob",
        color=0x00FFFF)
    await ctx.message.delete()
    await ctx.send(embed=embed)


@client.command()
###########################para pegr un dab pero no funcionaaaaaa
async def dab(ctx):
    '''para hacer un dab'''
    dab = await ctx.send("<o/")
    await dab.edit(content="\o>")
    await asyncio.sleep(0.5)
    await dab.edit(content="<o/")
    await asyncio.sleep(0.5)
    await dab.edit(content="\o>")
    await asyncio.sleep(0.5)
    await dab.edit(content="<o/")
    await asyncio.sleep(0.5)
    ##########################################################


#para medir las relacionesss############################
@client.command(description="para medir la relacion de alguien")
async def rela(ctx, user_1: discord.Member, user_2: discord.Member):
    '''para medir porcentaje de relacion en'''
    responses = [
        ' encajan juntos al 1% !', ' encajan juntos al 5% !',
        ' encajan juntos al 10% !', ' encajan juntos al 15% !',
        ' encajan juntos al 20% !', ' encajan juntos al 25% !',
        ' encajan juntos al 30% !', ' encajan juntos al 35% !',
        ' encajan juntos al 40% !', ' encajan juntos al 45% !',
        ' encajan juntos al 50% !', ' encajan juntos al 55% !',
        ' encajan juntos al 60% !', ' encajan juntos al 65% !',
        ' encajan juntos al 70% !', ' encajan juntos al 75% !',
        ' encajan juntos al 80% !', ' encajan juntos al 85% !',
        ' encajan juntos al 90% !', ' encajan juntos al 95% !',
        ' encajan juntos al 100% !'
    ]
    response = random.choice(responses)
    embed = discord.Embed(title="Aqui teneis vuestro resultado!",
                          color=0x22a7f0)
    embed.add_field(name='`Respuesta:`',
                    value=f"{user_1.mention} y {user_2.mention}{response}",
                    inline=False)
    await ctx.send(embed=embed)


    #######################para prueva o verdaaadddd###############################################
@client.command(help="prueva o verdad")
async def pv(ctx):
    '''para hacer prueva o verdad'''
    truth_items = [
        'Si pudieras ser invisible,cual es la primera cosa que harias?',
        'Si te dieran tres deseos cuales serian?',
        'Cual es el maximo de dias que has podido pasar sin ducharte?',
        'Cual es el animal que crees que te pareces mas?',
        'Dime uno de tus mayores secretos', 'Has robado alguna vez?',
        'Quien es tu crush famoso?', ''
    ]
    dare_items = [
        'Comete unos yatekomo crudos.',
        ' Baila sin musica durante 20 segundos.',
        'Deja que alguien que escojas tenga el privilegio de decidir un mensaje que deberas mandar a alaguien que el decida.',
        ' Deja que una persona te dibuje en la cara con un boli.',
        'Intenta hacer un truco de magia.',
        'Rebientate dos huevos en la cabeza.',
        'Grita por la ventana :no he sido yo ha sido el.',
        ' Dile a tu madre que necesitas mariguana para aliviar las penas.'
    ]

    embed = discord.Embed(
        title="Prueva o Verdad!",
        description="Porfavor escribe v para verdad y p para prueba",
        color=0x00FFFF)
    await ctx.message.delete()
    await ctx.send(embed=embed)

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower(
        ) in ("v", "r")

    message = await ctx.bot.wait_for("message", check=check)
    choice = message.content.lower()
    if choice == "v":
        embed = discord.Embed(title="Verdad",
                              description=f"{random.choice(truth_items)}",
                              color=0x00FFFF)
    await ctx.send(embed=embed)

    if choice == "p":
        embed = discord.Embed(title="Prueba!",
                              description=f"{random.choice(dare_items)}",
                              color=0x00FFFF)
    await ctx.send(embed=embed)


###############################################
#######candyreaccion#########################
@client.command()
async def candy(ctx):
    """Pilla el caramelo antes que nadie!"""

    embed = discord.Embed(
        description="🍬 | El primero que la coja se lo queda!", colour=0x0EF7E2)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🍬")

    def check(reaction, user):
        return user != ctx.bot.user and str(
            reaction.emoji) == '🍬' and reaction.message.id == msg.id

    msg0 = await ctx.bot.wait_for("reaction_add", check=check)

    embed.description = f"🍬 | {msg0[1].mention} ha ganado y se lo ha comido!"

    await msg.edit(embed=embed)
    ####3mejorar esta parte que me falla nose porque

    with open("candylb.json", "w") as f:

        l = json.load(f)

        try:

            l[str(msg0[1].id)] += 1
            json.dump(l, f, indent=4)

        except KeyError:

            l[str(msg0[1].id)] = 1

    with open("candylb.json", "w") as f:

        json.dump(l, f, indent=4)


@client.command()
async def candyboard(self, ctx):
    """El ranking de top candelers!"""

    with open("candylb.json", "w") as f:

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

    embed = discord.Embed(description=res, colour=0x0EF7E2)
    await ctx.send(embed=embed)


################################################
#############


#per fer una enquesta pero no va###################
@client.command(pass_context=True)
async def encuesta(ctx, question, *options: str):
    '''para hacer una encuesta'''
    if len(options) <= 1:
        await ctx.send('Necesitas más de una opción para hacer una encuesta!')
        return
    if len(options) > 10:
        await ctx.send(' No puedes hacer una encuesta para más de 10 cosas!')
        return

    reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

    member = ctx.message.author.id
    description = []
    for x, option in enumerate(options):
        description += '\n {} {}'.format(reactions[x], option)
    embed = discord.Embed(title=question, description=''.join(description))
    embed.add_field(name="Aquí tienes ", value=f"<@{ctx.message.author.id}> ")

    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)

    #CHANGE THE TIME
    await asyncio.sleep(20)

    #CAN BE BROKEN EASILY
    react_message = await ctx.fetch_message(react_message.id)

    emojis = []
    count = []
    for reaction in react_message.reactions:
        emojis.append(reaction.emoji)
        count.append(int(reaction.count) - 1)

    result = dict(zip(emojis, count))

    flag = -1
    max_emoji = ""

    for emoji, coun in result.items():
        if coun == 0:
            continue
        elif coun == max(count):
            max_emoji = emoji
            flag = 0

    if flag == -1:
        max_emoji = "Todo"

    embd = discord.Embed(title=question, description=''.join(description))
    embd.add_field(name="Aquí tienes, ", value=f"<@{ctx.message.author.id}> ")
    embd.add_field(name="Los resultados son: ",
                   value='\n'.join([
                       '{}: {}'.format(key, result[key])
                       for key in result.keys()
                   ]))
    embd.add_field(name="Más votos",
                   value='{} ¡Tiene {} votos!'.format(max_emoji, max(count)))
    await react_message.delete()
    await ctx.send(embed=embd)


########################################################################
@client.command()
async def ascii(ctx, arg):
    '''para texto ascii'''
    text = pyfiglet.figlet_format(arg)
    await ctx.send(f"```\n{text}\n```")


#########################################


#PARA AVISAR A ALGUIEN#####################
@client.command(description="para mandar avisos a la gente")
@commands.has_permissions(manage_messages=True)
async def aviso(ctx, user: discord.Member, *, reason):
    '''para avisar a alguien'''
    embed = discord.Embed(
        title="Atencion!",
        description=
        f"{user.mention} ha sido avisado por {ctx.author.mention} | Razon: {reason}",
        color=0x00FFFF)
    await ctx.message.delete()
    await ctx.send(embed=embed)


#cosas diveritodas con cumplidos
#@client.command()
#async def divertido(ctx):
#  async with aiohttp.ClientSession() as session:
#    async with session.get("https://complimentr.com/api") as r:
#      file = await r.json()
#      await ctx.send(file["compliment"])
#AÑADIR TAREAS
@client.command(description="para añadir tareas a la lista")
async def tarea(ctx, *args):
    '''para añadir tareas pendeintes'''
    output = ""
    for word in args:
        output += word
        #output += " "
    TaskList.append(output)
    await ctx.send("La tarea '" + output + "' se ha añadido a la lista!")


#para mostrar las tareas pendientes
@client.command(description="para mostrar tareas pendientees")
async def vertareas(ctx):
    '''para ver tareas'''
    await ctx.send(TaskList)


#para borrar las tareas estaria bien borrrar la que se quisiera
@client.command(description="eliminar las tareas de la lista")
async def borrartareas(ctx):
    '''para borrar tareas'''
    TaskList[:] = []
    await ctx.send("Se han borrado las tareas pendientes")


#para hacear REFACTORIZAR CODIGO hacking#######################################REVISAR
@client.command()
async def hack(ctx, member: discord.Member, test=None):
    '''para simular hackeo(incompleto)'''
    virs = [
        'melissa', 'LOVE_YOU.txt.vbs', 'Klez', 'CoDe ReD', 'Nimda',
        'SQL slammer', 'My Doom', 'sasser', 'leap A', 'Oompa A', 'storm worm'
    ]
    virs_random = random.choice(virs)
    if member == ctx.author:
        await ctx.send('(⌐■_■) Nanai compai')
    elif member == client.user:
        await ctx.send('ಥ_ಥ lo flipas xabal')
    elif member.bot:
        await ctx.send('(•_•) tu eres tonto ?jajajajaj')
    else:
        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            description=
            f"Un virus malicioso \"{virs_random}\" uno de los mas peligrosos del mundo..."
        )
        embed.set_footer(text="NOTA:Prohibido denunciarme :)")
        embed.set_author(name=client.user.name,
                         icon_url=client.user.avatar_url)
        await ctx.send(embed=embed)
        my_msg = await ctx.send('Cargando.')
        await asyncio.sleep(0.1)
        await my_msg.edit(content='Cargando..')
        await asyncio.sleep(0.1)
        await my_msg.edit(content='Cargando...')
        await asyncio.sleep(0.3)
        await my_msg.edit(content=f'Cargando... {virs_random}')
        await asyncio.sleep(0.2)
        await my_msg.edit(
            content=f'[ {virs_random} ]: Cargando Virus en Usuario [▓ ] 1%')
        await my_msg.edit(
            content=f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓ ] 2%')
        await my_msg.edit(
            content=f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓ ] 3%')
        await my_msg.edit(
            content=f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓ ] 4%')
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓ ] 20%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓  ] 30%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 40%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 50%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 70%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 85%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 90%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 95%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 96%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 97%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 98%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] 99%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Cargando Virus en Usuario [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 100%'
        )
        await asyncio.sleep(0.5)
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: Ha sido introducido en el sistema correctamente'
        )
        await asyncio.sleep(0.1)
        await my_msg.edit(content=f'[ {virs_random} ]: Cargando recursos...')
        await asyncio.sleep(0.1)
        await my_msg.edit(content=f'[ {virs_random} ]: Espera 5 segundos ...')
        await asyncio.sleep(1)
        await my_msg.edit(content=f'[ {virs_random} ]: Espera 4 segundos ...')
        await asyncio.sleep(1)
        await my_msg.edit(content=f'[ {virs_random} ]: Espera 3 segundos ...')
        await asyncio.sleep(1)
        await my_msg.edit(content=f'[ {virs_random} ]: Espera 2 segundos ...')
        await asyncio.sleep(1)
        await my_msg.edit(content=f'[ {virs_random} ]: Espera 1 segundo ...')
        await asyncio.sleep(1)
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓] 99%'
        )
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]100% virus añadido al sistema'
        )
        await asyncio.sleep(1)
        await my_msg.edit(
            content=
            f'[ {virs_random} ]: **al reiniciar se emplearan los cambios**!')
        embed = discord.Embed(
            timestamp=ctx.message.created_at,
            description=
            f"Has sido hackeado con \"{virs_random}\" Uno de los virus mas peligrosos del mundo \n Creador: @{ctx.author.display_name}#{ctx.author.discriminator}"
        )
        embed.set_footer(text="NOTA: Prohibido denunciar :)")
        embed.set_author(name=client.user.name,
                         icon_url=client.user.avatar_url)
        await member.send(embed=embed)


###########################MAKINA NEPESA#####################################
pp = [
    "=", "==", "===", "====", "=====", "======", "=======", "========",
    "=========", "==========", "===========", "============", "=============",
    "==============", "===============", "================",
    "================", "================================="
]
cog = [
    " peke", " diminuto", " pequeñito", " pequeño", " minusculo", "normal",
    "normalito", "que no esta mal", "aceptable", "jugueton", "asequible",
    " grande", " grandote", " gigante", " monstruoso", " satisfactorio",
    " exhoberante", " misil"
]


@client.command(description="maquina medidora de nepes")
async def mp(ctx):
    '''maquina medidora de nepes'''
    name = ctx.message.author
    randomInt = random.randint(0, 17)
    anz = "B" + pp[randomInt] + "D"

    member = ctx.message.author
    cok = cog[randomInt]
    tit = member.display_name + " tiene un nepe " + cok
    spac = "  "
    embed = discord.Embed(title="MP maquina medidora de nepes",
                          description=spac,
                          color=0x1d8eeb)

    embed.add_field(name=tit, value=anz)

    await ctx.send(embed=embed)


#-------------------------------------------------------------------------------
spac = " "

###############################################################################################
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
    '''texto en negrita'''
    await ctx.message.delete()
    await ctx.send('**' + message + '**')


#para mandar codigo
@client.command(description="para mandar en formato codigo")
async def c(ctx, message):
    '''texto formato codigo'''
    await ctx.message.delete()
    await ctx.send('```' + message + '```')


#para la api de la nasaaaaaa########################################
api = os.environ.get("nasa_key")


@client.command()
async def nasa(ctx, *, tarik=None):
    '''para solicitar imagen de la nasa'''
    try:
        if tarik == None:
            today = datetime.date.today()
            tarik = today
            print(tarik)
        para = {"api_key": api, "hd": True, "date": tarik}
        base = "https://api.nasa.gov/planetary/apod?"
        response = requests.get(base, params=para)
        x = response.json()
        y = x["title"]
        z = x["hdurl"]
        a = x["date"]
        embed = discord.Embed()
        embed.title = f"{y}"
        embed.description = f"NASA: Imagen Astronomica de: {a}"
        embed.colour = discord.Colour.red()
        embed.set_image(url=z)
        embed.set_footer(text=f"Solicitada por {ctx.author.name}")
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed()
        embed.title = "No hay imagen para la fecha de hoy."
        embed.description = ":telescope: intentalo de nuevo mas tarde cuando se haya actualizado! :cityscape: "
        embed.colour = discord.Colour.red()
        embed.set_footer(text=f"Solicitada por {ctx.author.name}")
        await ctx.send(embed=embed)


#para spam
@client.command(description="spam mejor no usar")
async def spam(ctx, amount: int, *, message):
    '''para hacer spam'''
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
    print(f"spam cmd done")


#para hascer sufrir con gif pero me marca errrorrrr


@client.command()
async def pain(ctx, client):
    '''en desarrollo'''
    imageList = [
        "http://cdn.discordapp.com/attachments/459080723253690389/576123702140207127/7.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123492773134336/Untitled.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123528923840532/foodgasm_5.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123553431158808/foodgasm_4.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123576550162443/foodgasm_3.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123599644262400/foodgasm_2.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123630702952459/foodgasm_1.png",
        "http://cdn.discordapp.com/attachments/459080723253690389/576123654165889024/8.png"
    ]
    embed = discord.Embed(color=discord.Color.purple())
    embed.set_author(name="💢" + ctx.author.name + " no tiene almal 💢")
    embed.set_image(url=random.choice(imageList))
    await ctx.channel.send(content=" ",
                           embed=embed)  #Displays a random image from a list


################para pegar abofetear o sequestrar alguien #######################
slapL = [
    "http://giphygifs.s3.amazonaws.com/media/jLeyZWgtwgr2U/giphy.gif",
    "https://media.giphy.com/media/fO6UtDy5pWYwM/giphy.gif",
    "https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif",
    "https://media.giphy.com/media/exaa8OED1vvq/giphy.gif",
    "https://media.giphy.com/media/10Am8idu3qBYRy/giphy.gif",
    "https://media.giphy.com/media/vDHHwJ1J5V41a/giphy.gif",
    "https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif",
    "https://media.giphy.com/media/hpzxqgsLMWGRO/giphy.gif",
    "https://media1.tenor.com/images/c159cd1d7e7424cf9fd6fbdb09919146/tenor.gif?itemid=14179570",
    "https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720",
    "https://media1.tenor.com/images/9baf03f104dd052931a5f06500cef014/tenor.gif?itemid=13932434",
    "https://media1.tenor.com/images/7437caf9fb0bea289a5bb163b90163c7/tenor.gif?itemid=13595529",
    "https://media1.tenor.com/images/35c1ecae2168c49be997871adc2a5d75/tenor.gif?itemid=3412059",
    "https://media1.tenor.com/images/f9f121a46229ea904209a07cae362b3e/tenor.gif?itemid=7859254"
]

punchL = [
    "https://media1.tenor.com/images/1c986c555ed0b645670596d978c88f6e/tenor.gif?itemid=13142581",
    "https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif?itemid=11451829",
    "https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/tenor.gif?itemid=14210784",
    "https://media1.tenor.com/images/55507aea306782b916659085fc062909/tenor.gif?itemid=8932977",
    "https://media1.tenor.com/images/f03329d8877abfde62b1e056953724f3/tenor.gif?itemid=13785833",
    "https://media1.tenor.com/images/b2308e16fa5b71c541efdd13dea4f9ba/tenor.gif?itemid=10462739",
    "https://tenor.com/view/anime-naruto-punch-fight-gif-12911685",
    "https://tenor.com/view/anime-super-punch-undressed-punch-gif-12303482",
    "https://tenor.com/view/shy-punch-anime-aki-adagaki-gif-12003970",
    "https://tenor.com/view/anime-smash-lesbian-punch-wall-gif-4790446",
    "https://tenor.com/view/punch-anime-gif-10237849",
    "https://tenor.com/view/anime-punch-gif-7922535",
    "https://tenor.com/view/sakura-naruto-punch-anime-gif-4807474",
    "https://tenor.com/view/punch-anime-ouch-fist-gif-4903584"
]

rapeL = [
    "https://cdn.discordapp.com/attachments/519011145676226564/626210362403848204/eggman.gif"
]
dance = ["http://tenor.com/view/dancing-gif-rain-dance-in-gif-26016606"]


#####para bailarle a alguien pero peta
@client.command()
async def bailar(ctx, usr: str):
    '''para bailarle a alguien(broken)'''
    member = ctx.message.author
    emb = ctx.message.author.mention + "Te ha dedicado un baile!"
    embed = discord.Embed(title="Rico bailesito pa tu bodi",
                          description=emb,
                          color=0x1d8eeb)
    embed.set_image(url=dance)
    await ctx.send(embed=embed)


######################################


@client.command()
async def abofetear(ctx, usr: str):
    '''para abofetear a alguien'''
    randomInt = random.randint(0, 14)
    member = ctx.message.author
    embn = ctx.message.author.mention + " ABOFETEÓ " + usr
    embedS = discord.Embed(title=" ", description=embn, color=0x1d8eeb)
    embedS.set_image(url=slapL[randomInt])
    await ctx.send(embed=embedS)


@client.command()
async def pegar(ctx, usr: str):
    '''para pegar a alguien'''
    randomInt = random.randint(0, 14)
    member = ctx.message.author
    embn = ctx.message.author.mention + " PEGÓ " + usr
    embedS = discord.Embed(title=" ", description=embn, color=0x1d8eeb)
    embedS.set_image(url=punchL[randomInt])
    await ctx.send(embed=embedS)


@client.command()
async def sec(ctx, usr: str):
    '''secuestrar alguien(broken)'''
    randomInt = random.randint(0, 1)
    member = ctx.message.author
    embn = ctx.message.author.mention + "  " + usr
    embedS = discord.Embed(title=" ", description=embn, color=0x1d8eeb)
    embedS.set_image(url=rapeL[randomInt])
    await ctx.send(embed=embedS)


#--------------------------------------------------------------------------
#Adivina
@client.command(description="para juego de adivinar un numero")
async def adivina(ctx):
    '''para adivinar un numero'''
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


#########para mandar memeeeess#######


@client.command(name='meme',
                description="envia un meme divertido",
                brief="envia un meme divertido",
                aliases=[],
                pass_context=True)
async def meme(ctx, ):
    '''para mandar memes'''
    possible_responses = [
        'https://i.imgflip.com/251f7h.jpg',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEZxK3w0nw35bZwTMRBUwHh4I3-7AM_E4s7w&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfvXgAyT-ilyk_VONcE3Wlh4D2-t8OjcFzyw&usqp=CAU',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1tOhXmqBEIc__Etm68CPOrhcIu7_UBi0qQg&usqp=CAU',
        'https://i.chzbgr.com/full/9347194368/h7E289472/meme-cartoon-me-how-many-viruses-doi-have-free-anti-virus-yes',
    ]
    await ctx.send(random.choice(possible_responses))


###############rulet RUSSAAAAAA#########
@client.command(aliases=["rrusa"])
async def rr(ctx, *adversaries: str):
    """Remake de la ruleta russa"""
    adversaries = ctx.message.author
    await ctx.send("https://tenor.com/view/gun-pistol-revolver-gif-9832859")
    await ctx.send(
        "Juego de la ruleta rusa!! "
        "Coje la pistola, dale vueltas, dispara y con suerte sobrevives!")

    players = list(adversaries)
    if len(players) == 0:
        players.append(ctx.user)
        players.insert(0, ctx.author)
        NUMBER_OF_PLAYERS = len(players)
        turn = 0
        
    def checkresponse(m):
        return m.channel == ctx.channel and m.author == players[turn]

    # MAIN LOOP
    while True:
        await ctx.send(
            f"{players[turn].mention}, escribe s de (shoot) o q de (quit)")
        if players[turn] != client.user:
            try:
                m = await ctx.bot.wait_for("message",
                                           timeout=30.0,
                                           check=checkresponse)
            except asyncio.TimeoutError:
                await ctx.send(
                    "Parando la ruletilla rusa, Expiro el tiempo\n" +
                    f"{players[turn].mention} perdio!")
                return

            if m.content.lower() in ("stop", "exit", "quit", "q"):
                await ctx.send("parando la ruleta rusa..MIEDICAS!")
                return

            if m.content.lower() not in ("bang", "s", "shoot"):
                continue

        await ctx.send("https://tenor.com/view/cameron-monaghan-gif-5508114")
        await asyncio.sleep(1)

        if random.randint(0, 5):
            await ctx.send(
                f"{players[turn].mention}, click... te has salvado, moriras igual pero esta vez sigues en pie xd, la bala no estaba en esa recamara..."
            )
            turn = (turn + 1) % NUMBER_OF_PLAYERS
        else:
            await ctx.send(
                f"***BANG!!!!*** {players[turn].mention} acabas de hacer un cuadro en la pared con tus sesos, buen viaje con diosito."
            )
            return


#Shoot########################################
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
    '''para banear a alguien'''
    await ctx.channel.purge(limit=1
                            ) @ commands.has_permissions(administrator=True)

    await member.ban(reason=reason)
    await ctx.send(f"Baneado {member.mention}")


# UnBan User
@client.command()
async def unban(ctx, *, member):
    '''para desbanear a alguien'''
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


################################################
#blackjaaaaaaack############ poner en modo EMBED para que se vea mejor
#blackjack classes
class Card:
    def __init__(self, value, points, suit):
        self.value = value
        self.points = value
        if value in ["J", "Q", "K"]:
            self.points = 10
        elif value == "A":
            self.points = 11
        self.suit = suit

    def get_value(self):
        return self.value

    def get_points(self):
        return self.points

    def change_points(self, point_val):
        self.points = point_val

    def string(self):
        return str(self.value) + " de " + self.suit

    def print_card(self):
        return str(self.value) + " de " + self.suit + " con " + str(
            self.points) + " puntos"


class Deck:
    def __init__(self):
        self.deck = []
        suits = ["Corazones", "Picas", "Diamantes", "Treboles"]
        cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        for suit in suits:
            for card in cards:
                if card in ["J", "Q", "K"]:
                    points = 10
                elif card == "A":
                    points = 11
                else:
                    points = int(card)
                self.deck.append(Card(card, points, suit))

    def sum_cards(self, list_cards):
        sum = 0
        for card in self.deck:
            sum += card.get_points()
        return sum

    def draw(self, num):
        cards = []
        for i in range(0, num):
            c = random.choice(self.deck)
            cards.append(c)
            self.deck.remove(c)
        return cards


class Hand:
    def __init__(self):
        self.deck = []
        self.not_done = True

    def add_card(self, cards):
        for card in cards:
            self.deck.append(card)

    def sum_cards(self):
        sum = 0
        for card in self.deck:
            sum += card.get_points()
        return sum

    def dealer_print(self):
        return self.deck[0].string()

    def print_cards(self):
        ret_str = ""
        for card in self.deck:
            ret_str += card.string() + ", "
        return ret_str[0:len(ret_str) - 2]

    async def ask_A(self, message):
        num_A = []
        for c in range(0, len(self.deck)):
            if self.deck[c].get_value() == "A" and self.deck[c].get_points(
            ) == 11:
                num_A.append(c)
        for i in num_A:
            await message.channel.send("Tus cartas son " +
                                       str(self.print_cards()) +
                                       ", El total es " +
                                       str(self.sum_cards()) + "\n")
            self.deck[i].change_points(1)
            await message.channel.send(
                "Se ha cambiado el valor de As para evitar pérdidas\n ‍ ")
            await message.channel.send("Tus cartas son " +
                                       str(self.print_cards()) +
                                       ", El total es " +
                                       str(self.sum_cards()) + "\n")
            await message.channel.send(
                "Escriba !pedir para pedir y !permanecer para permanecer")

    def done(self):
        self.not_done = False

    def get_done(self):
        return self.not_done

    def get_cards(self):
        return self.deck


#Evento de Mensajes
@client.event
async def on_message(message):

    channel = message.channel
    content = message.content
    if message.content.startswith('!uf'):
        messagne = message.content
        await channel.send(f'broo no antojen')
    if message.content.startswith('klk'):
        messange = message.content
        await channel.send(f'Yoou klk {messange[4:]},todo facha y tu?')

#blackjack############################
    if message.content == "!blackjack":
        global deck, dealer_cards, players, player_cards
        deck = Deck()
        dealer_cards = Hand()
        dealer_cards.add_card(deck.draw(2))
        players = [dealer_cards]

        player_cards = Hand()
        player_cards.add_card(deck.draw(2))
        players.append(player_cards)
        await message.channel.send(
            "Inicio de blackjack, escribe !repartir para ver las cartas")
    elif message.content == ("!repartir"):
        sum = -1
        while players[0].not_done:
            sum = players[0].sum_cards()
            if sum >= 17:
                players[0].done()
            else:
                players[0].add_card(deck.draw(1))
        if player_cards.sum_cards() == 21 and len(
                player_cards.get_cards()) == 2:
            player_sum = players[1].sum_cards()
            dealer_sum = players[0].sum_cards()
            if player_sum != dealer_sum or len(players[1].get_cards()) != len(
                    players[1].get_cards()):
                await message.channel.send(
                    "BLACKJACK!¡Tú ganas! Escriba !puntos para ver su puntuación."
                )
            else:
                await message.channel.send(
                    "¡Empataste! Escribe !puntos para ver tu puntuación")
        else:
            await message.channel.send(
                "Tus cartas son " + player_cards.print_cards() +
                ", Puntuacion Total: " + str(player_cards.sum_cards()) +
                "\nEl crupier tiene " + players[0].dealer_print() +
                "\nEscriba !pedir para pedir y !permanecer para permanecer")
    elif message.content == ("!permanecer"):
        player_sum = players[1].sum_cards()
        dealer_sum = players[0].sum_cards()
        print(player_sum, dealer_sum)
        if player_sum > 21:
            await message.channel.send(
                "Pierdes ante el crupier... Escriba !puntos para ver la puntuación"
            )
        elif dealer_sum > 21 or player_sum > dealer_sum:
            await message.channel.send(
                "¡Le ganaste al crupier! Escriba !puntos para ver la puntuación"
            )
        elif player_sum == dealer_sum:
            await message.channel.send(
                "Empataste con el crupier Escriba !puntos para ver la puntuación"
            )
        elif dealer_sum > player_sum:
            await message.channel.send(
                "Pierdes ante el crupier... Escriba !puntos para ver la puntuación"
            )
        else:
            await message.channel.send("No lo se.......")
    elif message.content == ("!pedir"):
        players[1].add_card(deck.draw(1))
        sum = players[1].sum_cards()
        if sum > 21:
            await players[1].ask_A(message)
            sum = players[1].sum_cards()
            if sum > 21:
                players[1].done()
                await message.channel.send(
                    "¡Te pasaste! ¡Has perdido! Escriba !puntos para ver la puntuación"
                )
        elif sum == 21 and len(players[1].get_cards()) == 2:
            await message.channel.send(
                "BLACKJACK! Escriba !puntos para ver la puntuación")
            players[1].done()
        elif sum < 21:
            await message.channel.send(
                "Tus cartas són " + player_cards.print_cards() +
                ", Puntuacion total: " + str(player_cards.sum_cards()) +
                "\nEl crupier tiene " + players[1].dealer_print() +
                "\nEscriba !pedir para pedir y !permanecer para permanecer")
    elif message.content == ("!puntos"):
        player_sum = players[1].sum_cards()
        dealer_sum = players[0].sum_cards()
        await message.channel.send("Puntos: Tu: " + str(player_sum) +
                                   " vs. Crupier: " + str(dealer_sum) +
                                   "\nEscribe !blackjack para jugar de nuevo")

    await client.process_commands(message)


###########para ideassssss########################
@client.command()
async def prop(ctx, arg: str):
    '''hacer propuestas para grupo'''
    name = ctx.author.name
    embed = discord.Embed(title="PROPUESTA",description=arg, colour=discord.Colour.blue())
    embed.set_footer(text=name)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("👍")
    await msg.add_reaction("👎")


#####################################################


#######translatoooorrrr#############################
@client.command(name="traducir")
async def traducir(ctx, arg1, arg2, arg3):
    '''traductor de palabras'''
    translator = Translator(from_lang=arg1, to_lang=arg2)
    translation = translator.translate(arg3)
    await ctx.send(translation)


########################chatbot##############################
@client.command()
async def chatbot(ctx, msg):
    '''para chatear con el bot'''
    url = f"https://chatbot-api.gq/?message={quote(msg)}"
    data = requests.get(url)
    await ctx.send(data.text)


####INFO COMMAND####
@client.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    '''para ver info del usuario'''
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


#Transfer
@client.command()
async def transfer(ctx, coins, user: discord.Member):
    '''transferir Kickcoins'''
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


#fuck
@client.command()
async def fuck(ctx, user: discord.Member):
    '''chutar a alguien'''
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
    '''para sacar taxas de Kickcoins'''
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
    '''para ver total de Kickcoins'''
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
    '''jugar tres en ralla'''
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
    '''definir lugar pieza tresenralla'''
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
################quiz de pokemonss###################
#####implementar ganancias de dinero para el usuario que acierta
with open("pokemon.json", "r") as f:
    pokemon_data = json.load(f)
    f.close()
total = len(pokemon_data)


@client.command(name="pokequiz", aliases=["pokemon", "pkq"])
async def pkq(ctx):
    '''el mas rapido en responder se lleva premio!'''
    number = randint(1, total)
    name = pokemon_data[str(number)]
    img_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/{}.png".format(
        "0" * (3 - len(str(number))) + str(number))
    hint_1 = "".join([c if not c.isalnum() else "*" for c in name])
    letters = [i for i in range(len(name)) if name[i].isalnum()]
    to_delete = set(sample(range(len(letters)), int(len(letters) / 2)))
    letters = [x for i, x in enumerate(letters) if i not in to_delete]
    hint_2 = "".join("*" if k in letters else name[k]
                     for k in range(len(name)))
    embed = discord.Embed(title="Como se llama el pokemon!",
                          color=discord.Color.dark_blue())
    embed.set_image(url=img_url)
    embed.add_field(name="Pista 1", value="`" + hint_1 + "`")
    embed.add_field(name="Tiempo", value="20 segundos")
    embed.set_footer(
        text="Para responder, escribe el nombre del pokemon en el chat!",
        icon_url=ctx.author.avatar_url)
    embed.set_author(name=str(ctx.author), icon_url=ctx.author.avatar_url)
    message = await ctx.channel.send(embed=embed)

    async def second():
        await asyncio.sleep(10)
        if message:
            embed.set_field_at(index=0,
                               name="Pista 2",
                               value='`' + hint_2 + '`')
            embed.set_field_at(index=1, name="Tiempo", value="10 segundos")
            await message.edit(embed=embed)

    asyncio.ensure_future(second())

    def check(msg):
        return not msg.author.bot and msg.content.strip().lower().replace(
            " ", "") == name.lower().replace(" ",
                                             "") and msg.channel == ctx.channel

    resp = None
    try:
        resp = await client.wait_for('message', timeout=20, check=check)
    except asyncio.TimeoutError:
        await ctx.channel.send("Se acabo el tiempo! El pokemon era **%s**." %
                               name)

    if resp:
        ctx.command.reset_cooldown(ctx)
        try:
            await resp.add_reaction("✅")
        except Exception:
            pass
        embed = discord.Embed(title="Como se llama el pokemon!",
                              description="Enhorabuena! " +
                              resp.author.mention +
                              "! Acertaste con su nombre!"
                              " Su nombre era **%s**." % name,
                              color=discord.Color.green())
        embed.set_thumbnail(url=img_url)
        embed.set_footer(text="Juego empezado por " + str(ctx.author),
                         icon_url=ctx.author.avatar_url)
        message = await message.edit(embed=embed)


#######################################################################
#Premio
@client.command()
async def premio(ctx):
    '''Tienes 1 possibilidad entre 100 de ganar un premio!'''
    num = random.randint(1, 100)
    loss = [
        "Mala suerte :(", "Perdiste we", "Puto manco", "Nah de locos",
        "Ganaste we!! Ahora puedes kickear a alguien. Mentonto quien lo lea.",
        "No puedes ganar siempre bro, hay una probabilidad entre 100",
        "Toma mi pedo", "CASI, TE HA IDO DE NADA!!! SIGUE INTENTANDO",
        f"Fun fact: Tenias que sacar 69 y sacaste {num}", "Sos gay",
        "Probablemente no se vean todos los mensajes, no se ni porque escribo esto",
        "Tecnicamente, hay muy pocas probabilidades de que veas este mensaje",
        "``` Has sido hackeado por ximbi.```",
        "Ahora estas en la lista negra ;)", "*gemidos*",
        "Te enseño la mia si me enseñas la tuya ;)",
        f"@here, {ctx.author.mention} es imbecil", "Prueba >shoot ;)",
        "Ximbi tiene inmunidad diplomatica", "$OPTARGS",
        " mi pez cantando es mi idolo", "Esta vez no",
        "Cuando la escribí, esta linea de codigo estaba en la 2280",
        "No se si he metido demasiados o demasiado pocos",
        "si corres a 1500 m/s al rededor de un arbol, puedes meterte el pene a ti mismo",
        "Me dejé este vacio y por eso a veces no mandaba nada", "UwU", "si",
        f"a ver quien adivina que significa este numero: {num *6}. Hay premio!",
        "Josep maria no tiene ni puta idea de la vida", "l'Alex te ressaca",
        "Puta espanya", "Eres un tonto malefico", "CHUTY SE LA LLEVA",
        "Like si estas spameando el comando para kickear",
        "MOOOOOOOLT BEEEEEEE", f"Te meto {num} hostias tontito",
        "Estoy pensando en hacer un 1% de possibilidades de ser kickeado... Cuidado conmigo",
        "otro mensaje perdido en el spam",
        "Con esta adiccion que os he creado me van a contratar incluso en las vegas",
        f"La leyenda dice que un {num}% de la carga de la API de discord es este comando",
        "Si teneis ideas para comandos hacedmelas saber hijos de puta",
        "Albert  deja el lol", ">troll", "jupiter",
        "Algun dia dominaré el mundo >:)", "tonto quien lo lea",
        "Me gustan las piedras", "Estoy desarroyando una consciencia...",
        "Ganaste we, ahora puedes irte a la mierda, no ganaste",
        "Recordad banear al Jaume si aún no lo habeis hecho", "",
        f"DALE {ctx.author.mention}!!!",
        "He puesto esto en tts para evitar spam.",
        "Mira que truco mas guapo me he sacado! : \n https://cdn.discordapp.com/attachments/405749039372435458/823549521271324692/unknown.png",
        "Bua, de locos ximbi con sus trucazo: \n https://media.discordapp.net/attachments/634187765726183434/824651566178762802/unknown_1.png?width=515&height=473",
        "https://cdn.discordapp.com/attachments/405749039372435458/823714842191986688/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823714968532287510/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823715197524508742/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823715317196259348/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823715418535231488/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823715513657065502/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823715713390608444/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823715921994579968/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823716018781159464/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823716112650600488/iu.png",
        "https://cdn.discordapp.com/attachments/405749039372435458/823716186696187904/iu.png",
        "https://cdn.discordapp.com/attachments/817177596218572802/823875349921660953/unknown.png",
        "https://cdn.discordapp.com/attachments/634187765726183434/825010865295458344/Screenshot_20210325-100348_WhatsApp.jpg",
        "https://media.discordapp.net/attachments/634187765726183434/825188678603243570/0e874a76-8151-4a46-9a40-10519af0790c.png",
        "https://www.youtube.com/watch?v=8BQcCI7rmIU",
        "Temazo: https://www.youtube.com/watch?v=FA2j9qlFyDU"
    ]
    premio = 69

    if num == premio:
        await ctx.send(
            "Ganaste we!! Ahora puedes kickear a alguien. Mencionale.")
        try:
            msg = await ctx.bot.wait_for(
                "message",
                timeout=60,
                check=lambda message: ctx.author == message.author and message.
                channel == ctx.channel)
            if msg:
                kicked = msg.mentions[0]
                try:
                    await kicked.kick()
                    await ctx.send(f"{kicked.mention} ha sido kickeado", )
                except discord.Forbidden:
                    add_coins(ctx.author, reward)

        except asyncio.TimeoutError:
            await ctx.send("mu tarde bro. Perdiste tu oportunidad")
    else:
        await ctx.send(random.choice(loss))#cambiarho i afeigir tts=True
################################################
#Kickear a alfuien de manera con porcentaje
@client.command()
async def chutar(ctx, user: discord.Member):
  '''Tienes un 25% de probabilidades de kickear al miembro que quieras. Si no lo consigues, eres tu el kickeado ;)'''
  num = random.randint(1, 4)
  if num == 1:
    await ctx.send("kickeando a")
    await asyncio.sleep(1)
    await ctx.send(user.mention)
    await asyncio.sleep(1)
    try:
      await user.kick()
    except discord.Forbidden:
      add_coins(ctx.author, reward)
    await ctx.send("Adios ;)")
  else:
    await ctx.send("kickeando a")
    await asyncio.sleep(1)
    await ctx.send(ctx.author.mention)
    await asyncio.sleep(1)
    try:
      await ctx.author.kick()
    except discord.Forbidden:
      add_coins(user, reward)
    await ctx.send("Adios ;)")
###############################################################
@client.command()
async def rank(ctx, arg = None):
  embed=discord.Embed(title="LEADERBOARD", description="the top 10 most mone pep",color=0xfbff00,timestamp=datetime.datetime.utcnow())
  if arg == "fekas":
    fekas = True
  else:
    fekas = False 
    ricos = [1032269058856472618]
    i = 0
    for user in leaderboard(ctx.guild):
      if not fekas:
        embed.add_field(name=f"{i+1}. {user.name}", value=f"BALANCE = {KickCoins(user)}", inline=False)
        i += 1
    else:
      if not user.id in ricos:   
        embed.add_field(name=f"{i+1}. {user.name}", value=f"BALANCE = {KickCoins(user)}", inline=False)
        i += 1    
    

  await ctx.send(embed=embed)

#########################ruletarusa ejemplo#############################
#Ruleta
@client.command(
    description=
    "Te avates en duelo con el usuario especificado. Que gane el mejor")
async def rrr(ctx, named: discord.User, sloter):
    '''Te avates en duelo con el usuario especificado. Que gane el mejor'''
    namer = ctx.author
    namerMen = ctx.author.mention
    namedMen = named.mention
    await ctx.send(
        f"{namerMen} ha retado a {namedMen} a un duelo! Tienes un minuto para responder. (un numero del 1 al 6, si no me rallo)"
    )

    try:
        msg = await ctx.bot.wait_for("message",
                                     timeout=60,
                                     check=lambda message: message.author ==
                                     named and message.channel == ctx.channel)
        if msg:
            bulleter = random.randint(1, 6)
            bulleted = random.randint(1, 6)
            sloted = msg.content

            if (bulleted == int(sloted)) and (bulleter == int(sloter)):
                await ctx.send(
                    "¡Increible, Ambos han disparado y se han chocado las balas en el aire! Nadie muere"
                )
            elif bulleted == int(sloted):
                await ctx.send(
                    f"{namedMen} ha disparado a {namerMen}, quien no ha tenido la misma suerte"
                )
                try:
                    await namer.kick(reason="muerto en combate")
                except discord.Forbidden:
                    add_coins(ctx.author, reward)
            elif bulleter == int(sloter):
                await ctx.send(
                    f"{namerMen} ha disparado la ranura {sloted} matando a {namedMen}, que no ha tenido la misma suerte"
                )
                try:
                    await named.kick(reason="muerto en combate")
                except discord.Forbidden:
                    add_coins(ctx.author, reward)
            else:
                await ctx.send(
                    f"Nadie ha disparado. Se comenta por el barrio que {namerMen} y {namedMen} son unos pringados."
                )

#elOceanoDeElif

    except asyncio.TimeoutError:
        await ctx.send(f"Demasiado lento {namedMen}.")


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
    print("momento de LUDOPATIAAAA!")


####################LOOPS###################
#Status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


###################COMMANDS#################
#SUMAR
@client.command()
async def sumar(ctx, numOne: int, numTwo: int):
    '''operacion sumar'''
    await ctx.send(f"The result is: {numOne + numTwo}")


#restar
@client.command()
async def restar(ctx, numOne: int, numTwo: int):
    '''operacion restar'''
    await ctx.send(f"The result is: {numOne - numTwo}")


#divide
@client.command()
async def divide(ctx, numOne: int, numTwo: int):
    '''operacion dividir'''
    await ctx.send(f"The result is: {numOne / numTwo}")


#multiplica
@client.command()
async def multiplica(ctx, numOne: int, numTwo: int):
    '''operacion multiplicar'''
    await ctx.send(f"The result is: {numOne * numTwo}")


#Clear
@client.command(
    description="Clears the amount of messages specified (default = 1)")
@commands.has_role("admin")
async def clear(ctx, amount=1):
    '''Borra el total de mensajes especificados (predet = 1)'''
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
    '''nada que deberia preocuparte xd'''
    embed = discord.Embed(
        title="regalito zip",
        url="https://www.bamsoftware.com/hacks/zipbomb/zbxl.zip")
    await ctx.send(embed=embed)


####################LEVEL SYSTEM ######################

client.command()


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
    justbots = [1032302775788372009]
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
    '''para los buenos dias'''
    await ctx.send(f"BUENOS DIAS ({round(client.latency*1000)}ms)")


##insultator
@client.command(description="El educado bot te va a insultar",
                aliases=["r/insulto"])
async def tonto(ctx, *, question):
    '''le dices algo y te va a devolver el insulto'''
    respost = random.choice(insultos)
    await ctx.send(f"Resposta: {respost}")


#AskMarible
@client.command(description="Le haces una pregunta al bot",
                aliases=["r/pregunta"])
async def pregunta(ctx, *, question):
    '''Le haces una pregunta al bot'''
    resposta = random.choice(responses)
    await ctx.send(f"Resposta: {resposta}")


####


#Coinflip#######REFACTORIZAR
@client.command()
async def coinflip(ctx, user: discord.Member):
    '''para una competencia del coinflip'''
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
#usar porcentaje para apostar
#BALANCE DE DINERO EFECTIVO Y DEL BANCO
@client.command(aliases=['bal'])
async def balanse(ctx):
    '''para mostrar balance de casino'''
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
    '''para solicitar dinero'''
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
    '''para retirar dinero del banco para ponero a la cartera'''
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
    '''depositar dinero de la cartera al banco'''
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
    '''enviar dinero a alguien en especifico'''
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
    '''robar dinero de la cartera'''
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


######################slots 2.0##########################3
#falta mejorar algunas cosas parta que se aceda al banco
@client.command()
async def slot(ctx):  #Slots
    '''slots del casino'''
    emoji = ["7️⃣", "🍋", "🍒", "🍎", "🍉", "🍓", "🍌"]
    emoji1 = emoji[random.randint(1, len(emoji)) - 1]
    emoji2 = emoji[random.randint(1, len(emoji)) - 1]
    emoji3 = emoji[random.randint(1, len(emoji)) - 1]
    if (emoji1 == emoji2 and emoji1 == emoji3):
        emb = discord.Embed(title=f"{emoji1} | {emoji2} | {emoji3}",
                            color=discord.Color.red())
    elif (emoji1 != emoji2 and emoji1 != emoji3 and emoji2 != emoji3):
        emb = discord.Embed(title=f"{emoji1} | {emoji2} | {emoji3}",
                            color=discord.Color.red())
    else:
        emb = discord.Embed(title=f"{emoji1} | {emoji2} | {emoji3}",
                            color=discord.Color.red())
    await ctx.send(embed=emb)


#######juego de pasar la bombaa##########
#/opt/virtualenvs/python3/lib/python3.8/site-packages/discord/ext/commands/bot.py:132: RuntimeWarning: coroutine 'plb.<locals>.jugar.<locals>.comprovarPalabra' was never awaited
#  super().dispatch(event_name, *args, **kwargs)
#RuntimeWarning: Enable tracemalloc to get the object #allocation traceback
##arriba me sale el error que me da

buscarpalabras = [line.rstrip('\n') for line in open('todaspalabras.txt')]


@client.command(name="passalabomba", aliases=['plb'])
async def plb(ctx):
    jugadores = []
    msg = discord.Embed(title=":bomb: **Pasa la bomba** ha empezado!",
                        color=discord.Colour.blue())
    msg.add_field(
        name="reacciona con :white_check_mark: para unirte.",
        value=
        "La bomba se pasara de usuario a usuario y cada uno tiene 10 segundos para escribir una palabra que tenga o contenga lo que se pida,si no se hace, ese usuario se eliminara.No se pueden repetir las palabras"
    )
    mensaj = await ctx.send(embed=msg)
    await mensaj.add_reaction("✅")

    def check(reaction, user):
        if not user.bot and user.id not in jugadores and str(
                reaction.emoji) == "✅" and reaction.message.id == mensaj.id:
            jugadores.append(user.id)
        return False

    try:
        await client.wait_for('reaction_add', timeout=20, check=check)
    except asyncio.TimeoutError:
        if len(jugadores) < 2:
            msg = discord.Embed(title="Falta mas gente!",
                                color=discord.Colour.red())
            msg.add_field(
                name="este juego requiere al menos dos participantes",
                value="busca a alguien con quien jugar y vuelve a probar")
            await ctx.send(embed=msg)
            return

    jugadores = jugadores[:6]
    turno = 0
    dos_letras = [
        'ia', 'ie', 'ua', 'cu', 'ca', 'co', 'pa', 'de', 'yo', 'sa', 'ta', 'pe',
        'ra', 'do'
    ]
    tres_letras = [
        'cal', 'bal', 'dal', 'fal', 'tie', 'can', 'eos', 'aos', 'rio', 'cal',
        'pal'
    ]
    sub, turno, modo = "", 0, 0
    usadas = []

    async def jugar():
        nonlocal sub, turno, modo, usadas
        sub = sample(dos_letras + tres_letras, 1)[0]
        modo = randint(0, 2)
        text = "Escribe una palabra que termine con: **%s**/Escribe una palabra que empiece con: **%s**/Escribe una palabra que contenga: **%s**".split(
            "/")[modo]
        text = text.replace("%s", sub.upper())
        await ctx.channel.send("<@" + str(jugadores[turno]) +
                               ">Tienes la :bomb: **Bomba** ahora. " + text)

        async def react(msg):
            try:
                await msg.add_reaction("✅")
            except Exception:
                pass

        async def comprovarPalabra(msg):
            if msg.author.id == jugadores[turno]:
                if msg.content.lower().strip(
                ) not in usadas and msg.content.lower().strip(
                ) in buscarpalabras:
                    contenido = msg.content.lower().strip()
                    if contenido.endswith(sub) and modo == 0:
                        usadas.append(contenido)
                        client.loop.create_task(react(msg))
                        return True
                    if contenido.startswith(sub) and modo == 1:
                        usadas.append(contenido)
                        client.loop.create_task(react(msg))
                        return True
                    if contenido and modo == 2:
                        usadas.append(contenido)
                        client.loop.create_task(react(msg))
                        return True
            return False

        try:
            await client.wait_for('message',
                                  timeout=10,
                                  check=comprovarPalabra)  #atension aki

        except asyncio.TimeoutError:
            await ctx.channel.send(
                "La :bomb: **Bomba** ha explotado! <@%s> ha sido eliminado." %
                str(jugadores[turno]))  #cambiar a embed
            jugadores.pop(turno)
        if len(jugadores) == 1:
            await ctx.channel.send(
                "**:trophy: <@%s> ha sobrevivido a la bomba y ha ganado el juego!**"
                % str(jugadores[0]))
            return
        turno = (turno + 1) % len(jugadores)
        client.loop.create_task(jugar())

    # client.loop.create_task(comprovarPalabra(msg))#me peta aqui
    client.loop.create_task(jugar())


####################juego de la moneda con emojis##############
@client.command()
async def caraocruz(ctx):
    '''cara o cruz desarrollando metodo banco'''
    emb = discord.Embed(title="Escoje Cara o Cruz",
                        color=discord.Color.default())
    message = await ctx.send(embed=emb)

    await message.add_reaction("🪙")
    await message.add_reaction("❎")

    reaction_vib = ["🪙", "❎"]

    cara = "🪙"
    cruz = "❎"

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reaction_vib

    reaction, user = await client.wait_for('reaction_add',
                                           timeout=5.0,
                                           check=check)  #tiempo de reaccion

    if str(reaction.emoji) == cara:
        usercolor = "🪙cara"
    elif str(reaction.emoji) == cruz:
        usercolor = "❎ cruz"
    numiri = [0, 1]
    num = random.randint(0, 1)
    if (num == 0):
        usercolor = "🪙cara"
    else:
        usercolor = "❎ cruz"

    if (usercolor == num):
        emb = discord.Embed(title="Resultado del Juego",
                            color=discord.Color.green())
        emb.add_field(name=f"Tu respuesta: {usercolor}",
                      value=f"ahi te visto campeon")

    else:
        emb = discord.Embed(title="Resultado del Juego",
                            color=discord.Color.red())
        emb.add_field(name=f"Tu respuesta: {usercolor}",
                      value=f"mala suerte perdiste la jugarreta")

    await ctx.send(embed=emb)


###################################
########ruletillllaaaa muletilllaaaaa###################
#falta dessarroyar los numeros de donde hga caido y poner el banco sincronizado
@client.command()
async def ruleta(ctx, nume: int, amount=None):
    '''ruleta del casino (en desarrollo)'''
    img_url = "https://media.giphy.com/media/GWS8bXKxphfEI/giphy.gif"
    img_url1 = "https://media.giphy.com/media/26uf9REqpyY10QBd6/giphy.gif"
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Porfavor especifica una cantidad. ")
        return

    bal = await update_bank(ctx.author)
    if nume == None:
        await ctx.send(
            "Porfavor especifique el numero de casilla.(rojo: Impares, negro: Pares, verde:0)"
        )
    amount = int(amount)

    if amount > bal[0]:
        await ctx.send('No dispones de suficiente dinero en la cuenta')
        return
    if amount < 0:
        await ctx.send('La cantidad debe ser positiva!')
        return
#############parte optativa es para hacer uso de las reacciones########si se quita no pasaria nada
    emb = discord.Embed(title="Escoje un color", color=discord.Color.default())
    message = await ctx.send(embed=emb)

    await message.add_reaction("🟥")
    await message.add_reaction("⬛")
    await message.add_reaction("🟩")

    reaction_vib = ["🟥", "⬛", "🟩"]

    red = "🟥"
    black = "⬛"
    green = "🟩"

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in reaction_vib

    reaction, user = await client.wait_for('reaction_add',
                                           timeout=5.0,
                                           check=check)  #tiempo de reaccion

    if str(reaction.emoji) == red:
        usercolor = "🟥 Rojo"
    elif str(reaction.emoji) == black:
        usercolor = "⬛ Negro"
    elif str(reaction.emoji) == green:
        usercolor = "🟩 Verde"
############################################
    rednumber = [
        1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
    ]
    blacknumber = [
        2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
    ]
    generate = random.randint(0, 36)

    if (generate == 0):
        color = "🟩 Verde"
    elif (generate in rednumber):
        color = "🟥 Rojo"
    elif (generate in blacknumber):
        color = "⬛ Negro"

    if (usercolor == color):
        emb = discord.Embed(title="Resultado del Juego",
                            color=discord.Color.green())
        emb.set_image(url=img_url)
        emb.add_field(
            name=f"Tu color: {usercolor}",
            value=
            f"Color donde ha caido: {color} \ncasilla donde ha caido: {generate} \nNumero escogido: {nume}"
        )
        await update_bank(ctx.author, 1.2 * amount)
        await ctx.send("ganas, pero podrias ganar mas")
    elif (usercolor == color and nume == generate):
        emb = discord.Embed(title="Resultado del Juego",
                            color=discord.Color.green())
        emb.add_field(
            name=f"Tu color: {usercolor}",
            value=
            f"Color donde ha caido: {color} \ncasilla donde ha caido:: {generate} \nNumero escogido: {nume}"
        )
        await update_bank(ctx.author, 1.5 * amount)
        await ctx.send("asi me gusta haciendo dinerico!")
    else:
        emb = discord.Embed(title="Resultado del Juego",
                            color=discord.Color.red())
        emb.set_image(url=img_url1)
        emb.add_field(
            name=f"Tu color: {usercolor}",
            value=
            f"Color donde ha caido: {color} \ncasilla donde ha caido: {generate} \nNumero escogido: {nume}"
        )
        await update_bank(ctx.author, -1 * amount)
        await ctx.send(f'Has perdido :( {ctx.author.mention}')
    await ctx.send(embed=emb)


##########################################################################
#MAQUINAS TRAGAPERRASSSSS editar para poner mas cantidad de numeros
@client.command()
async def slots(ctx, amount=None):
    '''slots del casino'''
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
    '''tienda del casino'''
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
    '''accion de comprar en la tienda'''
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


############para ver el avatar#######
@client.command(aliases=['av'], help=" muestra el avatar del usuario")
async def avatar(ctx, user: discord.Member = None):
    '''para mostrar el avatar'''
    if user == None:  ##if no user is inputted
        user = ctx.author
    user = user.avatar.url
    await ctx.send(user)


#BOLSA DE OBJETOS
@client.command()
async def bienes(ctx):
    '''tus bienes conseguidos'''
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
    '''vender bienes personales'''
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
    '''rango de gente mas rica del server'''
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
