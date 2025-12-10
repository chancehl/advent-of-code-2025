import re
import json

# part 0 of each line - [.##.]
type LightDiagram = list[str]

# part 1 of each line - [[3], [1,3], [2], [2,3], [0,2], [0,1]]
type ButtonWiringSchematics = list[list[int]]

# part 2 of each line - {3, 5, 4, 7}
type JoltageRequirements = list[int]

# the whole line - [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
type ElfFactoryMachineInstructions = tuple[
    LightDiagram, ButtonWiringSchematics, JoltageRequirements
]


class ElfMachineManual:
    def __init__(self, s: str) -> None:
        instructions = []

        for line in s.splitlines():
            parts = line.split(" ")

            lights = list(parts[0][1 : len(parts[0]) - 1])

            buttons = [
                [int(digit) for digit in re.findall("\\d+", button)]
                for button in parts[1 : len(parts) - 1]
            ]

            joltages = re.findall("\\d+", parts[-1].replace("}", "").replace("{", ""))

            instructions.append((lights, buttons, joltages))

        self._instructions = instructions

    def __str__(self) -> str:
        instructions = []
        for instruction in self._instructions:
            instruction_map = {
                "lights": instruction[0],
                "buttons": instruction[1],
                "joltages": instruction[2],
            }
            instructions.append(instruction_map)
        return json.dumps(instructions)

    def get_instructions(self) -> list[ElfFactoryMachineInstructions]:
        return self._instructions

    def get_instruction(self, n: int) -> ElfFactoryMachineInstructions:
        return self._instructions[n]

    def get_lights(self, n: int) -> LightDiagram:
        return self._instructions[n][0]

    def get_buttons(self, n: int) -> ButtonWiringSchematics:
        return self._instructions[n][1]

    def get_joltages(self, n: int) -> JoltageRequirements:
        return self._instructions[n][2]
