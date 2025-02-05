# Ecommerce API Criada com Flask

## Descrição
A **Ecommerce API** é um sistema backend desenvolvido com **Flask** para gerenciar produtos, usuários e carrinhos de compras. Suas funcionalidades incluem **autenticação**, operações **CRUD** para produtos, manipulação de itens do carrinho, e checkout.

## Tecnologias Usadas

![Python](https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/FLASK-000000?style=for-the-badge&logo=flask&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLITE-003B57?style=for-the-badge&logo=sqlite&logoColor=white) ![Postman](https://img.shields.io/badge/POSTMAN-FF6C37?style=for-the-badge&logo=postman&logoColor=white) 

## Funcionalidades
- **Autenticação**:
  - Login de usuários.
  - Logout de usuários.
- **Produtos**:
  - Criar, listar, detalhar, atualizar e deletar produtos.
- **Carrinho de Compras**:
  - Adicionar e remover itens do carrinho.
  - Visualizar o conteúdo do carrinho.
  - Realizar "checkout", esvaziando o carrinho.
- **EndPoints Públicos e Protegidos**:
  - Autenticação para proteger ações como adicionar, deletar ou atualizar produtos e itens do carrinho.

## Estrutura do Projeto
- **app.py**: Arquivo principal que contém as rotas e a lógica.
- **requirements.txt**: Lista das dependências.
- **.gitignore**: Define os diretórios que devem ser ignorados pelo Git.

##  Endpoints

###  Autenticação:
- **POST /login**: Faz login de um usuário.
- **POST /logout**: Faz logout de um usuário autenticado.

### Produtos:
- **POST /api/products/add**: Adiciona um novo produto (protegido).
- **GET /api/products**: Lista todos os produtos.
- **GET /api/products/{id}**: Detalha um produto específico.
- **PUT /api/update/{id}**: Atualiza os dados de um produto (protegido).
- **DELETE /api/products/delete/{id}**: Remove um produto (protegido).

### Carrinho de Compras:
- **POST /api/cart/add/{id}**: Adiciona um item ao carrinho (protegido).
- **DELETE /api/cart/remove/{id}**: Remove um item do carrinho (protegido).
- **GET /api/cart**: Exibe os itens no carrinho (protegido).
- **POST /api/cart/checkout**: Realiza o checkout, esvaziando o carrinho (protegido).

## Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/DanilloSouza03/ecommerce-api.git
   cd ecommerce-api
2. Crie e ative o ambiente virtual:
   ```bash
    python -m venv venv
    venv\Scripts\activate # No Linux/Mac: source venv/bin/activate
3. Instale as dependências:
   ```bash
    pip install -r requirements.txt
4. Configure o banco de dados e crie o usuário:
   ```bash
    flask shell
    >>> db.create_all()
    >>> user = User(username="seu user", password="sua senha")
    >>> db.session.add(user)
    >>> db.session.commit()
    >>> exit()
5. Execute a aplicação:
   ```bash
    python app.py
<hr>
<p align="center">
👨‍💻 @dev.danillo
</p>