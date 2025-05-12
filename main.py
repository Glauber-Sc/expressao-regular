import re

# ============================
# Validações com base na Teoria da Computação:
# Γ = [A-Z]  → letras maiúsculas
# Σ = [a-z]  → letras minúsculas
# N = [0-9]  → números
# ============================

def validar_nome(nome):
    # Expressão Regular Formal: ΓΣ+ ␣ ΓΣ+
    return re.fullmatch(r'[A-Z][a-z]+ [A-Z][a-z]+', nome) is not None

def validar_email(email):
    # Expressão Regular Formal: Σ+@Σ+(.com.br | .br)
    return re.fullmatch(r'[a-z]+@[a-z]+(\.com\.br|\.br)', email) is not None

def validar_senha(senha):
    # Expressão Regular Formal: (Σ ∪ Γ ∪ N)^8 ∧ contém pelo menos 1 Γ e 1 N
    if re.fullmatch(r'[A-Za-z0-9]{8}', senha):
        return re.search(r'[A-Z]', senha) and re.search(r'[0-9]', senha)
    return False

def validar_cpf(cpf):
    # Expressão Regular Formal: NNN.NNN.NNN-NN
    return re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) is not None

def validar_telefone(telefone):
    # Expressões Regulares Formais:
    # (NN) 9NNNN-NNNN
    # (NN) 9NNNNNNNN
    # NN 9NNNNNNNN
    return re.fullmatch(r'(\(\d{2}\)\s9\d{4}-\d{4}|\(\d{2}\)\s9\d{8}|\d{2}\s9\d{8})', telefone) is not None

# ============================
# Interface interativa
# ============================

def menu():
    while True:
        print("\n=== Validador com Expressões Regulares (Γ, Σ, N) ===")
        print("1. Validar Nome")
        print("2. Validar Email")
        print("3. Validar Senha")
        print("4. Validar CPF")
        print("5. Validar Telefone")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nExpressão usada: ΓΣ+ ␣ ΓΣ+")
            valor = input("Digite o nome (ex: Alan Turing): ")
            print("✅ Válido!" if validar_nome(valor) else "❌ Inválido!")

        elif opcao == "2":
            print("\nExpressão usada: Σ+@Σ+(.com.br | .br)")
            valor = input("Digite o email (ex: a@a.br): ")
            print("✅ Válido!" if validar_email(valor) else "❌ Inválido!")

        elif opcao == "3":
            print("\nExpressão usada: (Σ ∪ Γ ∪ N)^8 com pelo menos 1 Γ e 1 N")
            valor = input("Digite a senha (8 caracteres, com 1 Γ e 1 N): ")
            print("✅ Válido!" if validar_senha(valor) else "❌ Inválido!")

        elif opcao == "4":
            print("\nExpressão usada: NNN.NNN.NNN-NN")
            valor = input("Digite o CPF (ex: 123.456.789-09): ")
            print("✅ Válido!" if validar_cpf(valor) else "❌ Inválido!")

        elif opcao == "5":
            print("\nExpressões usadas:")
            print("  (NN) 9NNNN-NNNN")
            print("  (NN) 9NNNNNNNN")
            print("  NN 9NNNNNNNN")
            valor = input("Digite o telefone: ")
            print("✅ Válido!" if validar_telefone(valor) else "❌ Inválido!")

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("❌ Opção inválida.")

# ============================
# Execução
# ============================
if __name__ == "__main__":
    menu()
