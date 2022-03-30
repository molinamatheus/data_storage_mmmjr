# Data Storage
## Objetivo:
Criar uma API usando a linguagem Python, frameworks: Django e Django Rest Framework.
- A API deverá realizar a comunicação com um banco de dados SQL;
- O banco deverá ter pelo menos duas tabelas: 
         - Uma tabela chamada “Region” que conterá apenas uma coluna “name” com informação dos nomes das regiões do Brasil ( Norte, Nordeste, etc.);
         - Uma tabela chamada “Fruit” que conterá colunas “name” (o nome da fruta) e uma coluna de associação por chave estrangeira (foreign key) com a tabela “Region” associando cada fruta a uma região existente na primeira tabela.
- Para cada tabela, a API deve conter os quatro métodos GET, POST, PUT e DELETE.

## O que preciso baixar?
Django e Django-rest-framework e Postman.
Obs.: O Postman é opcional, mas eu usei ele para testar.

## O que preciso criar?
Venev.
Obs.: O Venv é opcional, mas eu usei ele para criar um ambiente virtual na minha máquina.

## Como testar a aplicação?(VÍDEO)
Para acessar o vídeo tutorial, basta seguir o link a baixo:


## Como testar a aplicação?(TEXTO)
Utilizei o Postman para isso, após ativar o ambiente virtual e rodar o server, como na imagem a baixo:

![image](https://user-images.githubusercontent.com/99224273/160835154-a5d0230c-179d-4548-9266-7abb749f60c0.png)

Seguir os seguintes passos:
### Region
#### Criar uma request POST
- Criar uma nova HTTP Request POST, clicando em "new">"HTTP Request">"POST"
![image](https://user-images.githubusercontent.com/99224273/160837850-7527d9b0-80e1-4fa3-a940-9b7f366fe002.png)
![2022-03-30 (1)](https://user-images.githubusercontent.com/99224273/160838414-91478dba-57ee-4cf1-9b16-676b36bdc831.png)
![2022-03-30 (3)](https://user-images.githubusercontent.com/99224273/160838819-4fcaa821-3974-4a9a-bb1c-4b34a36caa9a.png)

- Inserir request URL:
http://127.0.0.1:8000/regions/

- Em "Body", clicar em "raw" e digitar o script como no exemplo abaixo:
{
    "name": "Sudeste"
}
- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (4)](https://user-images.githubusercontent.com/99224273/160839437-7467195a-9bba-4229-8cad-f41987789400.png)

#### Criar uma request GET
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Inserir request URL:
http://127.0.0.1:8000/regions/

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (5)](https://user-images.githubusercontent.com/99224273/160841040-b374a8c8-a2bb-4426-9b5a-b7d23919e8de.png)

#### Criar uma request PUT
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Criar uma nova HTTP Request PUT, clicando em "GET" para abrir a lista suspensa>selecionar "PUT"
![2022-03-30 (3)](https://user-images.githubusercontent.com/99224273/160838819-4fcaa821-3974-4a9a-bb1c-4b34a36caa9a.png)

- Inserir request URL com o id da região da qual deseja EDITAR, como no exemplo a seguir:
http://127.0.0.1:8000/regions/2/

- Em "Body", clicar em "raw" e digitar o script com o nome da região que quer alterar como no exemplo abaixo:
{
    "name": "Sul"
}

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (6)](https://user-images.githubusercontent.com/99224273/160841985-8885e6a3-3b7f-41b8-bbaf-1a51d2f6bffc.png)

#### Criar uma request DELETE
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Criar uma nova HTTP Request DELETE, clicando em "GET" para abrir a lista suspensa>selecionar "DELETE"
![2022-03-30 (3)](https://user-images.githubusercontent.com/99224273/160838819-4fcaa821-3974-4a9a-bb1c-4b34a36caa9a.png)

- Inserir request URL com o id da região da qual deseja DELETAR, como no exemplo a seguir:
http://127.0.0.1:8000/regions/3/

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (7)](https://user-images.githubusercontent.com/99224273/160842335-94da0442-2cef-45b2-ba2b-acc7bb0bc276.png)

### Fruit
#### Criar uma request POST
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Criar uma nova HTTP Request POST, clicando em "GET" para abrir a lista suspensa>selecionar "POST"
![2022-03-30 (3)](https://user-images.githubusercontent.com/99224273/160838819-4fcaa821-3974-4a9a-bb1c-4b34a36caa9a.png)

- Inserir request URL:
http://127.0.0.1:8000/fruits/

- Em "Body", clicar em "raw" e digitar o script como no exemplo abaixo, vinculando a fruta a um ID de uma região ja cadastrada:
{
    "name": "Mamão",
    "region": 4
}

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (8)](https://user-images.githubusercontent.com/99224273/160843882-84b91bc5-e689-4c5f-83b9-b51da72bf55d.png)

#### Criar uma request GET
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Inserir request URL:
http://127.0.0.1:8000/fruits/

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (5)](https://user-images.githubusercontent.com/99224273/160841040-b374a8c8-a2bb-4426-9b5a-b7d23919e8de.png)

#### Criar uma request PUT
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Criar uma nova HTTP Request PUT, clicando em "GET" para abrir a lista suspensa>selecionar "PUT"
![2022-03-30 (3)](https://user-images.githubusercontent.com/99224273/160838819-4fcaa821-3974-4a9a-bb1c-4b34a36caa9a.png)

- Inserir request URL com o id da região da qual deseja EDITAR, como no exemplo a seguir:
http://127.0.0.1:8000/fruits/4/

- Em "Body", clicar em "raw" e digitar o script com o nome da fruta e a região que quer alterar como no exemplo abaixo:
{
    "name": "Melão",
    "region": 4
}

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (10)](https://user-images.githubusercontent.com/99224273/160844431-bb357a50-78d8-4582-860f-16e4d05e6298.png)

#### Criar uma request DELETE
- Clicar no "+", como indicado na imagem abaixo:
![image](https://user-images.githubusercontent.com/99224273/160840754-9bc5842a-9710-4a56-b380-eb218e090236.png)

- Criar uma nova HTTP Request DELETE, clicando em "GET" para abrir a lista suspensa>selecionar "DELETE"
![2022-03-30 (3)](https://user-images.githubusercontent.com/99224273/160838819-4fcaa821-3974-4a9a-bb1c-4b34a36caa9a.png)

- Inserir request URL com o id da região da qual deseja DELETAR, como no exemplo a seguir:
http://127.0.0.1:8000/fruits/3/

- Clicar em "Send" como na imagem a seguir:
![2022-03-30 (11)](https://user-images.githubusercontent.com/99224273/160844578-64032876-4707-4c93-a552-7499462a32c0.png)

