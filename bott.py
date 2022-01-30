import discord
import json
import urllib.request

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="pls waifu"))

@client.event
async def on_message(message):
    if "!waifu" == message.content:
        fh = urllib.request.urlopen("https://api.waifu.im/sfw/waifu/").read().decode()
        js = json.loads(fh)
        await message.channel.send(js["images"][0]["url"])

client.run("OTM2NDExNTY5Mjk2OTA4MzUw.YfMzOw.7DBWUQRCserE8NNSD8LZQ0L3Mv8")
