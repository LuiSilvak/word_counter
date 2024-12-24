# Importando biblioteca

from collections import Counter

def contador_de_palavras():
    print("=== Contador de Palavras ===")
    texto = input("Digite ou cole o texto para análise: ")

    # Conta palavras
    palavras = texto.split()
    numero_palavras = len(palavras)

    # Conta caracteres
    numero_caracteres = len(texto)

    # Palavras mais frequentes
    contagem = Counter(palavras)
    palavras_mais_comuns = contagem.most_common(3)

    # Exibe os resultados
    print(f"\nResultados da análise: ")
    print(f"Número total de palavras: {numero_palavras}")
    print(f"Número total de caracteres: {numero_caracteres}")
    print("\nPalavras mais frequentes: ")
    
    for palavra, frequencia in palavras_mais_comuns:
        print(f"- {palavra}: {frequencia} vez(es)")


if __name__ == "__main__":
    contador_de_palavras()