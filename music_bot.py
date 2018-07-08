import discord
from discord.ext import commands
import os

class MinnesingerBot:

    def __init__(self):
        self.bot_creds_file = "bot_credentials.txt"
        self.playlist_folder = 'playlist/'
        self.playlist_names = []

    def get_bot_credentials(self):
        file = open(self.bot_creds_file, "r")
        read_lines = [line.strip() for line in file.readlines()]
        return read_lines

    def get_command_with_args(self, message_content):
        return None

    def action(self):
        [bot_token, voice_channel_id] = self.get_bot_credentials()

        Client = discord.Client()
        client = commands.Bot(command_prefix="?")

        @client.event
        async def on_ready():
            print("Minnesinger music bot is ready to play.")

        @client.event
        async def on_message(message):
            command = message.content.upper().split(" ")
            if command[0] == "REPORT":
                await client.send_message(message.channel, "Aye aye, sir!")
            if command[0] == "JOIN":
                self.voice = await client.join_voice_channel(client.get_channel(voice_channel_id))
            if command[0] == "LEAVE":
                await self.voice.disconnect()
            if command[0] == "SHOW_MUSIC":
                for file in os.listdir(self.playlist_folder):
                    if file.endswith(".mp3"):
                        self.playlist_names.append(file)
                await client.send_message(message.channel, "\n".join(name for name in self.playlist_names))
            if command[0] == "LOAD":
                what_to_play = self.playlist_folder + command[1]
                self.player = self.voice.create_ffmpeg_player(what_to_play)
            if command[0] == "PLAY":
                self.player.start()
            if command[0] == "STOP":
                self.player.stop()

        client.run(bot_token)


# mpd = MinnesingerBot()
# mpd.action()
