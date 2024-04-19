import discord
import base64
import codecs
import logging
import json

# Dictionary to map each character to an emoji.
emoji_dict = {
    'a': '🔒', 'b': '👮', 'c': '🍓', 'd': '🍉', 'e': '🟥', 'f': '🧯', 'g': '🍍', 'h': '🥝', 'i': '🔥', 'j': '🥢',
    'k': '🍬', 'l': '🍅', 'm': '🔑', 'n': '🍨', 'o': '🌌', 'p': '🍪', 'q': '🍿', 'r': '🍚', 's': '🍡', 't': '🍩',
    'u': '🍤', 'v': '🐣', 'w': '🥞', 'x': '🤘', 'y': '💣', 'z': '🥬', ' ': '🐷', 'A': '⭐', 'B': '🍐', 'C': '👂', 'D': '🍇',
    'E': '🍄', 'F': '🥖', 'G': '🍠', 'H': '🍯', 'I': '🌼', 'J': '🦂', 'K': '🏀', 'L': '🍦', 'M': '🍰', 'N': '🚗', 'O': '🍫',
    'P': '🍭', 'Q': '🌋', 'R': '🍘', 'S': '🍢', 'T': '🐢', 'U': '🐌', 'V': '🍲', 'W': '🤨', 'X': '🥓', 'Y': '🥚', 'Z': '🥗',
    '0': '🥱', '1': '🧠', '2': '🐀', '3': '🤣', '4': '🌕', '5': '🎯', '6': '🎭', '7': '🎇', '8': '🙈', '9': '💎',
    '!': '🤲', '/': '🚸', '\\': '🥁', '?': '🌍', '@': '📧', '#': '🌈', '$': '🧙‍♂️', '%': '💯', '^': '🚣', '&' : '🎣', '*': '🦆',
    '=': '✍', '-': '🐉', '[': '🎥', ']': '🤩', '{': '📊', '}': '🕸️', '|': '🐍',
'<': '👻', '>': '💨', ';': '🤑', ':': '💦', ',': '🧡', '.': '👋', '`': '👍', '~': '💀',
    '(': '✨', ')': '🏰', '_': '⚔️', '+': '👀' 
}

# Reverse dictionary to decode the emoji message.
reverse_emoji_dict = {v: k for k, v in emoji_dict.items()}

class TranslateBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False
        self.tree = discord.app_commands.CommandTree(self)

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync()
            self.synced = True
        print(f'Logged in as {self.user}.')

client = TranslateBot()

@client.tree.command(name="encode", description="Encode a message.")
async def encode_message(interaction: discord.Interaction, message: str):
    # Add the username to the message
    message_with_username = f"**{interaction.user.name}:** \n{message}"

    encoded_base64 = base64.b64encode(message_with_username.encode()).decode()
    encoded_rot13 = codecs.encode(encoded_base64, 'rot_13')
    scrambled_message = ''.join(emoji_dict[c] for c in encoded_rot13)

    # Send an ephemeral confirmation
    await interaction.response.send_message("**Message encoded and sent!**", ephemeral=True)

    # Send the message in the channel
    await interaction.channel.send(f"**{interaction.user.name}:** \n{scrambled_message}")

@client.tree.context_menu(name="Decode")
async def decode_message(interaction: discord.Interaction, message: discord.Message):
    try:
        # Split the message content into username and encoded message
        username, encoded_message = message.content.split('\n', 1)

        # Decode the message
        decoded_data = ''.join(reverse_emoji_dict[c] for c in encoded_message)
        decoded_rot13 = codecs.decode(decoded_data, 'rot_13')
        decoded_base64 = base64.b64decode(decoded_rot13).decode('utf-8')

        # Remove the username from the decoded message
        decoded_message = decoded_base64.replace(f"{username}: \n", '')

        await interaction.response.send_message(f'{decoded_message}', ephemeral=True)
    except (KeyError, ValueError):
        await interaction.response.send_message("Can't decode this message.", ephemeral=True)

def run_discord_bot():
    try:
        with open('config.json') as f:
            data = json.load(f)
        client.run(data['discord_bot_token'])
    except Exception as e:
        logging.error(f"An error occurred while running the bot: {e}")

if __name__ == "__main__":
    run_discord_bot()
    
