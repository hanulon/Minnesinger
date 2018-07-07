import discord
from discord.ext import commands
import os

class MinnesingerBot:


    def action(self):
        playlist_folder = 'playlist/'
        playlist_names = []

        Client = discord.Client()
        client = commands.Bot(command_prefix="?")

        @client.event
        async def on_ready():
            print("Bot is ready!")

        @client.event
        async def on_message(message):
            command = message.content.upper().split(" ")
            if command[0] == "REPORT":
                await client.send_message(message.channel, "Aye aye, sir!")
            if command[0] == "JOIN":
                self.voice = await client.join_voice_channel(client.get_channel("VOICE CHANNEL ID"))
            if command[0] == "LEAVE":
                await self.voice.disconnect()
            if command[0] == "SHOW_MUSIC":
                for file in os.listdir(playlist_folder):
                    if file.endswith(".mp3"):
                        playlist_names.append(file)
                await client.send_message(message.channel, "\n".join(name for name in playlist_names))
            if command[0] == "LOAD":
                what_to_play = playlist_folder + command[1]
                self.player = self.voice.create_ffmpeg_player(what_to_play)
            if command[0] == "PLAY":
                self.player.start()
            if command[0] == "STOP":
                self.player.stop()

        client.run("YOUR BOT CREDENTIALS")


mpd = MinnesingerBot()
mpd.action()