# =========================================
# Sistema Escolar de Notas
# =========================================

print("=" * 45)
print("        SISTEMA ESCOLAR ")
print("=" * 45)

nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

frequencia = int(input("Digite a frequência do aluno (%): "))

media = (nota1 + nota2) / 2

print("\n" +"=" * 45)

print("RELATÓRIO DO ALUNO")
print("=" * 45)

print(f"Nome do aluno: {nome}")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Média final: {media:}")
print(f"Frequência: {frequencia}%")

print("=" * 45)

if frequencia < 75:
    situacao = "REPROVADO POR FALTA"
    mensagem = "O aluno não atingiu a frequência mínima."

elif media >= 9:
    situacao = "APROVADO COM EXCELÊNCIA"
    mensagem = "Parabéns pelo excelente desempenho!"

elif media >= 7:
    situacao = "APROVADO"
    mensagem = "Aluno aprovado com sucesso."

elif media >= 5:
    situacao = "RECUPERAÇÃO"
    mensagem = "Aluno deverá realizar recuperação."

else:
    situacao = "REPROVADO POR NOTA"
    mensagem = "Aluno não atingiu a média mínima."

print(f"Situação Final: {situacao}")
print(mensagem)

print("=" * 45)

if media == 10:
    print("🏆 Nota máxima alcançada!")

elif media < 3:
    print("⚠ Desempenho muito abaixo do esperado.")

print("=" * 45)
print("Sistema finalizado com sucesso!")
print("=" * 45)