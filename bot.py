import random

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