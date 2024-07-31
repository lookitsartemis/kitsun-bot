import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xfd9d63
        
    @commands.Cog.listener()
    async def on_member_join(self, member: Member):

        channel_id = 1268244661403910255
        channel = self.bot.get_channel(channel_id)
        
        embed = nextcord.Embed(
            title="Welcome",
            description=f"Hello {member.mention}, welcome to the server!",
            color=self.color
        )
        embed.set_thumbnail(url=member.avatar.url)
        
        await channel.send(
            content=member.mention,
            embed=embed
        )
        
def setup(bot):
    bot.add_cog(Welcomer(bot))