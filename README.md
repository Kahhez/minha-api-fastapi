# Relatório e Aprendizados: Migração da API para FastAPI

Este documento detalha a jornada e os aprendizados obtidos durante a migração de uma API de Tarefas, originalmente construída com Flask, para o framework FastAPI com Pydantic.

## Saindo do Flask para o FastAPI

A migração foi a oportunidade perfeita para sentir na prática as diferenças entre os dois frameworks. Duas coisas se destacaram imediatamente:

* **A Validação de Dados com Pydantic:** Essa foi a mudança mais impactante. No Flask, a validação era um processo manual. Com FastAPI e Pydantic, definimos "Schemas" que representam nossos dados, e o framework cuida de toda a validação e conversão de tipos automaticamente. O resultado é um código muito mais limpo e seguro.

* **A Documentação Automática:** O segundo ponto foi a documentação interativa. O FastAPI gera, a partir do próprio código, uma página (`/docs`) onde é possível visualizar e testar todos os endpoints. É uma ferramenta fantástica que serve como um manual vivo do projeto.

## Como foi o processo da Migração?

O processo de reescrever a API foi metódico:

1.  **Configuração de Ambiente:** Comecei usando `venv` para criar um espaço de trabalho isolado, uma prática essencial.
2.  **Modelagem de Dados:** O primeiro passo foi desenhar os "Schemas" com Pydantic, criando modelos para a criação, atualização e visualização das tarefas.
3.  **Transcrição dos Endpoints:** Depois, reescrevi cada uma das rotas (GET, POST, PUT, DELETE), aplicando os modelos Pydantic para validar tanto os dados que chegam quanto os que saem da API.

## Acesso ao Repositório do Projeto

O código-fonte completo da nova API está disponível neste repositório do GitHub.

---
