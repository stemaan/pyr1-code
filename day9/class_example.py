class WashingMachine:
    def __init__(self, manufacturer, model):
        self.producer = manufacturer
        self.model = model
        self.is_on = False

    def turn_on(self):
        if not self.is_on:  # 0/False -> not 0/False -> 1/True
            self.is_on = True

    def turn_off(self):
        if self.is_on:
            self.is_on = False


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
