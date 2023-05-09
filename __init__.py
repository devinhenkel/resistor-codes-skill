from mycroft import MycroftSkill, intent_file_handler


class ResistorCodes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('codes.resistor.intent')
    def handle_codes_resistor(self, message):
        color = message.data.get('color')

        self.speak_dialog('codes.resistor', data={
            'color': color
        })


def create_skill():
    return ResistorCodes()

