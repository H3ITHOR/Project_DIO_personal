def obter_biotipo():
    print("Escolha seu biotipo corporal:")
    print("1. Ectomorfo (Corpo mais magro, difícil ganhar peso e massa muscular)")
    print("2. Mesomorfo (Corpo naturalmente musculoso, facilidade para ganhar massa muscular e perder gordura)")
    print("3. Endomorfo (Corpo com tendência a acumular gordura, maior dificuldade em perder peso)")
    
    escolha = input("Digite o número correspondente ao seu biotipo (1/2/3): ")
    
    if escolha == '1':
        return "Ectomorfo"
    elif escolha == '2':
        return "Mesomorfo"
    elif escolha == '3':
        return "Endomorfo"
    else:
        print("Opção inválida! Tente novamente.")
        return obter_biotipo()

def obter_dias_disponiveis():
    print("Quantos dias você pode treinar por semana?")
    print("1. 1 dia")
    print("2. 3 dias")
    print("3. 5 dias")
    
    escolha = input("Digite o número correspondente (1/2/3): ")
    
    if escolha == '1':
        return 1
    elif escolha == '2':
        return 3
    elif escolha == '3':
        return 5
    else:
        print("Opção inválida! Tente novamente.")
        return obter_dias_disponiveis()

def obter_tipo_exercicio():
    print("Qual tipo de exercício você prefere?")
    print("1. Funcional")
    print("2. Maquinário")
    print("3. Peso Livre")
    print("4. Cardio")
    print("5. HIIT")
    
    escolha = input("Digite o número correspondente ao seu tipo de exercício preferido (1/2/3/4/5): ")
    
    tipos = {
        '1': "Funcional",
        '2': "Maquinário",
        '3': "Peso Livre",
        '4': "Cardio",
        '5': "HIIT"
    }
    
    return tipos.get(escolha, "Tipo de exercício não definido")

def gerar_treino(biotipo, dias_disponiveis, tipo_exercicio):
    # Definindo o plano de treino com base nos dias disponíveis
    if dias_disponiveis == 1:
        treino = "Treino Full Body"
    elif dias_disponiveis == 3:
        treino = "Treino ABC"
    elif dias_disponiveis == 5:
        treino = "Treino ABCDE"
    else:
        treino = "Plano de treino não definido"
    
    # Personalizando com base no biotipo e tipo de exercício
    plano_final = (
        f"\n--- Plano de Treino Personalizado ---\n"
        f"Biotipo: {biotipo}\n"
        f"Dias de Treino por Semana: {dias_disponiveis}\n"
        f"Tipo de Exercício Preferido: {tipo_exercicio}\n"
        f"Plano de Treino Sugerido: {treino}\n"
        f"--------------------------------------"
    )
    
    return plano_final

def main():
    print("Bem-vindo ao Assistente de Personal Trainer!\n")
    
    biotipo = obter_biotipo()
    dias_disponiveis = obter_dias_disponiveis()
    tipo_exercicio = obter_tipo_exercicio()
    
    plano_treino = gerar_treino(biotipo, dias_disponiveis, tipo_exercicio)
    
    print(plano_treino)

if __name__ == "__main__":
    main()
