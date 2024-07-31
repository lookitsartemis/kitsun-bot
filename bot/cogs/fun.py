import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import aiohttp
import json
import random
import os

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        self.topics = self.load_topics()

    def load_topics(self):
        json_path = os.path.join(os.path.dirname(__file__), '..', 'json', 'topics.json')
        with open(json_path, 'r') as file:
            data = json.load(file)
        return data["topics"]
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.avatar = self.bot.user.avatar
        
    
    @nextcord.slash_command(description='Get a random fox image!')
    async def fox(self, interaction: Interaction):
        api_url = 'https://randomfox.ca/floof/'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                if response.status != 200:
                    await interaction.response.send_message("Failed to fetch fox image.", ephemeral=True)
                    return
                
                data = await response.json()
                fox_image_url = data['image']
                
                embed = nextcord.Embed(
                    title="Fox",
                    color=self.color
                                       )
                embed.set_image(url=fox_image_url)
                
                await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description='Get a random conversation topic.')
    async def topic(self, interaction: Interaction):
        random_topic = random.choice(self.topics)
        
        embed = nextcord.Embed(
            title="Topic",
            description=random_topic,
            color=self.color
        )
        embed.set_thumbnail(url=self.avatar)
        
        await interaction.response.send_message(embed=embed)
       
    @nextcord.slash_command(description='Ask the Magic 8-Ball a question.')
    async def eightball(self, interaction: Interaction, question: str):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        
        response = random.choice(responses)
        
        embed = nextcord.Embed(
            title="8-Ball",
            description=f"**Question**: {question}\n**Answer**: {response}",
            color=self.color
        )
        
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description='Flip a coin.')
    async def coinflip(self, interaction: Interaction):
        outcome = random.choice(["Heads", "Tails"])
        
        embed = nextcord.Embed(
            title="Coin Flip",
            description=f"The coin landed on: **{outcome}**!",
            color=self.color
        )
        
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(name="howgay", description="Check how gay you are with a fun percentage.")
    async def howgay(self, interaction: Interaction):
        percentage = random.randint(0, 100)
        avatar = interaction.user.avatar.url
        
        embed = nextcord.Embed(
            title="How Gay",
            color=self.color,
            description=f"You are {percentage}% gay! "
        )
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)
        
def setup(bot):
    bot.add_cog(Fun(bot))