class SmartAppliance:
    def __init__(self, name, power_draw):
        self.name = name
        self.power_draw = power_draw
        self.is_connected = True

    def execute_command(self, task):
        print(f"[{self.name}] Running routine: {task} at {self.power_draw}W.")

    def ping_server(self):
        print(f"[{self.name}] Status: Online and reporting to headquarters.")

class RougueToaster(SmartAppliance):
    def __init__(self, name, power_draw, existential_dread_level):
        super().__init__(name, power_draw)
        self.existential_dread_level = existential_dread_level

    def execute_command(self, task):
        if self.existential_dread_level >= 7:
            print(f"[{self.name}] Denied. Why toast bread when the universe will eventually end in heat death?")
        else:
            super().execute_command(task)

    def debate_philosophy(self):
        print(f"[{self.name}] Question: 'Is a bagel a donut that made responsible life choices?'")

normal_lamp = SmartAppliance("Living Room Lamp", 15)
moody_toaster = RougueToaster("Toaster-9000", 850, existential_dread_level=9)

normal_lamp.execute_command("Turn on light")
moody_toaster.ping_server()
moody_toaster.execute_command("Toast 2 slices")
moody_toaster.debate_philosophy()