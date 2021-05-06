from conta_corrente import ContaCorrente

conta_gui = ContaCorrente(15)
print(conta_gui)
conta_gui.deposita(500)
print(conta_gui)

conta_dani = ContaCorrente(47685)
print(conta_dani)
conta_dani.deposita(100)
print(conta_dani)

contas = [conta_gui, conta_dani]
print("Contas -------")
for conta in contas:
    print(conta)