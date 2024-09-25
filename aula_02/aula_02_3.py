Nome = str(input("Digite o nome do Hotel: "))
Quant_Estrelas = str(input("Digite a quantidades de estrelas do Hotel: "))
Cidade = str(input("Digite o nome da cidade: "))

Largura = 20
caract_preenchimento = "*"

print(Largura,caract_preenchimento)
print(Nome.center(Largura, caract_preenchimento))
print(Quant_Estrelas.center(Largura, caract_preenchimento))
print(Cidade.center(Largura, caract_preenchimento))