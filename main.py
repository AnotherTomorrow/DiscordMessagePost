import requests

# Put in your discord tokens inside the brackets, within quotation marks, and separate with a comma.
# For example: ["lahjbfahjwebfa.awefliaweufbn", "afuweyfbuawebfawe.yailuweblriawe", etc etc]
tokens = []

# Put any amount of wallets you want within these brackets, same format as tokens.
wallets = []


def send_message(token, wallet):
    payload = {
        'content': wallet,
    }

    header = {
        'authorization': token,
    }

    # Change the discord channel you want to post to by changing the api link in the quotation marks under.
    discord_channel = "https://discord.com/api/v9/channels/9160314896683240125/messages"

    request = requests.post(discord_channel, data=payload,
                            headers=header)


for i in range(len(tokens)):
    send_message(tokens[i], wallets[i])
