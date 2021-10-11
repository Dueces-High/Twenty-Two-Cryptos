from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy import platform


if platform == "android":
    from android.permissions import request_permissions, Permission

    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])











def showpopup60():
    show = BoxLayout(orientation="vertical")
    img = Image(source="GameOver.png", size_hint=(1,.5))
    btn = Button(text="Start New Game", size_hint=(1, .2))
    lab = Label(text="Your game is over and we hope you \nenjoyed your experience learning "
                    "about \nall the shitcoins on the market. \nFor more info on "
                    "Bitcoin, visit us at\nhttp://www.fomodin.com",
                size_hint=(1, .3))
    show.add_widget(img)
    show.add_widget(lab)
    show.add_widget(btn)
    popupwindow = Popup(title="You are out of guesses", content=show, size_hint=(1, 1))
    popupwindow.open()
    btn.bind(on_press=popupwindow.dismiss)


class Menu(Screen):
    pass

class EndGame(Screen):
    pass






class Question1(Screen):
    mytext = StringProperty("Guesses Total")
    Guesseslimit = StringProperty("4")

    guess_limit = 3
    guess_count = 1

    def on_enter(self, *args):
        self.mytext = "Guesses Total"
        self.Guesseslimit = "4"

        self.guess_limit = 3
        self.guess_count = 1



    def on_button_click(self):

        self.Guesseslimit = str(self.guess_limit)
        self.guess_limit -= 1
        super(Screen, self).__init__()

        if self.guess_limit <= -1:
            print("try again")
            showpopup60()
            self.manager.current = "question1"

            self.guess_limit = 3
            self.Guesseslimit = "4"

        else:
            print("game not over")

    def Correct(self):
        print("You are right")

    def showpopup2(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "BitcoinSV.jpg",size_hint= (1, .1))
        btn = Button(text = "Close this window",size_hint= (1, .05))
        lab = Label(text = "BitcoinSV is a crypto that \nforked from Bitcoin Cash. \nIts a hated coin by many\nand often "
                           "considered a scam. \nFor more info on BitcoinSV,\nvisit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is BitcoinSV?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup1(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Bitcoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .03))
        lab = Label(text = "Bitcoin is the Gold Standard. \nIts the GodFather of Crypto.\nWith only "
                                 "22 million coins ever to \nbe in existence, you should \nget them while you can. "
                                 "\n \n \nFor more info on Bitcoin,\nvisit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Bitcoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup3(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Bitcoin_Gold.jpg",size_hint= (1, .1))
        btn = Button(text = "Close this window",size_hint= (1, .05))
        lab = Label(text = "Bitcoin Gold is a crypto that \nforked from Bitcoin. The Supply\nlimit is 21,000,000 BTG \n"
                           "For more info on Bitcoin \nGold,visit us at \nhttp://www.fomodin.com", size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is BitcoinSV?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


class Question2(Screen):
    Guesseslimit3 = NumericProperty()

    def on_enter(self, *args):
        self.screen2_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit3 = int(self.manager.ids.question1.ids.Guesseslimit2.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit3 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit3 <= 0:
            print("ry again")
            showpopup60()
            self.manager.current = "question1"

        else:
            print("game not over")


    def Correct(self):
        print("You are right")
        # self.mytext


    def showpopup4(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Ethereum.jpeg",size_hint= (1, .1))
        btn = Button(text = "Close this window",size_hint= (1, .05))
        lab = Label(text = "Ethereum is an open-source \nblockchain used for smart \ncontracts. "
                           "For more info on \nEthereum,visit us at\nhttp://www.fomodin.com", size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Ethereum?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup5(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Chainlink.png",size_hint= (1, .1))
        btn = Button(text = "Close this window",size_hint= (1, .05))
        lab = Label(text = "Chainlink is a decentralized\noracle network that provides\n"
                           "real-world data to smart \ncontracts on the blockchain. \n"
                           "For more info on \nChainlink,visit us at\nhttp://www.fomodin.com", size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Chainlink?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup6(self):
        show = BoxLayout(orientation="vertical")
        img = Image(source="LiteCoin.jpeg", size_hint=(1, .1))
        btn = Button(text="Close this window", size_hint=(1, .05))
        lab = Label(text="LiteCoin is a crypto nearly\nidentical to Bitcoin. Its\nis one of the oldest altcoins\nto date."
                             "For more info on \nLiteCoin,visit us at\nhttp://www.fomodin.com", size_hint=(1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is LiteCoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press=popupwindow.dismiss)


class Question3(Screen):
    Guesseslimit4 = NumericProperty()

    def on_enter(self, *args):
        self.screen3_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit4 = int(self.manager.ids.question2.ids.Guesseslimit3.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit4 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit4 <= 0:
            print("ryR again")
            showpopup60()

            self.manager.current = "question1"
        else:
            print("game not over")

    def showpopup8(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Digibyte.jpeg",size_hint= (1, .1))
        btn = Button(text = "Close this window",size_hint= (1, .05))
        lab = Label(text = "Digibyte is an innovative \nblockchain that can be used \nfor digital assets, "
                           "smart contracts,\ndecentralized applications and \nsecure authentication."
                           "For more\ninfo on Digibyte, visit\nus at http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Digibyte?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup9(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Monero.png",size_hint= (1, .1))
        btn = Button(text = "Close this window",size_hint= (1, .05))
        lab = Label(text = "Monero is a coin for you \nsecretive people. It is\na decentralized cryptocurrency \nthat "
                           "offers anonymity. This \ncoin has been around for a \nvery long time."
                           "For more info\non Monero, visit us at\n http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Monero?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup7(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Solana.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Solana is a blockchain platform \nspecifically designed to host \ndecentralized applications."
                           " \nSimilar to Ethereum, but with\nfaster operations and lower \ntransaction fees."
                           "Solana is a\nPoS (proof of stake) blockchain, \nmaking it more environmentally \nfriendly than"
                           "the popular PoW \n(proof of work) blockchains like \nEthereum and Bitcoin. For \nmore info on"
                           " Solana, visit us\nat http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Solana?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def Correct(self):
        print("You are right")


class Question4(Screen):
    Guesseslimit5 = NumericProperty()

    def on_enter(self, *args):
        self.screen4_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit5 = int(self.manager.ids.question3.ids.Guesseslimit4.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit5 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit5 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")

    def Correct(self):
        print("You are right")

    def showpopup10(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "PancakeSwap.png",size_hint= (1, .05))
        btn = Button(text = "Close this window",size_hint= (1, .03))
        lab = Label(text = "PancakeSwap is a decentralized \nexchange that allows you \nto trade cryptocurrencies and \n"
                           "tokens without a centralized \nintermediary, keeping custody of \nyour tokens all the while. "
                           "For \nmore info on"
                           " PancakeSwap, visit\nus at http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is PancakeSwap?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)



    def showpopup11(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "ravencoin.jpg",size_hint= (1, .05))
        btn = Button(text = "Close this window",size_hint= (1, .03))
        lab = Label(text = "Ravencoin is an open-source project\nforked from Bitcoin. Ravencoin \nis a peer-to-peer "
                           "blockchain,\nhandling the efficient creation\nand transfer of assets from one"
                           "\nparty to another.For \nmore info on"
                           "Solana, visit us\nat http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Raven Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup12(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "waves.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Waves blockchain is designed to \nenable users to create and launch \ncustom crypto tokens. "
                           "Waves \nallows for the creation and \ntrade of crypto tokens without\nthe need for extensive "
                           "smart \ncontract programming. Rather,\ntokens can be created and \nmanaged via scripts that"
                           "run in \nuser accounts on the Waves \nblockchain. For more info on\n"
                           " Waves, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Waves Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


class Question5(Screen):
    Guesseslimit6 = NumericProperty()

    def on_enter(self, *args):
        self.screen5_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit6 = int(self.manager.ids.question4.ids.Guesseslimit5.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit6 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit6 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup13(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "holo.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Holo (HOT) is an Ethereum token \nthat powers Holo, a distributed \npeer-to-peer hosting "
                           "platform \nfor Holochain apps (hApps).\n Users who host hApps on their \npersonal computers "
                           "can receive \nHOT tokens in return.. For more\n info on Holo Token, visit us at\n"
                           " http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Holo Token?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup14(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "hedera.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Hedera Hashgraph is a distributed \nledger technology that has been \ndescribed as an"
                           "alternative to \nblockchains. The hashgraph \ntechnology is currently patented,\nand the"
        "only authorized ledger \nis Hedera Hashgraph. The \nnative cryptocurrency of the \nHedera Hashgraph system "
                         "is \nHBAR. For more info on Hedera \nHashgraph, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Hedera Hashgraph Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup15(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "huobi.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Founded in China in 2013 \nHuobi Token (HT) is an exchange \nbased token and native "
                           "currency \nof the Huobi Global crypto \nexchange. Huobi is a \ncryptocurrency financial \n"
                           "services group. For more info \non Huobi Token, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Huobi Token?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question6(Screen):
    Guesseslimit7 = NumericProperty()

    def on_enter(self, *args):
        self.screen6_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit7 = int(self.manager.ids.question5.ids.Guesseslimit6.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit7 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit7 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup16(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Dragoncoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Dragon Coin is an entertainment \ncoin. The FinTech company aims \nto provide a seamless"
                           "distributed \nledger solution to the Asian \ngaming industry; providing \na more transparent,"
                           "secure \nand cost-effective way \nfor clients to move their funds.\n For more info on"
                           " Dragon \nCoin, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Dragon Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup17(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Dogecoin1.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Dogecoin is a cryptocurrency \ncreated by software engineers \nBilly Markus and Jackson "
                           "Palmer,\nwho decided to create a \npayment system as a joke, \nmaking fun of the wild\n"
                           "speculation in cryptocurrencies \nat the time. Despite its  satirical \nnature, some consider"
                           " it a \nlegitimate investment prospect.\nFor more info on"
                           " Doge Coin, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is DogeCoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup18(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Batcoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "BAT is not traded now at any \nknown exchange markets. So far, \nwe don't know how the "
                           "price \nof Batcoin has changed in \nthe past 7 days",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Batcoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question7(Screen):
    Guesseslimit8 = NumericProperty()

    def on_enter(self, *args):
        self.screen7_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit8 = int(self.manager.ids.question6.ids.Guesseslimit7.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit8 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit8 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup20(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "BitcoinAdult.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Bitcoin Adult is cryptocurrency \nfocused to become an ultimate \npayment solution in adult "
                           "\nentertainment industry. Adult \nservices have always had problems \nwith payments via "
                           "credit cards, \nbanks and PayPal payments, with \nservices being denied and accounts \nclosed. "
                           "Bitcoin Adult is here to help. \nFor more info on"
                           "Bitcoin Adult, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Bitcoin Adult?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup21(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "SexCoin.jpg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Sexcoin is Like Litecoin, \nBut Aimed at the Adult Webcam \nand Pornography Industry. "
                           "It \nis another Litecoin-like \ncryptocurrency in that it \nuses Scrypt-encryption, \npreventing "
                           "the use of Bitcoin-\nminers, called ASICs, which \npermit for extremely \nfast mining by users"
                           "with \nthe specialized hardware.\nFor more info on"
                           " Sex Coin, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is SexCoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup19(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "KimCoin.jpg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "KimCoins are assets \nrepresenting consulting hours– \none coin is one hour \nof a "
                           "workweek. \nEach week or maybe month\ncoins are released for sale and \nthereby time"
                           "gets a value based \non the competence or the \ndemand of the consulting time.\nFor more info on"
                           " Kim Coin, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Kim Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)



class Question8(Screen):
    Guesseslimit9 = NumericProperty()

    def on_enter(self, *args):
        self.screen8_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit9 = int(self.manager.ids.question7.ids.Guesseslimit8.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit9 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit9 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup22(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "potcoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "PotCoin provides blockchain \npayment technology and \necosystem solutions to \nempower "
                           "the Cannabis Industry. \nFor more info on Pot Coin, \n               visit us at"
                           "\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Pot Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup23(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "tokes.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Founded to solve the cannabis \nindustry’s banking problem via \ncryptocurrency "
                           "payments, \nthe Tokes Platform also \nbuilds blockchain based track \nand trace solutions " 
                           "for supply \nchain visibility and \nintegration to with existing \nseed to sale software."
                           "\nFor more info on Tokes Coin, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Tokes Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup24(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Hempcoin.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Launched in 2014, the \nHempCoin (THC) was built \non the source code of \nKomodo (KMD) for "
                           "the \nHemp Industry. The vision \nfor THC is to help \nfacilitate secure transactional\n "
                           "relationships between farmers, \ndistributors, and consumers\nFor more info on"
                           " Hemp Coin, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Hemp Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


class Question9(Screen):
    Guesseslimit10 = NumericProperty()

    def on_enter(self, *args):
        self.screen9_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit10 = int(self.manager.ids.question8.ids.Guesseslimit9.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit10 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit10 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup26(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Mcaffee.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "The Last Mcaffee token is a\ndeflationary DEFI token on \nthe Binance Smart Chain."
                           "\nThe Last Mcaffee is dedicated \nto his (John Mcaffee) libertarian \nprinciples and his "
                           "belief in a \ndecentralized monetary \nsystem."
                            " For more info on\nThe Last Mcaffee, visit us at\nhttp://www.fomodin.com",
                            size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is The Last Mcaffee?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup27(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "KanyeCoin.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Coinye, formerly Coinye West,\nis an abandoned scrypt-based\ncryptocurrency that "
                           "became \nembroiled in a trademark \ninfringement lawsuit for using \nthe likeness of"
                           "American \nhip hop artist Kanye West \nas its mascot, despite West \nhaving no "
                           "affiliation with \nthe project. For more info on\n"
                           "Kanye Coin, visit us at\nhttp://www.fomodin.com",
                            size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Kanye Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup25(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "PutinCoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "PutinCoin (PUT) is a \ncryptocurrency. Users are \nable to generate PUT \nthrough the "
                           "process of mining. \nPutinCoin has a current supply \nof 20,109,156,990 with \n"
                           "1,188,750,832.44736 in \ncirculation. For more info on\n"
                           "Putin Coin, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Putin Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


class Question10(Screen):
    Guesseslimit11 = NumericProperty()

    def on_enter(self, *args):
        self.screen10_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit11 = int(self.manager.ids.question9.ids.Guesseslimit10.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit11 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit11 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup28(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "eagle.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Eagle payment system, a \npayment system using \nblockchain technology supporting \nfiat "
                           "money tokens that comply \nwith the regulatory authorities \nof most jurisdictions and \n"
                           "reduce the risk of \ncryptocurrency fluctuation."
                            "\nFor more info on\n"
                           "Eagle Coin, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Eagle Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup29(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "vampireprotocol.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Vampire Protocol is described \nto be an intersection of \nthe most interesting "
                           "financial \ngames in cryptocurrency today. \nThe project claims to \nprovide farming, "
                           "staking and \nrebase events that join \ntogether to create a novel \nexperience. "
                            "For more info on\n"
                           "Vampire Protocol, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))

        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Vampire Protocol?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup30(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Batcoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "BAT is not traded now at any \nknown exchange markets. So far, \nwe don't know how the "
                           "price \nof Batcoin has changed in \nthe past 7 days",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Batcoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question11(Screen):
    Guesseslimit12 = NumericProperty()

    def on_enter(self, *args):
        self.screen11_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit12 = int(self.manager.ids.question10.ids.Guesseslimit11.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit12 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit12 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup32(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Idena.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Idena is the first Proof-of-\nPerson blockchain based \non democratic principles. Every\n "
                           "mining node is linked to a \ncryptoidentity – one \nsingle person with equal \nvoting power "
                           "and mining \nincome. Every unique human \ncan become an Idena validator \nno matter who they"
                           "are and \nwhere they live. For more \ninfo on "
                           "Idena Token, visit us \nat http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Idena?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup33(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "TabooToken.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Taboo is an adult NFT \n& Streaming media project. \nSpecializing in highly, "
                           "exclusive \ncontent. With models, who \naren’t strictly porn stars, \ntheir content "
                           "is not like \nother adult tokens. Their \nmarketplace is cutting-edge, \nwith its creation"
                           "by the \nEnjin Coin Marketplace \nDevelopers. For more info on\n"
                           "Taboo Token, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Taboo Token?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup31(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Ghost_Coin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Ghost is a proof of stake \nnetwork controlled by GHOST \ncoin holders and users. \nGhost "
                           "has no central company \nor owner, and is ran \nand maintained by the \ncommunity. "
                           "For more info on\nGhost Coin, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Ghost Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question12(Screen):
    Guesseslimit13 = NumericProperty()

    def on_enter(self, *args):
        self.screen12_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit13 = int(self.manager.ids.question11.ids.Guesseslimit12.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit13 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit13 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup34(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "kingdefi.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "KingDeFi is a DeFi project \ncombining two main areas: \nanalytics and monitoring "
                           "\nwhere they provide a \nmarket overview, liquidity \npool search engine and \nportfolio "
                           "tracking to users and \nfarming as we are a yield \noptimizer project on BSC \nand Solana."
                           " For more \ninfo on King Defi, \nvisit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is King Defi?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup35(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "MonkCoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "MONK's vision is to make \nMasternodes usable for \neveryone. MONK tries \nto help users to "
                           "\nhost and monitor their \nMasternodes without any \ntechnical knowledge."
                           " For \nmore info on Monk Coin, \nvisit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Monk Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup36(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "sherpa.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Sherpa Cash is a \ndecentralized, non-custodial \nprivacy solution built \non Avalanche."
                           " For \nmore info on Sherpa Cash, \nvisit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Sherpa Cash?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question13(Screen):
    Guesseslimit14 = NumericProperty()

    def on_enter(self, *args):
        self.screen13_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit14 = int(self.manager.ids.question12.ids.Guesseslimit13.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit14 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit14 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup37(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "insane.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "InsaneCoin (INSN) is a \ncommunity lead project \nthat is “insane about \ncrypto” "
                           "Everyone on Team \nInsane Coin is working \ntowards a shared goal of \nwanting to make "
                           "crypto \n a major part of everyday \nlife for all people on \nplanet Earth."
                           " For more \ninfo on Koji Coin, \n           visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Insane Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup38(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Koji.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Koji is the distributed, \nworldwide, decentralized\n digital token, designed to"
                           "unite \nthe earth population with \na core mission of helping \nin times of crisis and \n"
                           "donating to charitable \norganizations."
                           " For \nmore info on Koji Coin, \n           visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Koji Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup39(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "EvilCoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "The purpose of this coin \nis to embrace and inspire evil."
                           "\nFUDers and Trolls are EVIL, \nso they are welcome here."
                           "\nPumpers and Dumpers are \nEVIL, so they are welcome \nhere."
                            "Users are able to \ngenerate EVIL through \nthe process of mining. "
                           " For \nmore info on Evil Coin, \nvisit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Evil Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question14(Screen):
    Guesseslimit15 = NumericProperty()

    def on_enter(self, *args):
        self.screen14_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit15 = int(self.manager.ids.question13.ids.Guesseslimit14.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit15 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit15 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup40(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "elondoge.png",size_hint= (1, .03))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "ELONDOGE is a project that \ntakes the mission to \nprepare society for the \nMars "
                           "colony seriously. With \n$EDOGE, we can power the \nMars society with a \nuniversal basic "
                           "income thru \nthe reflectivity mechanism, \nexpanding liquidity while \nproducing endless "
                           "ELON+DOGE \nNFTs as a proof of culture.\n"
                           "For more info on Elon \nDoge, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Elon Doge Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup41(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "elongate.jpeg",size_hint= (1, .03))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "ELONGATE is a cryptocurrency \ntoken built on the Binance \nSmart Chain. "
                           "Born out of a \ntweet by Elon Musk, ELONGATE \nemploys unique tokenomics \nwith full "
                           "integration of charity. \nAs a real world use case, \nall transactions within \nthe "
                           "ecosystem are taxed \nwherein a set portion is \ndonated to charities every \nweek."
                           " For more info on Elon \nGate, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Elon Gate?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup42(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "StopElon.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Stop Elon is the world’s \nfirst protest Cryptocurrency\n"
                            "Users buy this token \nas a protest of Elon Musk \nand the manipulation\n"
                           "of the crypto currency \nmarketplace"
                           " For more \ninfo on Stop Elon, \n      visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Stop Elon?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question15(Screen):
    Guesseslimit16 = NumericProperty()

    def on_enter(self, *args):
        self.screen15_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit16 = int(self.manager.ids.question14.ids.Guesseslimit15.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit16 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit16 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup44(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "DaddyDoge.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Daddy Doge is a deflationary \ntoken that acts as a store \nof value on the binance "
                           "\nsmart chain. Each transaction \nhas a unique tax that distributes \ntokens to holders, "
                           "adds \nliquidity to the pool and \nincreases funds in the \nmarketing wallet."
                           " For more \ninfo on Daddy Doge, visit us \nat http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Daddy Doge?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup45(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "DogeCash.png",size_hint= (1, .03))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "DogeCash (DOGEC) is a \ntransparent, community-\ngoverned cryptocurrency \naimed at "
                           "preserving what \nmakes DogeCoin unique \nwhile offering an alternative \nway to get involved. "
                           "This \nis done through the \ncreation of DogeNodes, \nutilization of Proof of \nStake, and "
                           "active governance. \n For more info on Doge Cash, \n               visit us \nat http://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Doge Cash?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup43(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Dogecoin1.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Dogecoin is a cryptocurrency \ncreated by software engineers \nBilly Markus and Jackson "
                           "Palmer,\nwho decided to create a \npayment system as a joke, \nmaking fun of the wild\n"
                           "speculation in cryptocurrencies \nat the time. Despite its  satirical \nnature, some consider"
                           " it a \nlegitimate investment prospect.\nFor more info on"
                           " Doge Coin, \n               visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is DogeCoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


class Question16(Screen):
    Guesseslimit17 = NumericProperty()

    def on_enter(self, *args):
        self.screen16_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit17 = int(self.manager.ids.question15.ids.Guesseslimit16.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit17 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit17 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup46(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Hungrybear.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Hungry Bear is a \ndeflationary, fully \naudited and community-\ndriven BEP-20 token "
                           "built \non the Binance Smart Chain\n(BSC). Hungry bear's \nmission is to solve "
                           "world \nhunger as well as helping \nin the conservation of \nendangered species."
                           "For \nmore info on"
                           " Hungry Bear, \n             visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Hungry Bear?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup47(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "bearhunt.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "BHUNT is a token that aims \nto hunt all the crypto \nbears in your neighborhood\n  "
                           "and start the Bull season \nagain. Lets blow up the \nshort positions."
                           "For more \n info on Bear Hunt, \n             visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Bear Hunt?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup48(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "BEARSWAP.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Bear Swap is a decentralized \nexchange running on Binance \nSmart Chain. Simply its \nsimilar "
                           "to  Uniswap. For more \n info on Bear Hunt, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Bear Swap?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question17(Screen):
    Guesseslimit18 = NumericProperty()

    def on_enter(self, *args):
        self.screen17_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit18 = int(self.manager.ids.question16.ids.Guesseslimit17.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit18 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit18 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup49(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "akon.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Akoin helps fuel the \ndreams of entrepreneurs, \nbusiness owners, and \nsocial activists"
                           "by \nhelping them connect and \nengage across the rising \neconomies of Africa and \nbeyond; "
                           "created by visionary \nglobal artist, change-maker, \ninnovator, and humanitarian, \nAkon. "
                           "For more info \non Akon Coin, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Akoin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup50(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "GoatZuckerberg.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Goat token is a decentralized \ncommunity-driven token \nthat encourages users to \n"
                           "partake in the Meme-\ninspired ecosystem. The \nmain inspirational force for \nmememizing" 
                           "Goat Token is \nMark Zuckerberg's newly \nborn goat twins."
                           "For more \ninfo on Goat Token, visit us \nat \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Goat Zuckerberg?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)


    def showpopup51(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "brucelee.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Bruce Lee Token is a \ntoken on BSC that rewards \nyou with 1Inch tokens."
                           "By \nholding 1INCHPUNCH, you \nwill get automatic airdrops \nevery 60 minutes of "
                           "$1INCH \nstraight to your wallet! \n"
                           "For more info on Bruce Lee\nToken, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Bruce Lee Token?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question18(Screen):
    Guesseslimit19 = NumericProperty()

    def on_enter(self, *args):
        self.screen18_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit19 = int(self.manager.ids.question17.ids.Guesseslimit18.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit19 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit19 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup52(self):

        show = BoxLayout(orientation = "vertical")
        img = Image(source = "elondoge.png",size_hint= (1, .03))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "ELONDOGE is a project that \ntakes the mission to \nprepare society for the \nMars "
                           "colony seriously. With \n$EDOGE, we can power the \nMars society with a \nuniversal basic "
                           "income thru \nthe reflectivity mechanism, \nexpanding liquidity while \nproducing endless "
                           "ELON+DOGE \nNFTs as a proof of culture.\n"
                           "For more info on Elon \nDoge, visit us at\nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Elon Doge Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup53(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Minidoge.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Mini Doge is on a \nmission to help lost \nand scared animals \nfind their way to \nthe nearest "
                           "animal shelter. \nFor more info on Mini Doge \nToken, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Mini Doge?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup54(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "BabyDoge.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Baby Doge coin is a crypto \nasset created by the online \nDogecoin community. According \nto "
                           "its website, “Baby \nDoge seeks to impress his \nfather by showing his new, \nimproved "
                           "transaction speeds and \nadorableness.” For more \ninfo on Baby Doge \nToken, "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Baby Doge?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question19(Screen):
    Guesseslimit20 = NumericProperty()

    def on_enter(self, *args):
        self.screen19_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit20 = int(self.manager.ids.question18.ids.Guesseslimit19.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit20 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit20 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup55(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "MonkCoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "MONK's vision is to \nmake Masternodes usable for \neveryone. "
                           "MONK tries to \nhelp users to host and \nmonitor their Masternodes \nwithout "
                           "any technical \nknowledge. For more \ninfo on Monk Coin \nToken, "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Monk Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup56(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "MtGox.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Mt Gox is not a crypto \ncurrency. It was an \nexchange that stole \neveryone's money and is"
                           "\nreminder to everyone to \nget your crypto off \nexchanges.” For more \ninfo on Mount Gox \nToken, "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Mount Gox?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup57(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Monacoin.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "MonaCoin is an open \nsource digital currency \nand a peer-to-peer (p2p) \npayment network. "
                           "Dubbed by \nits creators as “the first \nJapanese cryptocurrency,” \nthe coin has become "
                           "somewhat \nof Japan’s national alternative \nto Bitcoin or Litecoin. \n"
                           "For more \ninfo on Mount Gox \nToken, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Mona coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question20(Screen):
    Guesseslimit21 = NumericProperty()

    def on_enter(self, *args):
        self.screen20_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit21 = int(self.manager.ids.question19.ids.Guesseslimit20.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit21 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit21 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup58(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "dogepepsi.jpg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Doge Pepsi is a project \nthat intends to merge \nthe significant "
                           "meaning \nof “Pepsi”, as a drink \nand global icon for \npeople of all ages "
                           "For more \ninfo on Doge Pepsi, "
                           "visit us \n                   at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Doge Pepsi?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup59(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "Dogeback.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Doge Back is the first \ntoken with dividend yield \npaid in Dogecoin.” \nIt’s a simple "
                           "concept \ncombining the two trending \nmechanisms : buy back \nand dividend. "
                           "For more \ninfo on Doge Back\nToken, "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Doge Back?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup65(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "BossToken.jpg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "The Boss Token is a \ncommunity driven DeFi \ncryptocurrency, with \nthe aim to become the"
                           " boss \nof Dogcoins!"
                           "For more \ninfo on Boss Token \nToken, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Boss Token", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question21(Screen):
    Guesseslimit22 = NumericProperty()

    def on_enter(self, *args):
        self.screen21_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit22 = int(self.manager.ids.question20.ids.Guesseslimit21.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit22 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit22 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup68(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "fear.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Fear is a blockchain \nbased horror games project \nfounded by the creators \nof the "
                           "famous Whack \nIt series of bloody point \nand click casual idle games.\n"
                           "Fear develop horror\n based blockchain NFT \ngames targeting "
                           "teenagers and \nyoung adults. For more \ninfo on Fear , "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Fear?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup67(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "osmosis.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Osmosis is a decentralized \npeer-to-peer blockchain \nthat people can use \nto create"
                           " liquidity \nand trade IBC enabled \ntokens. The Osmosis \nblockchain is made up \nof free, "
                           "public, and open-\nsource software.For more \ninfo on Osmosis \nToken, "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Osmosis?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup66(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "piratecoin.png",size_hint= (1, .03))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "PirateCoin aims to \nproduce a game integrating \nNFT by finding Treasure \nand earning "
                           "PirateCoin. \nEach character within the \ngame is Unique and can \nbe sold on the PirateCoin\n "
                           "NFT. The character will \nearn and get experience \nthe more time spent in \nthe game. "
                           "For more \ninfo on Pirate Coin Token \nToken, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Pirate Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class Question22(Screen):
    Guesseslimit23 = NumericProperty()

    def on_enter(self, *args):
        self.screen22_output.text = self.manager.ids.question1.ids.screen1_output.text
        self.Guesseslimit23 = int(self.manager.ids.question21.ids.Guesseslimit22.text)

    def on_button_click(self):
        print("try again")
        self.Guesseslimit23 -= 1
        super(Screen, self).__init__()
        if self.Guesseslimit23 <= 0:
            print("ryR again")
            showpopup60()
            self.manager.current = "question1"
        else:
            print("game not over")


    def Correct(self):
        print("You are right")

    def showpopup69(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "aquafi.png",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "$AQUA is the native token \nfor the AquaFi protocol — \na universal liquidity mining "
                           "\nprotocol that allows anyone \nto earn a premium on their \nLP fees from DEXs like \nUniswap "
                           "and Suishiswap For \nmore info on AquaFi , "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is AquaFi?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup70(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "dirtyfinance.jpeg",size_hint= (1, .04))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "DIRTY Finance is an NFT \nproject. It focuses on \ndropping NFTs in the \nHentai Genre. "
                           "Staking of \nDIRTY LP Tokens allows \nto earn exclusive NFT's \nfrom the DIRTY Finance's "
                           "\nNFT Marketplace..For more \ninfo on Dirty Finance \nToken, "
                           "visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Dirty Finance?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

    def showpopup71(self):
        show = BoxLayout(orientation = "vertical")
        img = Image(source = "ultraclearcoin.png",size_hint= (1, .03))
        btn = Button(text = "Close this window",size_hint= (1, .02))
        lab = Label(text = "Ultra Clear (UCR) is a coin \nwhich will make the saving \nof carbon lucrative for \n"
                           "individuals and businesses. \nIt is supposed to compensate \nor even turn around the\n"
                           "competitive disadvantage of \nenvironmentally friendly actions \nby means of market \n"
                           "economy rules, including \ncarbon trading."
                           "For more \ninfo on Ultra Clear Coin \nToken, visit us at \nhttp://www.fomodin.com",
                    size_hint= (1, .1))
        show.add_widget(img)
        show.add_widget(lab)
        show.add_widget(btn)
        popupwindow = Popup(title="WRONG: What is Ultra Clear Coin?", content=show, size_hint=(.75, .75))
        popupwindow.open()
        btn.bind(on_press = popupwindow.dismiss)

class WindowManager(ScreenManager):
    pass

Crypto911App = Builder.load_file("Crypto911App.kv")

class Crypto911(App):
    def build(self):
        self.icon = "FomodinLogo.png"
        return WindowManager()





if __name__ == "__main__":
    Crypto911().run()