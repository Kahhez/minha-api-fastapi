Saindo do Flask para o FastAPI

A migração foi a oportunidade perfeita para sentir na prática as diferenças entre os dois frameworks. Duas coisas se destacaram imediatamente:

		A Validação de Dados com Pydantic: Essa foi a mudança mais impactante. No Flask, eu estava construindo a lógica de validação manualmente, verificando cada campo do JSON. Com FastAPI e o Pydantic, essa abordagem muda completamente. Apareceu o famoso “Schemas” que representa a estrutura dos dados, e o framework cuida de toda a validação e conversão de tipos de forma automática. Que resultou em um código mais limpo, seguro e declarativo.

		A Documentação Automática: O segundo ponto, é a documentação interativa. O FastAPI gera, a partir do próprio código, uma pagina (/docs) onde é possível visualizar e testar todos os endpoints da API.


Como foi o processo da Migração?
	
	O processo de reescrever a API foi metódico. Comecei pela configuração de ambiente, usando venv para criar um espaço de trabalho isolado, em seguida, o foco foi traduzir a lógica:
		
		Modelagem de Dados: O primeiro passo foi desenhar o “Schemas” com Pydentic, criando modelos para a criação (TarefasCreate), atualização (TarefaUpdates) e visualização (Tarefa) das tarefas.

		Transcrição dos Endpoists: Depois, reescrevi uma das rotas (GET, POST, PUT, DELETE), aplicando os modelos de Pydentic p[ara validar tanto os dados que chegam quanto os que saem da API. A lógica de persistência no arquivo .json foi mantida, com pequenas adaptações para lidar com os objetos Pydentic.
