import discord
import serial
import time
import asyncio
import datetime

DISCORD_TOKEN = 'Token censoreret af sikkerhedsmæssige årsager'
TARGET_CHANNEL_ID = Også censoreret af sikkerhedsmæssige årsager
ARDUINO_PORT = '/dev/cu.usbmodem101'
BAUD_RATE = 9600
TRIGGER_CHAR = b'W'

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

timer_mode = False
interval_seconds = 0
last_trigger_time = None


def send_serial_trigger():
    ser = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)
    ser.write(TRIGGER_CHAR)
    ser.close()
    print("Water cycle triggered")


async def timer_loop():
    global last_trigger_time

    while True:
        if timer_mode and interval_seconds > 0:
            now = datetime.datetime.now()

            if last_trigger_time is None:
                last_trigger_time = now

            elapsed = (now - last_trigger_time).total_seconds()

            if elapsed >= interval_seconds:
                send_serial_trigger()
                last_trigger_time = now
                print("Interval water cycle triggered")

        await asyncio.sleep(5)


@client.event
async def on_ready():
    print(f'{client.user} has connected')
    client.loop.create_task(timer_loop())


@client.event
async def on_message(message):
    global timer_mode, interval_seconds, last_trigger_time

    if message.author == client.user:
        return

    if message.channel.id != TARGET_CHANNEL_ID:
        return

    content = message.content.lower().strip()

    if content == "w":
        send_serial_trigger()
        await message.channel.send("Water cycle started")

    elif content == "timer on":
        timer_mode = True
        last_trigger_time = None
        await message.channel.send("Interval timer enabled")

    elif content == "timer off":
        timer_mode = False
        await message.channel.send("Interval timer disabled")

    elif content.startswith("time "):
        _, days, hours, minutes = content.split()
        interval_seconds = (
            int(days) * 86400 +
            int(hours) * 3600 +
            int(minutes) * 60
        )
        last_trigger_time = None

        await message.channel.send(
            f"Interval set to {days}:{hours}:{minutes}"
        )


client.run(DISCORD_TOKEN)
