import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import time

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        self.start_time = time.time()   
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.avatar = self.bot.user.avatar
        
    @nextcord.slash_command(description="The bot's stats.")
    async def stats(self, interaction: Interaction):
        
        name = self.bot.user.mention
        id = self.bot.user.id
        created_at = self.bot.user.created_at
        discord_timestamp = f"<t:{int(created_at.timestamp())}:F>"
        user_count = sum(guild.member_count for guild in self.bot.guilds)
        uptime = int(time.time() - self.start_time)
        latency = int(self.bot.latency * 1000)
        
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        formatted_uptime = f"{hours}h {minutes}m {seconds}s"
        
        embed = nextcord.Embed(
            title="Stats",
            color=self.color
        )
        embed.set_thumbnail(self.avatar)
        embed.add_field(name="Name", value=name)
        embed.add_field(name="ID", value=id)
        embed.add_field(name="Ping", value=f"{latency}ms")
        embed.add_field(name="Creation", value=discord_timestamp)
        embed.add_field(name="Users", value=user_count)
        embed.add_field(name="Uptime", value=formatted_uptime)
        
        await interaction.response.send_message(embed=embed)
      
    @nextcord.slash_command(description="Get server information.")
    async def server(self, interaction: Interaction):
        
        server = interaction.guild
        icon = server.icon.url
        name = server.name
        members = server.member_count

        embed = nextcord.Embed(
            title="Server",
            color=self.color
        )
        embed.add_field(name="Name", value=name)
        embed.add_field(name="Members", value=members)
        embed.set_thumbnail(url=icon)
        
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Gets the members information.")
    async def user(self, interaction: Interaction, member: Member = None):
        
        if member is None:
            member = interaction.user
            
        name = member.mention
        avatar = member.avatar.url
        
        embed = nextcord.Embed(
            title="Name",
            color=self.color
        )
        embed.add_field(name="User", value=name)
        embed.set_thumbnail(url=avatar)
        
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Get the users avatar.")
    async def avatar(self, interaction: Interaction, member: Member = None):
        
        if member is None:
            member = interaction.user
        
        user = member.global_name
        avatar = member.avatar.url
        
        
        embed = nextcord.Embed(
            title=f"@{user}'s Avatar",
            color=self.color
        )
        embed.set_image(url=avatar)
        
        await interaction.response.send_message(embed=embed)
        
    @nextcord.slash_command(description="Get a list of hotlines.")
    async def hotlines(self, interaction: Interaction):\
        await interaction.response.send_message("You are not alone, here is a list of helplines: Coming soon!")
        
def setup(bot):
    bot.add_cog(Utilites(bot))