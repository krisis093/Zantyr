import re

HISTORY = ['Zantyr, co (napisał(a)?|powiedział(a)?) (?P<arg>\w+)',
           'Zantyr, pokaż historię (wiadomości)? (użytkownika|gracza) (?P<arg>\w+)']

def commandCom(client, message):
    if message.content.startswith("Zantyr, "):
        for pattern in HISTORY:
            m = re.match(pattern, message.content)
            if m:
                arg = m.group('arg')
                messages = [m.content for m in client.messages if arg in [m.author.nick, m.author.name]]
                if messages:
                    return "Proszę bardzo: {}".format("\n".join(["```{}```".format(x) for x in messages]))
                else:
                    return "Nie mogę znaleźć żadnych wiadomości użytkownika {}".format(arg)
        else:
            return 'Ty chuju!'

EXPORT = [commandCom]
