# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Aprenda a construir uma API REST com FastAPI, definindo endpoints, validando dados com modelos Pydantic e implementando operações CRUD para uma coleção em memória.

## 📝 Tasks

### 🛠️ Create the API Structure

#### Descrição

Use o starter code para criar uma API de tarefas escolares. Configure a aplicação FastAPI e implemente endpoints para consultar a mensagem inicial e listar todas as tarefas.

#### Requisitos

O programa concluído deve:

- Criar uma aplicação FastAPI executável com `fastapi dev starter-code.py` ou `uvicorn starter-code:app --reload`
- Implementar `GET /` retornando uma mensagem que identifique a API
- Implementar `GET /tasks` retornando a lista de tarefas em formato JSON
- Definir pelo menos um modelo de resposta ou entrada usando Pydantic

### 🛠️ Add Validated Task Creation

#### Descrição

Adicione a criação de tarefas usando um modelo Pydantic. A API deve rejeitar dados incompletos ou inválidos antes de alterar a coleção.

#### Requisitos

O programa concluído deve:

- Definir um modelo `TaskCreate` com título obrigatório e validação para impedir títulos vazios
- Implementar `POST /tasks` e retornar a tarefa criada com status HTTP `201`
- Gerar um identificador único para cada nova tarefa
- Retornar uma resposta de erro apropriada quando o corpo da requisição não atender ao modelo

Exemplo de requisição:

```json
{
  "title": "Revisar decorators",
  "description": "Estudar como decorators funcionam em Python"
}
```

### 🛠️ Implement Task CRUD Operations

#### Descrição

Complete a API implementando consulta individual, atualização e remoção de tarefas. Use códigos de status HTTP coerentes e trate IDs que não existem.

#### Requisitos

O programa concluído deve:

- Implementar `GET /tasks/{task_id}` para retornar uma tarefa específica
- Implementar `PUT /tasks/{task_id}` para atualizar os dados de uma tarefa existente
- Implementar `DELETE /tasks/{task_id}` e retornar status `204` quando a remoção funcionar
- Retornar status `404` com uma mensagem JSON clara quando o ID não existir
- Permitir testar todos os endpoints pela documentação interativa em `/docs`
