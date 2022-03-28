from cardinal.decorators import command, help, regex
import random

class BaconPlugin(object):
    def __init__(self, cardinal, config):
        pass

    @regex(r'[Bb8][Aa4][Cc][Oo0][Nn](?![Bb][oO][tT])')
    @help("Talk about bacon.")
    @help("Syntax: bacon")
    def bacon(self, cardinal, user, channel, msg):
        nick = user.nick
        if "bot" not in nick: 
            cardinal.sendMsg(channel, self.get_bacon_msg(nick))

    def get_bacon_msg(self,nick):
        messages = ("⌇⌇⌇ Bacon Party ⌇⌇⌇", 
                "Welcome to the bacon party, %s!" % nick,
                "Bacon is a vegetable.",
                "You know, it's hard to beat bacon at anytime of day. — Nick Offerman",
                '''"I'm not sure how healthy bacon is in general, but I know it's incredibly delicious." — Gwyneth Paltrow''',
                '''"I unfortunately still crave chicken McNuggets and bacon, which is the meat candy of the world." — Katy Perry''',
                '''"Who cannot appreciate the smell of bacon?" — Tony Cardenas''',
                'GPL is great and all, %s, but have you tried bacon?' % nick,
                'Why did we call it Fedora Silverblue and not Fedora Bacon?',
                'mmmmmmmmmm, Bacon',
                '''"Bacon's the best. Even the frying of bacon sounds like applause." - Jim Gaffigan''',
                '''When you have bacon in your mouth, it doesn't matter who's president or anything. - Louis CK''',
                '''Bacon. Let's talk about bacon. There's no meat more glorious than bacon. - Rob Manuel''',
                'You worry too much, %s. Eat some bacon.' % nick,
                '''I'm not sure about your question, %s, but bacon is the answer.''' % nick,
                'I want someone to look at me the way I look at bacon.',
                'Roses are red.  Bacon is red.  Make some when you get out of bed.',
                'Did someone say bacon?!?'
                )
        return random.choice(messages)

    def close(self, cardinal):
        pass

entrypoint = BaconPlugin
