with open("/data/input.txt") as f:
    numeros = [int(x.strip()) for x in f]

print("Suma:", sum(numeros))
