#!/usr/bin/python3

import random;
from ..handlers.phraselist import PhraseList;
from .teletokens import CID;
import emoji

from telegram import Bot,Update;

LIST = [
"Me gustas por tu software no por tu hardware",
#"Agregame como Repositorio para que descargues las actualizaciones de mi paquete",
"Quisiera ser integral para ser el área bajo tu curva",
"Eres como Taringa. En tí está todo lo que un hombre puede desear",
"Quién fuera recta tangente para tocar el punto en tu parábola",
"Tú aceleras mi conexión",
"Quisiera ser mouse viejo para que me movieras la bolita",
"¿No te llamas google? - no ¿Por qué? - Porque tienes todo lo que busco",
"Me gustaría explorar tu código abierto",
"Eres como wikipedia... No importa que me mientas, yo te creo todo",
"Permiteme que te dedique la última linea de código.",
"Quien fuera programador para desarrollar un modulo en tu sistema",
"Eres como un lumos en la oscuridad, como un patronus en medio de cien dementores" ,
"Por ti respetaría los semáforos del GTA" ,
"Eres mi única y verdadera 42" ,
"Te quiero tanto que a tu Sim no le ahogo en la piscina" ,
"Eres el kernel de mi linux" ,
"Eres mi constante" ,
"Te quiero yo, y todos mis yos de todos los universos paralelos" ,
"Eres mas perfecta que Célula después de absorber a A-18" ,
"Tu has llenado toda la memoria de mi disco duro" ,
"Mi vida sin tí sería más difícil que acabar el Super Mario Bros sin saltar" ,
#"¡Hola guapa! ¿Te gusta el pimiento?" ,
#"Perdonad mi osadía, pero una princesa como vos no debería estar en un castillo... custodiada por un dragón de fuego?" ,
"Eres el trending topic de mi corazón" ,
#"¡Guapa, me das más morbo que la princesa Leia encadenada a Jabba the Hut!" ,
"Por ti me dejaria ganar a piedra, papel, tijera, lagarto, spock" ,
#"Sé que soy DC y tú eres de Marvel, pero qué rico un crossover...",
"My love for you is like dividing by zero-- it cannot be defined.",
"Is your name Wi-Fi? Because I'm feeling a connection.",
"Chemists do it on the table periodically.",
"You are the HCl to my NaOH. With our sweet love we could make an ocean together.",
"You must be the one for me, because my selectively permeable membrane let you through.",
"I'm sorry I wasn't part of your past, can I make it up by being in your future? ",
"Are you a carbon sample? Because I want to date you.",
"I'm so strongly attracted to you, scientists will have to discover a fifth fundamental force.",
"I wish I were adenine because then I could get paired with U.",
"If I had a star for every time you brightened my day, I'd have a galaxy in my hand.",
#"This must be the 8th castle because I just found my princess.",
"I'd like to calculate the slope of those curves.",
"According to the second law of thermodynamics, you're supposed to share your hotness with me. ",
"Are you a singularity? Not only are you attractive, but the closer I get to you, the faster time seems to slip by.",
"My love for you is like dividing by zero-- it cannot be defined.",
"If you were a triangle youd be acute one.",
"Are you made of beryllium, gold, and titanium? You must be because you are BeAuTi-ful.",
"Are you made of copper and tellurium? Because you're CuTe ",
"You had me at -Hello World.-",
"Are you a computer keyboard? Because you're my type.",
"You're so pretty, I wouldn't even need to use an Instagram filter if I took your photo.",
"Isn't your e-mail address beautiful@mydreams.com?",
"I'd switch to emacs for you.",
"Come to my 127.0.0.1 and I’ll give you sudo access.",
"You auto-complete me.",
"You are hotter than the bottom of my laptop.",
"Computer techs have skilled fingers if you know what I mean."
 ];

e_smilekiss = emoji.emojize(":kissing_heart:",use_aliases=True);
e_lovecat = emoji.emojize(":heart_eyes_cat::kissing_cat:",use_aliases=True);
e_heartsmile = emoji.emojize(":heart_eyes::kissing_closed_eyes::smile:",use_aliases=True);



SARALIST = [
"Te quiero mogollón, que lo sepas",
"En nada nos vemos!",
(10*e_smilekiss),
(10*e_lovecat),
"Me encanta tu risa",
"Estás más buena que el pan",
(9*e_heartsmile),
"Cuando te vea voy a .... y a ....., arufffffff"
 ]


class PiropoList(PhraseList):
    def __init__(self,cmd):
        super().__init__(cmd,LIST,"message");

    def get_max_cmd_response(self,update):
        text= update.message.from_user.first_name.split()[0];
        text +=", no seas presumid@, deja de pedir piropos";
        #return "BQADBAADKgAD15TmAAFDS0IqiyCZgwI","audio"
        #return "AwADBAADJwAD15TmAAG3Lbh5kdhR6QI","voice"
        return text,"message";


class SaraPiropoList(PhraseList):
    def __init__(self,cmd):
        super().__init__(cmd,LIST,"message");
        self._cid = CID["SARA"]

    def process(self,userR,bot,update):
        ret = False;
        if self.cmd_ok(update.message.text):
            if self._cid == update.message.chat_id:
                bot.send_message(chat_id=self._cid,text="Claro que si lovechu, a ti te mando lo que me pidas!");
                #bot.send_message(chat_id=self._cid,text=self.get_random_phrase());
                bot.send_message(chat_id=self._cid,text=random.choice(SARALIST));
            else:
                bot.send_message(chat_id=update.message.chat_id,text="Lo siento, las cosas realmente bonitas solo se las digo a una persona...");
            ret = True;
        return ret;

    def get_max_cmd_response(self,update):
        return "","";
