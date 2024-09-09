# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).
km = int(input("a quantidade de km percorrido: "))
Lt = int(input("a quantidade de litros gastos: "))

consumo = float(km/Lt)
print(f"o consumo foi de {consumo}km/1")
