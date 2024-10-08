# Problema da Mochila utilizando Algoritmos Genéticos
Este projeto resolve o problema da mochila (Knapsack Problem) utilizando Algoritmos Genéticos (GA). O problema consiste em selecionar um subconjunto de itens, cada um com um peso, valor e tempo de carga, de forma que o valor total seja maximizado, sem exceder a capacidade de peso da mochila ou o tempo limite de carga.

# Explicação do Algoritmo
O algoritmo é uma implementação de um Algoritmo Genético, que evolui uma população de soluções potenciais (indivíduos) ao longo de várias gerações para encontrar a melhor solução para o problema da mochila.

Definindo variaveis:
- POPULATION_SIZE: Define o número de indivíduos na população (10).
- GENOME_SIZE: Número de genes (itens) no genoma de cada indivíduo.
- GENERATIONS: Número de gerações que o algoritmo vai executar.
- MUTATION_RATE: Taxa de mutação aplicada aos indivíduos.
- KNAPSACK_CAPACITY: Capacidade máxima de peso da mochila.
- TIME_LIMIT: Limite de tempo para carregar os itens na mochila.
- item: Cada item é representado como uma tupla (peso, valor, tempo_de_carga): Exemplo: O item (2, 3, 2) tem peso 2, valor 3 e leva 2 unidades de tempo para ser carregado.

![Captura de Tela 2024-10-08 às 19 04 21](https://github.com/user-attachments/assets/8c2e7fa1-2597-43b5-a23b-fe8ecaf3f57b)

# Função de fitness:
A função fitness avalia cada indivíduo (solução) com base:

- No peso total dos itens escolhidos.
- No valor total dos itens escolhidos.
- No tempo total necessário para carregar esses itens.
- Penalizações são aplicadas se o peso exceder a capacidade da mochila ou se o tempo de carga exceder o limite de tempo.

![Captura de Tela 2024-10-08 às 19 06 20](https://github.com/user-attachments/assets/ef91dc7d-461b-489d-91b8-95f808d56dbe)

# Funcões:

- Criação de um Indivíduo: Um indivíduo é representado por um vetor binário (genoma), onde cada posição indica se o item correspondente foi selecionado (1) ou não (0).

- Criação de uma População: Função que cria a população inicial composta por POPULATION_SIZE indivíduos.

- Cruzamento (Crossover): Um ponto de corte é escolhido aleatoriamente, e o filho herda os genes dos pais até esse ponto.

- Mutação: Durante a mutação, cada gene tem uma chance de ser invertido com base na MUTATION_RATE.

- Seleção: A seleção é realizada escolhendo os indivíduos com maior aptidão para cruzamento.

![Captura de Tela 2024-10-08 às 19 07 44](https://github.com/user-attachments/assets/9ac5698a-2c85-4e7c-b488-849cf459f376)

# Evolução & Execução do Algoritmo Genético:
  - A função de evolução cria uma nova geração cruzando e mutando os pais selecionados até preencher a população novamente.
  - O algoritmo roda por GENERATIONS gerações, evoluindo a população e exibindo a melhor aptidão de cada geração.

![Captura de Tela 2024-10-08 às 19 10 58](https://github.com/user-attachments/assets/abec3812-c1dd-4d93-91e0-99a9fcf9a6c5)

# Exibição da Melhor Solução:

Ao final, a melhor solução encontrada pelo algoritmo é exibida, mostrando os itens selecionados, o peso total, o valor total e o tempo total de carga.

![Captura de Tela 2024-10-08 às 19 12 16](https://github.com/user-attachments/assets/4eb7e51f-2bc8-40ff-b321-f22626859dbe)


