# Assistente de Personal Trainer - Gerador de Treino Ideal

🏋️‍♂️ Este projeto é um desafio de Prompt Engineer, onde o objetivo é criar um assistente automatizado que ajuda a montar o treino ideal para cada combinação de fatores, como biotipo corporal, disponibilidade de tempo e tipo de exercícios preferidos. O assistente gerado será capaz de personalizar os treinos de acordo com as características e necessidades do usuário.

## 📋 Índice

- [Introdução](#-introdução)
- [Biotipos Corporais](#-biotipos-corporais)
- [Dias Disponíveis para Treino](#-dias-disponíveis-para-treino)
- [Tipos de Exercícios](#-tipos-de-exercícios)
- [Regras de Negócio](#-regras-de-negócio)
- [Material de Apoio](#-material-de-apoio)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Licença](#-licença)

## 📝 Introdução

Este projeto visa criar um assistente de personal trainer automatizado que ajuda a gerar treinos personalizados. O usuário fornecerá informações como o biotipo corporal, a quantidade de dias disponíveis para treinar na semana e o tipo de exercício preferido, e o assistente gerará um plano de treino ideal com base nessas informações.

## 💪 Biotipos Corporais

A primeira regra para personalizar o treino é determinar o biotipo corporal do usuário. Existem três biotipos principais:

| Biotipo    | Descrição                                                        |
|------------|------------------------------------------------------------------|
| Ectomorfo  | Corpo mais magro, difícil ganhar peso e massa muscular.         |
| Mesomorfo  | Corpo naturalmente musculoso, facilidade para ganhar massa.     |
| Endomorfo  | Corpo com tendência a acumular gordura, dificuldade em perder peso.|

## 📅 Dias Disponíveis para Treino

A segunda regra é determinar quantos dias por semana o usuário tem disponível para treinar. Dependendo do número de dias, o treino sugerido pode variar:

| Dias por Semana | Tipo de Treino Sugerido |
|----------------|--------------------------|
| 1 dia          | Treino Full Body         |
| 3 dias         | Treino ABC               |
| 5 dias         | Treino ABCDE             |

## 🏋️ Tipos de Exercícios

A terceira regra envolve a escolha do tipo de exercício preferido. Aqui estão algumas categorias com exemplos:

| Tipo de Treino | Descrição                                                    |
|----------------|--------------------------------------------------------------|
| Funcional       | Exercícios que melhoram a funcionalidade do corpo.         |
| Maquinário      | Exercícios feitos em máquinas, focando em isolar músculos.  |
| Peso Livre      | Exercícios com pesos livres, como halteres e barras.       |
| Cardio          | Exercícios voltados para melhorar resistência cardiovascular.|
| HIIT            | Treinos intervalados de alta intensidade.                   |

## 🛠️ Regras de Negócio

- Identifique seu biotipo corporal consultando a seção de biotipos.
- Determine quantos dias por semana você pode treinar e escolha o tipo de treino mais adequado.
- Selecione o tipo de exercício que prefere realizar e que se encaixa melhor nos seus objetivos.
- Use o assistente para gerar um plano de treino personalizado.

## 📖 Material de Apoio

Aqui estão alguns recursos adicionais que podem ser úteis para entender melhor o projeto e as práticas de prompt engineering:

- [Fundamentos de Engenharia de Prompt](#)
- [Boas Práticas de Prompt](#)

## 🎯 Como Executar o Projeto

1. **Pré-requisitos:**
   - Python 3.x instalado.

2. **Clone o repositório:**
   ```bash
   git clone <URL-do-repositório>
