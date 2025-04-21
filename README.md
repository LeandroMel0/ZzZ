# ZzZ - Linguagem de Programação do Universitário

A linguagem **ZzZ** foi projetada para simular a vida de um universitário, incluindo pausas aleatórias durante a execução (Dormiu). Seu código é traduzido para Python, proporcionando uma forma divertida e intuitiva de aprender conceitos de programação.

## 1. Estrutura Geral
- O código deve ser salvo com a extensão `.ZzZ`.
- Blocos são delimitados por `{ }`.
- O programa pode "dormir" aleatoriamente, imprimindo `ZzZzZzZzZzZzZzZzZzZ` e aguardando qualquer entrada para continuar.

## 1.1. Desenvolvedores
- [Leandro Melo](https://github.com/LeandroMel0)
- [Nicole Souza](https://github.com/nicolesouzab) 

## 2. Declaração de Variáveis
As variáveis começam com `#` e não possuem tipo explícito. Não podem ser inicializadas sem um valor inicial:
```ZzZ
#nota = 8
```
Equivalente em Python:
```python
nota = 8
```

## 3. Entrada e Saída
### 3.1 Exibir dados (Apresentar)
```ZzZ
Apresentar "Olá, mundo!"
```
Equivalente em Python:
```python
print("Olá, mundo!")
```

### 3.2 Entrada do usuário (Anotar)
As entradas são do tipo inteiro:
```ZzZ
Anotar em idade
```
Equivalente em Python:
```python
idade = int(input())
```

## 4. Estruturas Condicionais
### 4.1 if (TemTempo?)
```ZzZ
TemTempo? (#nota >= 7) {
    Apresentar "Passei!"
}
NaoDeu {
    Apresentar "Reprovado..."
}
```
Equivalente em Python:
```python
if nota >= 7:
    print("Passei!")
else:
    print("Reprovado...")
```

## 5. Laços de Repetição
### 5.1 Loop infinito (Estudar ... Terminei)
```ZzZ
Estudar {
    Apresentar "Estudando..."
    Terminei
}
```
Equivalente em Python:
```python
while True:
    print("Estudando...")
    break
```

## 6. Funções (Questao)
Toda função deve ter um retorno obrigatório:
```ZzZ
Questao Somar (a, b) {
    Responder a + b
}
```
Equivalente em Python:
```python
def Somar(a, b):
    return a + b
```

## 7. Pausas Aleatórias (Dormiu)
Qualquer loop, função ou estrutura condicional pode "dormir" aleatoriamente. Durante esse período, o programa imprime:
```
ZzZzZzZzZzZzZzZzZzZ
```
Para acordá-lo, basta pressionar "Enter".

---

## Exemplo Completo
```ZzZ
#nota = 8

TemTempo? (#nota >= 7) {
    Apresentar "Passei na matéria!"
}
NaoDeu {
    Apresentar "Vou ter que fazer final..."
}

Estudar {
    Apresentar "Estudando..."
    Cansei
}
```
Equivalente em Python:
```python
nota = 8

if nota >= 7:
    print("Passei na matéria!")
else:
    print("Vou ter que fazer final...")

while True:
    print("Estudando...")
    break
```

---

## Conclusão
A linguagem **ZzZ** foi projetada para ser simples e expressiva, refletindo o cotidiano de um universitário. Com pausas aleatórias e uma sintaxe intuitiva, ela é uma abordagem divertida para aprender conceitos de programação.

Contribuições são bem-vindas! Bora codar antes que o sono vença. 😴

