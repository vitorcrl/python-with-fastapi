
# FastAPI CRUD Example

Este projeto é um exemplo básico de um CRUD (Create, Read, Update, Delete) utilizando FastAPI, SQLAlchemy, e SQLite. O código fornece endpoints para gerenciar "items" com operações de criação, leitura, atualização e exclusão.

## Configuração do Ambiente

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Crie e ative um ambiente virtual**:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate
    ```

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Estrutura do Projeto

- `main.py`: Ponto de entrada da aplicação.
- `app/routers/items.py`: Contém os endpoints CRUD.
- `app/crud.py`: Contém as funções que interagem com o banco de dados.
- `app/models.py`: Define os modelos do banco de dados.
- `app/schemas.py`: Define os esquemas Pydantic usados para validação e serialização.
- `app/database.py`: Configuração da conexão com o banco de dados.

## Executando a Aplicação

Para rodar a aplicação, utilize o comando:

```bash
poetry run uvicorn main:app --reload
```

Isso iniciará o servidor em modo de recarga automática em `http://127.0.0.1:8000`.

## Endpoints Disponíveis

- `POST /items/`: Cria um novo item.
- `GET /items/`: Retorna uma lista de itens.
- `GET /items/{item_id}`: Retorna um item específico pelo ID.
- `PUT /items/{item_id}`: Atualiza um item existente pelo ID.
- `DELETE /items/{item_id}`: Exclui um item pelo ID.

## Testando os Endpoints

Você pode testar os endpoints utilizando ferramentas como `curl`, `Postman` ou acessando a documentação interativa em `http://127.0.0.1:8000/docs`.

### Exemplo de Criação de um Item

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Item1",
  "description": "A sample item",
  "price": 10.5,
  "tax": 1.5
}'
```
### Gerenciando Migrações com Alembic
1. Criando uma Nova Migração
Após alterar os modelos em app/models.py, você precisa criar uma nova migração para refletir essas mudanças no banco de dados.

No diretório raiz do projeto, execute:

```bash
alembic revision --autogenerate -m "Descrição da migração"
```
Isso gerará um novo arquivo de migração no diretório alembic/versions/.
2. Aplicando Migrações
Para aplicar as migrações ao banco de dados, execute:

```bash
alembic upgrade head
```
Este comando aplicará todas as migrações pendentes e atualizará o esquema do banco de dados.

3. Revertendo Migrações
Se precisar reverter uma migração, você pode usar:

```bash
alembic downgrade -1
```
Isso reverterá a última migração aplicada. Você pode especificar um número de revisão específico ou usar base para voltar ao estado inicial.
### Exemplo de Leitura de Todos os Itens

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json'
```

## Dependências

As principais dependências do projeto são:

- `fastapi`
- `uvicorn`
- `sqlalchemy`
- `pydantic`

## Considerações Finais

Este é um exemplo básico para fins de aprendizado. Para ambientes de produção, considere configurar um banco de dados mais robusto e medidas adicionais de segurança.
