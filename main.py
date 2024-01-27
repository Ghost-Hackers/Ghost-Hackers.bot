# Standard Library Imports
import os
import datetime
import platform
import psutil
import json

# Third-Party Library Imports
import discord
from discord.ext import commands, tasks
from interactions import Client
from interactions.models import SlashCommand
from discord import Game
from dotenv import load_dotenv

# Internal Imports
# Load environment variables from .env
load_dotenv()

# Access the token from the environment
token = os.getenv('DISCORD_BOT_TOKEN')

# Check if the token is available
if token is None:
    print("Error: Discord bot token not found. Make sure to set it in the .env file.")
else:
    # Open and read config.json
    with open('config/config.json', 'r') as config_file:
        config = json.load(config_file)

    # Use your token in your Discord bot setup...
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user.name} ({bot.user.id})')

    bot.run(token)

# Path: src/GhostHackers_Bot.py
from src.GhostHackers_Bot import start_bot

BOT_VERSION = "v0.2.0"
COGS_DIRECTORY = 'cogs'
CHANNEL_ID = 1102907872809062520
USER_ID = 597996927375900682

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config', 'config.json')

# Initialize bot and slash commands
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='*', intents=intents)
interaction_bot = Client(bot)
bot_token = os.getenv("DISCORD_BOT_TOKEN")

# Load cogs from the 'cogs' directory
for filename in os.listdir(COGS_DIRECTORY):
    if filename.endswith('.py'):
        cog_name = filename[:-3]  # Remove '.py' extension
        bot.load_extension(f'{COGS_DIRECTORY}.{cog_name}')

# Bot events and configurations can be added here
@bot.event
async def on_ready():
    user_mention = bot.get_user(USER_ID).mention

    # Get relevant information
    ping_time = round(bot.latency * 1000, 2)
    server_count = len(bot.guilds)
    user_count = sum(guild.member_count for guild in bot.guilds)
    uptime = datetime.datetime.utcnow() - bot.start_time

    # Get system information
    system_info = f"{platform.system()} {platform.version()} ({platform.architecture()[0]})"
    process = psutil.Process()
    memory_info = f"{round(process.memory_info().rss / (1024 ** 2), 2)} MB"

    # Get library versions
    discord_version = discord.__version__

    # Create an embed
    embed = discord.Embed(title="Ghost Hackers Back Online", color=discord.Color.dark_blue())
    embed.set_author(name="Codergeist Phantom", icon_url=bot.user.avatar_url)
    embed.description = f"The ethereal journey continues as {user_mention} and the Codergeist Phantom returns online!\n\n"

    # Add startup information
    embed.add_field(name="🌐 Ping Time", value=f"{ping_time} ms", inline=True)
    embed.add_field(name="🛡️ Server Count", value=server_count, inline=True)
    embed.add_field(name="👥 User Count", value=user_count, inline=True)
    embed.add_field(name="⏱️ Uptime", value=str(uptime), inline=True)

    # Add system information
    embed.add_field(name="💻 System", value=system_info, inline=False)
    embed.add_field(name="🧠 Memory Usage", value=memory_info, inline=False)

    # Get library versions
    discord_version = discord.__version__

    # Add library versions
    embed.add_field(name="📚 Discord Library Version", value=discord_version, inline=True)
    embed.add_field(name="🤖 Bot Version", value=BOT_VERSION, inline=True)

    # Add footer
    embed.set_footer(text="May the code guide us through the spectral realms...")

    # Send the embed to a specific channel
    channel = bot.get_channel(CHANNEL_ID)

    if channel:
        await channel.send(embed=embed)

    await bot.change_presence(activity=Game(name="with code"))

# Interaction handling
@interaction_bot.event
async def on_interaction(interaction):
    if interaction["type"] == 1:  # Ping interactions
        await interaction.create_response("Pong!")  # Replace with your actual response
    elif interaction["type"] == 2:  # Slash command interactions
        command_name = interaction["data"]["name"]
        command_args = interaction["data"]["options"]
        await interaction.create_response("Command received!")
    else:
        await interaction.create_response("Unknown interaction type received.")
        
# Ensure this code is only executed when the script is run directly
if __name__ == "__main__":
    load_dotenv()
    discord_secret = os.getenv("DISCORD_CLIENT_SECRET")
    start_bot(discord_secret)