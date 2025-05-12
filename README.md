# 🎓 Validador com Expressões Regulares (Γ, Σ, N)

Este projeto foi desenvolvido como parte da disciplina **Teoria da Computação**, do Programa de Pós-Graduação em Ciência da Computação da **Universidade Federal do Pará (UFPA)**. Seu objetivo é implementar **máscaras de validação** utilizando **expressões regulares formais**, com base nos alfabetos:

- **Γ = {A..Z}** → letras maiúsculas  
- **Σ = {a..z}** → letras minúsculas  
- **N = {0..9}** → dígitos numéricos

---

## 📌 Campos Validados

Cada campo do formulário possui uma expressão regular baseada em uma linguagem formal, como definido a seguir:

| Campo     | Expressão Regular Formal                  | Exemplo Válido         |
|-----------|--------------------------------------------|-------------------------|
| Nome      | ΓΣ⁺ ␣ ΓΣ⁺                                  | `Alan Turing`          |
| E-mail    | Σ⁺@Σ⁺(`.com.br` ∣ `.br`)                   | `a@a.br`               |
| Senha     | (Γ ∪ Σ ∪ N)^8 ∧ contém ≥1 Γ e ≥1 N         | `F123456A`             |
| CPF       | NNN.NNN.NNN-NN                             | `123.456.789-09`       |
| Telefone  | (NN) 9NNNN-NNNN ∣ (NN) 9NNNNNNNN ∣ NN 9NNNNNNNN | `(91) 99999-9999` |

---

## 🖥️ Execução

### ✅ Pré-requisitos

- Python 3.x instalado

### ▶️ Rodando

No terminal, execute:

```bash
python main.py
