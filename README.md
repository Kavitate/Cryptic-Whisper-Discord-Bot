<h1 align="center">💬 🤫 Cryptic Whisper Discord Bot 🤫 💬</h1>

## About
A Discord bot that converts your chat messages into a secret language by first taking your original message and encoding it in Base64, then ROT13, and finally scrambling it with emojis.

Because the bot converts all text to emojis, it also makes the text unsearchable within Discord.

Since this repo is public, it's OBVIOUSLY a good idea to swap the emojis out with whichever ones you want to use to ensure it can't be easily decoded.

## Variables
Prior to using the bot, the following variable must be changed in the `config.json` file:
- Remove `YOUR_DISCORD_BOT_TOKEN` and replace it with your Discord bot token.

## Commands
Once the above variables have been updated, run the bot using the following commands:
- `/encode` followed by the message you want to send.

After the message has been sent or someone else has sent a message:
- Right click on the scrambled emoji message, hover over `Apps`, and select `Decode`.

## Example
First, use the `/encode` command and type the message you want to scramble.
<p align="center">
  <img src="https://i.imgur.com/c6TvzWp.png">
</p>
<br><br>

This is what the scambled message looks like.
<p align="center">
  <img src="https://i.imgur.com/Uejb29K.png">
</p>
<br><br>

To decode it, right click on the scambled message, hover over `Apps`, and select `Decode`.
<p align="center">
  <img src="https://i.imgur.com/9UqQKKk.png">
</p>
<br><br>

Now, you have a decoded message from the bot that only you can see.
<p align="center">
  <img src="https://i.imgur.com/ibRpBfN.png">
</p>

## Credits
Credit to [SkeletonMan03](https://github.com/SkeletonMan03) for the idea of thowing emojis into the mix.
