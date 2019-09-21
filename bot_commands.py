# Daniel Holmes
# 2018/11/2
# bot_commands.py


from sobel_functions import sobel_from_url
from compression_functions import compression_from_url
from arguments import check_sobel_arguments, check_compression_arguments, get_sobel_arguments, get_compression_arguments
from constants import SKIP


PROCESSING_MESSAGE = "Let's paint a happy little image!"
ERROR_MESSAGE = 'Sorry there was an issue with your command'


async def sobel_command(client, message):
    """ Sobel Command """
    valid, message = check_sobel_arguments(message)

    if valid:
        await client.send_message(message.channel, PROCESSING_MESSAGE)

        url = get_sobel_arguments(message)
        image = sobel_from_url(url)
        image.save('temp.png', 'png')

        with open('temp.png', 'rb') as image:
            await client.send_message(message.channel, 'Here is your image:')
            await client.send_file(message.channel, image)

    else:
        await client.send_message(message.channel, f'{ERROR_MESSAGE}: {message}')


async def compression_command(client, message):
    """ Compression Command """
    valid, message = check_compression_arguments(message)

    if valid:
        await client.send_message(message.channel, PROCESSING_MESSAGE)

        url, n = get_compression_arguments(message)
        image = compression_from_url(url, n, SKIP)
        image.save('temp.png', 'png')

        with open('temp.png', 'rb') as image:
            await client.send_message(message.channel, f'Here is your image in {n} colours:')
            await client.send_file(message.channel, image)

    else:
        await client.send_message(message.channel, f'{ERROR_MESSAGE}: {message}')
