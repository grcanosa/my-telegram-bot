import emoji;
import random;
from ..handlers.phraselist import PhraseList;

NAMELIST = [
   ":bowtie:",
   ":smile:",
   ":simple_smile:",
   ":laughing:",
   ":blush:",
   ":smiley:",
   ":relaxed:",
   ":smirk:",
   ":heart_eyes:",
   ":kissing_heart:",
   ":kissing_closed_eyes:",
   ":flushed:",
   ":relieved:",
   ":satisfied:",
   ":grin:",
   ":wink:",
   ":stuck_out_tongue_winking_eye:",
   ":stuck_out_tongue_closed_eyes:",
   ":grinning:",
   ":kissing:",
   ":kissing_smiling_eyes:",
   ":stuck_out_tongue:",
   ":sleeping:",
   ":worried:",
   ":frowning:",
   ":anguished:",
   ":open_mouth:",
   ":grimacing:",
   ":confused:",
   ":hushed:",
   ":expressionless:",
   ":unamused:",
   ":sweat_smile:",
   ":sweat:",
   ":disappointed_relieved:",
   ":weary:",
   ":pensive:",
   ":disappointed:",
   ":confounded:",
   ":fearful:",
   ":cold_sweat:",
   ":persevere:",
   ":cry:",
   ":sob:",
   ":joy:",
   ":astonished:",
   ":scream:",
   ":neckbeard:",
   ":tired_face:",
   ":angry:",
   ":rage:",
   ":triumph:",
   ":sleepy:",
   ":yum:",
   ":mask:",
   ":sunglasses:",
   ":dizzy_face:",
   ":imp:",
   ":smiling_imp:",
   ":neutral_face:",
   ":no_mouth:",
   ":innocent:"
   ];

LIST = [];
for s in NAMELIST:
    LIST.append(emoji.emojize(s,use_aliases=True));

class PeopleEmoji(PhraseList):
    def __init__(self,cmd):
        self._cmd = cmd;
        self._list = LIST;
        self._type ="message";
        text = "Quieres emoji?, pues toma dos ";
        text += emoji.emojize(":coffee::coffee: \n",use_aliases=True);
        self._response = text;

    def get_max_cmd_response(self,update):
        text = self._response;
        for i in range(1,20):
            text+=self.get_random_phrase();
        return text,"message";
