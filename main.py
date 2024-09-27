import discord
from discord.ext import commands
import asyncio
import os
import urllib.parse

# Charger le token depuis un fichier
with open('token.txt', 'r') as file:
    token = file.read().strip()

intents = discord.Intents.all()
intents.guilds = True
intents.guild_messages = True
intents.voice_states = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')
    await bot.tree.sync()
    print('Commandes slash enregistrées !')


async def join_voice_and_speak(interaction: discord.Interaction, texte: str, langue: str, message: str) -> None:
    member = interaction.user

    if member.voice is None:
        await interaction.response.send_message("<!> BE: Vous devez être dans un canal vocal pour utiliser cette commande <!>", ephemeral=True)
        return

    channel = member.voice.channel
    voice_client = await channel.connect()

    phrases = texte.split('.')

    async def play_next_sentence():
        for sentence in phrases:
            sentence = sentence.strip()
            if sentence:
                url = f"http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q={urllib.parse.quote(sentence)}&tl={langue}"
                voice_client.play(discord.FFmpegPCMAudio(url))

                while voice_client.is_playing():
                    await asyncio.sleep(1)

    await interaction.response.send_message(message, ephemeral=True)
    await play_next_sentence()
    await voice_client.disconnect()

@bot.tree.command(name='fr', description='Parler dans la voc')
async def speak_fr(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'fr', "Je viens en voc !")

@bot.tree.command(name='en', description='Speak in english')
async def speak_en(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'en', "I m comming bro !")

@bot.tree.command(name='ar', description='Parler en arabe')
async def speak_ar(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'ar', "Je viens en voc !")

@bot.tree.command(name='de', description='Parler en allemand')
async def speak_de(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'de', "Je viens en voc !")

@bot.tree.command(name='ru', description='Parler en russe')
async def speak_de(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'ru', "Je viens en voc !")

@bot.tree.command(name='es', description='Parler en espagnol')
async def speak_de(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'es', "Je viens en voc !")

@bot.tree.command(name='nl', description='Parler en néerlandais')
async def speak_de(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'nl', "Je viens en voc !")

@bot.tree.command(name='it', description='Parler en russe')
async def speak_de(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'it', "Je viens en voc !")

@bot.tree.command(name='ja', description='Parler en russe')
async def speak_de(interaction: discord.Interaction, texte: str):
    await join_voice_and_speak(interaction, texte, 'ja', "Je viens en voc !")


bot.run(token)
