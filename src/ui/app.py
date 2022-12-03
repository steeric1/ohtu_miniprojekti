from PyInquirer import prompt

class CommandLineUI:
    def __init__(self, io, service):
        self._io = io
        self._service = service
        self._run = True

    def start_app(self):
        self._io.write("Tervetuloa viitekirjastoon!")
        while self._run is True:
            start_input = {
                'type': 'list',
                'name': 'start input',
                'message': 'Mitä haluat tehdä?',
                'choices': ['lisää viite','listaa viitteet','poistu']
                }
            user_input = prompt(start_input)

            if user_input['start input'] == "lisää viite":
                add_input =  {
                'type': 'list',
                'name': 'add input',
                'message': 'Minkälainen viite lisätään?',
                'choices': ['kirja','lehtiartikkeli','gradu','muu']
                }
                reference = prompt(add_input)
                self._service.add_reference(reference['add input'])

            elif user_input['start input'] == "listaa viitteet":
                referencelist = self._service.list_references()
                if referencelist:
                    for reference in referencelist:
                        self._io.write(reference)
                else:
                    self._io.write("Viitekirjasto on tyhjä.")

            elif user_input['start input'] == "poistu":
                self._run = False

            else:
                self._io.write("Virheellinen syöte.")