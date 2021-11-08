import discord, time, datetime
from datetime import date
from discord.ext import tasks

today = date.today()
now = datetime.datetime.now()
print(today)
print(now)

today == date.fromtimestamp(time.time())

endwalker_release = date(today.year, 12, 3)
if endwalker_release < today:
  endwalker_release = endwalker_release.replace(year=today.year + 1)

time_to_release = abs(endwalker_release - today)
time_to_release.days

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@tasks.loop(hours=24)
async def daily_countdown():
  channel = client.get_channel(854100437190574081)
  await channel.send('**{} days until the release of Endwalker!**'.format(time_to_release.days))

@client.event
async def on_ready():
  daily_countdown.start()

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('&date'):
    await message.channel.send('**{} days until the release of Endwalker!**'.format(time_to_release.days))

  if message.content.startswith('&test'):
    await message.channel.send('Test completed')

client.run(BOT_TOKEN)
