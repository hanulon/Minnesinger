import discord
from discord.ext import commands
import os

class MinnesingerBot:

    def __init__(self):
        self.bot_creds_file = "bot_credentials.txt"
        self.playlist_folder = 'playlist/'
        self.playlist_names = []
        self.command_char = '/'

    def get_bot_credentials(self):
        file = open(self.bot_creds_file, "r")
        read_lines = [line.strip() for line in file.readlines()]
        file.close()
        return read_lines

    def get_command_with_args(self, message_content):
        stripped_message = message_content.strip()
        if stripped_message.__len__() > 1:
            if stripped_message[0] == self.command_char:
                tokenized_message = stripped_message.lower().split(" ")
                return tokenized_message[0][1:], tokenized_message[1:]
        return None, []

    def action(self):
        [bot_token, voice_channel_id] = self.get_bot_credentials()

        Client = discord.Client()
        client = commands.Bot(command_prefix="?")

        @client.event
        async def on_ready():
            print("Minnesinger music bot is ready to play.")

        @client.event
        async def on_message(message):
            command = self.get_command_with_args(message.content)
            if command[0] == "report":
                await client.send_message(message.channel, "Aye aye, sir!")
            if command[0] == "join":
                self.voice = await client.join_voice_channel(client.get_channel(voice_channel_id))
            if command[0] == "leave":
                await self.voice.disconnect()
            if command[0] == "show_music":
                for file in os.listdir(self.playlist_folder):
                    if file.endswith(".mp3"):
                        self.playlist_names.append(file)
                await client.send_message(message.channel, "\n".join(name for name in self.playlist_names))
            if command[0] == "load":
                what_to_play = self.playlist_folder + command[1]
                self.player = self.voice.create_ffmpeg_player(what_to_play)
            if command[0] == "play":
                self.player.start()
            if command[0] == "STOP":
                self.player.stop()

        client.run(bot_token)


# mpd = MinnesingerBot()
# mpd.action()
