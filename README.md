# Migração (Atualização) da API de Tarefas para FastAPI

O objetivo aqui é contar um pouco sobre o processo, as ferramentas que utilizei e,
principalmente, o que aprendi ao ter feito essa troca de (Flask) para (FastAPI)

## Saindo do Flask para o FastAPI

A migração foi a oportunidade perfeita para sentir na prática as diferenças entre os
dois frameworks. Duas coisas se destacaram imediatamente:

* **A Validação de Dados com Pydantic:** Essa foi a mudança mais impactante.
No Flask, eu estava construindo a lógica de validação manualmente, verificando cada
campo do JSON. Com FastAPI e o Pydantic, essa abordagem muda completamente.
Apareceu o famoso “Schemas” que representa a estrutura dos dados, e o framework cuida
de toda a validação e conversão de tipos de forma automática. Que resultou em um código
mais limpo, seguro e declarativo

* **A Documentação Automática:** O segundo ponto, é a documentação
interativa. O FastAPI gera, a partir do próprio código, uma pagina (/docs) onde é possível
visualizar e testar todos os endpoints da API.

## Como foi o processo da Migração?

O processo de reescrever a API foi metódico. Comecei pela configuração de
ambiente, usando venv para criar um espaço de trabalho isolado, em seguida, o foco foi
traduzir a lógica:

1.  **Modelagem de Dados:** O primeiro passo foi desenhar os "Schemas" com Pydantic, criando modelos para a criação, atualização e visualização das tarefas.
2.  **Transcrição dos Endpoints:** Depois, reescrevi cada uma das rotas (GET, POST, PUT, DELETE), aplicando os modelos Pydantic para validar tanto os dados que chegam quanto os que saem da API.

## Acesso ao Repositório do Projeto

O código-fonte completo da nova API está disponível neste repositório do GitHub.

---
