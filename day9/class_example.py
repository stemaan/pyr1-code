class WashingMachineProgram:
    def __init__(self, name, temperature, speed, time_to_complete):
        self.name = name
        self.temperature = temperature
        self.spinning_speed = speed
        self.time = time_to_complete


class WashingMachine:
    def __init__(self, manufacturer, model):
        self.producer = manufacturer
        self.model = model
        self.is_on = False
        self.current_program = None
        self.current_state = None
        self.states = (
            'washing',
            'spinning',
            'pumping_out'
        )
        self.programs = (
            'daily',
            'wool',
            'silk',
            'sport'
        )

    def turn_on(self):
        if not self.is_on:  # 0/False -> not 0/False -> 1/True
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            self.is_on = False

    def enable_program(self, program_name):
        if self.is_on:
            if self.current_state is None:
                self.current_program = program_name
                # pralka rozpoczyna proces prania
                self.current_state = self.states[0]
            else:
                print('Nie mozesz zmienic programu gdy inny juz trwa!')
        else:
            print('Wlacz pralke!')

    def display_current_status(self):
        print(f'Aktualny program to: {self.current_program}, cykl: {self.current_state}')


if __name__ == '__main__':
    whirlpool_washing_machine = WashingMachine('Whirlpool', 'XXX123')
    updated_whirlpool_washing_machine = WashingMachine('Whirlpool', 'XXX124')
    beko_washing_machine = WashingMachine('Beko', '123ABC')

    whirlpool_washing_machine.turn_on()
    print(whirlpool_washing_machine.producer, whirlpool_washing_machine.model, whirlpool_washing_machine.is_on)

    print(updated_whirlpool_washing_machine.producer, updated_whirlpool_washing_machine.model,
          updated_whirlpool_washing_machine.is_on)

    beko_washing_machine.turn_on()
    print(beko_washing_machine.producer, beko_washing_machine.model, beko_washing_machine.is_on)
    beko_washing_machine.turn_on()
    print(beko_washing_machine.producer, beko_washing_machine.model, beko_washing_machine.is_on)

    updated_whirlpool_washing_machine.enable_program('daily')
    updated_whirlpool_washing_machine.turn_on()
    updated_whirlpool_washing_machine.enable_program('daily')
    updated_whirlpool_washing_machine.display_current_status()