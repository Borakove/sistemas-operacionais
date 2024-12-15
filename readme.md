# Atividade de Sistemas Operacionais - Conversão de Números

## Descrição
Este projeto foi desenvolvido como parte da atividade avaliativa da disciplina de Sistemas Operacionais, ministrada pelo professor Laercio Pontin Junior (IFTO - CAMPUS COLINAS DO TOCANTINS). O programa realiza a conversão de números decimais para as bases binária, octal e hexadecimal.

## Funcionalidades
O programa implementa as seguintes conversões:
- Decimal para Binário
- Decimal para Octal
- Decimal para Hexadecimal

## Tecnologias Utilizadas
- Python 3.x
- Bibliotecas padrão do Python

## Como Executar
1. Certifique-se de ter o Python instalado em sua máquina
2. Faça o download do arquivo `conversao_numeros.py`
3. Execute o programa usando o comando:
```bash
python conversao_numeros.py
```

## Exemplo de Uso
O programa converte automaticamente os números 647, 543 e 91 para suas respectivas representações em diferentes bases numéricas.

### Exemplo de Saída:
```
Número decimal: 647
Binário: 1010000111
Octal: 1207
Hexadecimal: 287

Número decimal: 543
Binário: 1000011111
Octal: 1037
Hexadecimal: 21F

Número decimal: 91
Binário: 1011011
Octal: 133
Hexadecimal: 5B
```

## Estrutura do Código
- `convert_number()`: Função responsável pela conversão dos números
- `print_conversions()`: Função que formata e exibe os resultados
- O programa inclui verificação de resultados para garantir a precisão das conversões

## Autores
Matheus Santos Lima

## Disciplina
Sistemas Operacionais

## Professor
Laercio Pontin Junior

## Observações
- As conversões são verificadas através da reconversão para decimal
- O programa utiliza as funções built-in do Python para garantir precisão nas conversões