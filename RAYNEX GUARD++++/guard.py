import discord
import re
import asyncio

TOKEN = 'bot_token'
CHANNEL_ID = 'uyarinin_atilacagi_kanal'
INTERVAL = 7200  # İki saat (saniye cinsinden)

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

async def send_tos_message():
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNEL_ID))
    while not client.is_closed():
        await channel.send("Lütfen Discord'un Kullanım Şartlarına (TOS) uyun: https://discord.com/terms")
        await asyncio.sleep(INTERVAL)

@client.event
async def on_ready():
    print(f'online {client.user}')
    client.loop.create_task(send_tos_message())

@client.event
async def on_message(message):
    if 'CP' in message.content.upper(): # BU SATİRİ ELLEME 
        await message.channel.send(f'{message.author.mention}, CP içeren mesajlar paylaşmak yasaktır!')
        await message.delete()

    if re.search(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b', message.content): # BU SATİRİ ELLEME 
        await message.channel.send(f'{message.author.mention}, kredi kartı bilgilerini paylaşmak yasaktır!')
        await message.delete()

    if re.search(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', message.content): # BU SATİRİ ELLEME 
        await message.channel.send(f'{message.author.mention}, telefon numarası paylaşmak yasaktır!')
        await message.delete()

    if re.search(r'\b\d{1,5}\s\w.\s(\b\w*\b\s){1,2}\w*\.', message.content): # BU SATİRİ ELLEME 
        await message.channel.send(f'{message.author.mention}, adres paylaşmak yasaktır!')
        await message.delete()

client.run(TOKEN)
