# trabalho3
Trabalho 3 - SEL0456 Técnicas de Software Livre

# Automacao Residencial - Prova de Conceito

Este projeto é uma prova de conceito para uma aplicação de automação residencial que requer autenticação por senha para a execução de rotinas críticas.

## Estrutura do Projeto

- `main.py`: Script principal que interage com o usuário para verificar a senha.
- `password_util.py`: Módulo contendo funções para manipulação de senhas.
- `requirements.txt`: Lista de dependências do projeto.
- `tests/test_password_util.py`: Testes para o módulo de manipulação de senhas.
- `.github/workflows/test.yml`: Configuração do GitHub Actions para automação de testes.

## Branches

- `branch1`: Apresenta a senha ao usuário e informa se está correta.
- `branch2`: Realiza o teste de comparação internamente, sem informar ao usuário.

## Como Testar no GitHub Actions

1. Faça alterações no código.
2. Faça commit e push para o repositório.
3. Acesse a guia "Actions" no GitHub para verificar a execução automática dos testes.

## Uso

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
