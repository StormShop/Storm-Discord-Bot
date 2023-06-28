import discord
import random
import string
from discord.ext import commands, tasks

intents = discord.Intents.default()

bot_token = 'TOKEN'
bot_prefix = '!'
bot = commands.Bot(command_prefix=bot_prefix, intents=intents)

# Set to track channels where the bot has already sent a message
posted_channels = set()

def generate_random_code(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

@bot.event
async def on_ready():
    check_channels.start()
    print("Bot is ready.")

@tasks.loop(seconds=3)
async def check_channels():
    for guild in bot.guilds:
        for category in guild.categories:
            if category.name == '⟪👑⟫ General | Основное':
                for channel in category.text_channels:
                    # If the channel starts with 'ticket-' and bot has not posted yet
                    if channel.name.startswith('ticket-') and channel.id not in posted_channels:
                        random_code = generate_random_code()

                        # Split the message into parts
                        part1 = "**⭐Покупайте Нитро способами, удобными для вас!**\nМы поддерживаем множество способов оплаты, такие как Карта, Киви, Криптовалюта, Vk pay и YooMoney.\n\n**⭐Важное примечание:** Всю комиссию вы гасите сами! Помните об этом, иначе мы не выдадим вам Нитро!\n"
                        # part2 = f"Пошаговая Интрукция:\n\n**1. Сначала нужно оплатить!**\n\nОплатите удобным для вас способом, указанным ниже. Можете использовать QR коды, если вам так удобнее! Также вам нужно будет отправить данный код: **{random_code}**, вместе с сообщением при оплате. Это необходимо, чтобы мы поняли, что оплату провели именно вы!"
                        part2 = "\n⭐Для базовой информации вам следует заклянуть в чат #📄│информация, там вы найдёте всю необходимую информацию!\n"
                        part3 = f'\n**⭐Ваш уникальный код: {random_code}** \nОтправьте его в сообщение вметсе с оплатой, чтобы мы могли удостовериться, что именно вы отправили оплату!\n'
                        part4 = "\n**⭐Способы оплаты:** [Обязательно Погасите Комиссию!]\n**Карта**: 2200 7008 2390 2746\n**Qiwi**: https://qiwi.com/n/SHOPPAYMENTS\n**VK pay**: https://vk.me/moneysend/nikitatutor\n**YooMoney**: https://yoomoney.ru/to/4100117124514335\n"
                        part5 = "\n[Оплачивайте по современному курсу рубля / доллара к нужной вам криптовалюте]\n**Bitcoin**: bc1q7p5xggs8rqc6zd3m3tnx5z4jeepqu2tn5g2s89\n**USDT (TRC20)**: TLrLCek3WqBzXY8zGAP84eTfRcfrgS5wzi\n**ETHER**: 0x4ADB5Ab8F8D13f20C31dE6b579145aa812B93fFB\n"
                        part6 = '\n**⭐После оплаты оповестите нас о том, что вы оплатили Нитро и ожидайте отправки QR кода, который вам нужно отсканировать и просто подождать 5-10 минут, чтобы получить Нитро!**'
                        # part5 = f"**\n2. Оповестите нас!**\n\nЗатем вам нужно будет написать сообщение в этот чат в формате:\n\n@Administration, Я оплатил(а) Nitro Full на месяц через Банковскую карту. Мой код: **{random_code}**\n\nЕсли же оплата проходила через криптовалюту, то укажите криптовалюту, которую вы использовали, например USDT, а затем номер кошелька, через который проходила оплата.\nПример сообщения, при оплате криптовалютой:\n\n@Administration, Я оплатил(а) Nitro Full на год через USDT, мой кошелек: <ваш номер кошелька>\n\nПримечание: Данный формат сообщения не обязательный, но если вы напишете всё так, мы быстрее обработаем вашу покупку!"
                        # part6 = "\n**3. Ожидание**\n\nНа этом этапе вам лишь необходимо подождать ответа от Администрации, обычно это занимает не более 30 минут, но может потребовать большего времени \n\n **QR код для VK pay && Bitcoin:**"

                        # Load the images
                        with open('image/qr.png', 'rb') as f:
                            file1 = discord.File(f, filename='qr.png')
                        with open('image/qr2.png', 'rb') as f2:
                            file2 = discord.File(f2, filename='qr2.png')

                        # Create the embed message
                        embed = discord.Embed(color=discord.Color.from_rgb(255, 183, 255))
                        embed.description = part1 + part2 + part3 + part4 + part5 + part6

                        # Send the roles ping
                        await channel.send("<@&1105856086948458618> <@&1105855886561390592>")

                        # Send the embed message
                        await channel.send(embed=embed)

                        # Send the images separately
                        # await channel.send(files=[file1, file2])

                        # Add the channel id to the posted_channels set
                        posted_channels.add(channel.id)


check_channels.before_loop(bot.wait_until_ready)
bot.run(bot_token)
