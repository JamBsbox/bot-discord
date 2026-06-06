import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.command()
async def bonjour(ctx):
    await ctx.send(f"Bonjour {ctx.author.name} !")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong ! 🏓")

@bot.command()
async def gg(ctx, membre: discord.Member):
    await ctx.send(f"🏆 GG à {membre.mention} ! Bien joué !")

@bot.command()
async def pile_ou_face(ctx):
    resultat = random.choice(["Pile 🪙", "Face 🪙"])
    await ctx.send(f"C'est... **{resultat}** !")

@bot.command()
async def stats(ctx, membre: discord.Member):
    précision = random.randint(0, 100)
    vitesse = random.randint(0, 100)
    skill = random.randint(0, 100)
    chance = random.randint(0, 100)
    await ctx.send(
        f"📊 **Stats de {membre.display_name}** :\n"
        f"🎯 Précision : {précision}%\n"
        f"⚡ Vitesse : {vitesse}%\n"
        f"🎮 Skill : {skill}%\n"
        f"🍀 Chance : {chance}%"
    )

bot.run(os.environ["DISCORD_TOKEN"])