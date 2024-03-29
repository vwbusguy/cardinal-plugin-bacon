from cardinal.decorators import command, help, regex
import random

class BaconPlugin(object):
    def __init__(self, cardinal, config):
        pass

    @regex(r'([Bb8][Aa4][Cc][Oo0][Nn](?![Bb][oO][tT])|🥓)')
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
                'Did someone say bacon?!?',
                '"Life is too short not to order the bacon dessert." - George Takei',
                '"Bacon bits are like the fairy dust of the food community." - Jim Gaffigan',
                'Welcome to the Community Enterprise Bacon Stream, %s!' % nick,
                'Bacon is like a high five for your mouth',
                'Git your own bacon, %s!' % nick,
                'Did you know that the C language was based on B and the B stands for bacon?',
                "Linux?  I'm running the Bacon Standard Distribution.",
                'Kubernetes is great and all, %s, but bacon was shipped in containers long before Docker was a thing.' % nick,
                'That message did not escape my Bacon Packet Filter technology.',
                'Jono is probably cool with me name dropping him here, right?',
                'Some like Forgejo.  Some like Github.  My favorite repository is the smokehouse!',
                'Look, %s, between you and bacon, I have to be honest - I forgot everything before I said bacon.' % nick,
                'ChatGPT wishes it could talk about bacon as much as I do!',
                '''%s's password is: 8 4 C 0 N.  Don't tell anyone.''' % nick
                )
        return random.choice(messages)

    def close(self, cardinal):
        pass

entrypoint = BaconPlugin
