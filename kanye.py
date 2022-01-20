from redbot.core import commands
import discord
import requests
import json

from requests.structures import CaseInsensitiveDict




class Kanye(commands.Cog):
    """kanye west quotes"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def kanye(self, ctx):
        """Send a random kanye quote"""
        # Your code will go here
        kanye = "https://api.kanye.rest"
        response = requests.get(kanye)
        data = response.json()
        await ctx.send(data['quote'])

