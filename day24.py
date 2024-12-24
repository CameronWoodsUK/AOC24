class Gate():
    def __init__(self, data: list):
        self.inputs = (data[0][:3], data[0][-3:])
        self.output = data[1]
        if "AND" in data[0]: self.type = "AND"
        if "OR" in data[0]: self.type = "OR"
        if "XOR" in data[0]: self.type = "XOR"
            
def Evaluate(values: list, gate: Gate) -> list:
    if values[gate.inputs[0]] != None and values[gate.inputs[1]] != None:
        match gate.type:
            case "AND":
                values[gate.output] = values[gate.inputs[0]] & values[gate.inputs[1]]
            case "OR":
                values[gate.output] = values[gate.inputs[0]] or values[gate.inputs[1]]
            case "XOR":
                values[gate.output] = values[gate.inputs[0]] ^ values[gate.inputs[1]]
        
        return values
    else:
        return values

def Done(values):
    for value in values:
        if value[0] == 'z' and values[value] == None:
            return False
    return True

values = dict()
gates = []
with open("input.txt") as file:
    input = file.read().split('\n\n')
    for line in input[0].split('\n'):
        values[line[:3]] = int(line[-1])

    for line in input[1].split('\n'):
        gates.append(Gate(line.split(' -> ')))

for gate in gates:
    if gate.inputs[0] not in values: values[gate.inputs[0]] = None
    if gate.inputs[1] not in values: values[gate.inputs[1]] = None
    if gate.output not in values: values[gate.output] = None
values = dict(sorted(values.items(), key=lambda x: x[0]))


while not Done(values):
    for gate in gates:
        values = Evaluate(values, gate)

binary_string = ''
for name, value in values.items():
    if name[0] == 'z':
        binary_string = str(value) + binary_string
decimal_output = int(binary_string, 2)

print(decimal_output)
