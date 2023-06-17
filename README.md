# UF Converter

Este é um aplicativo simples em Flask que converte um código de área de telefone brasileiro para a sigla do estado correspondente. Ele fornece um endpoint de API RESTful que aceita um código de área de telefone como entrada e retorna a sigla do estado correspondente.

## Requisitos

Antes de executar o aplicativo, verifique se você tem os seguintes requisitos instalados:

- Python 3.x
- Flask
- SQLAlchemy
- psycopg2

Você pode instalar as dependências do projeto executando o seguinte comando:

```bash
pip install flask sqlalchemy psycopg2
```

## Configurando as chaves de API

1 - Certifique-se de ter o PostgreSQL instalado e em execução.

```link
https://sbp.enterprisedb.com/getfile.jsp?fileid=1258506
```

2 - Atualize a URL de conexão do banco de dados no arquivo app.py:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seu_usuario:senha@localhost:5432/seu_banco_de_dados'
```

3 - Execute o seguinte código para criar a tabela de chaves de API:

```bash
python app.py init_db
```

4 - Em seguida, você pode adicionar suas chaves de API usando o seguinte código:

```python
api_key = "sua_chave_de_api"
hashed_key = hashlib.sha1(api_key.encode()).hexdigest()
db_conn.insert_api_keys([hashed_key])
```

## Executando o aplicativo

Para executar o aplicativo, siga as etapas abaixo:

1. Clone este repositório para o seu diretório local.

2. Navegue até o diretório do projeto:

```bash
cd uf-converter
```

3. Certifique-se de que você tenha um banco de dados PostgreSQL em execução e atualize a URL de conexão no arquivo `app.py` para corresponder às suas configurações:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://seu_usuario:senha@localhost:5432/seu_banco_de_dados'
```

4 - Execute o seguinte comando para iniciar o servidor Flask:

```bash
python app.py
```
5 - O servidor estará sendo executado em http://localhost:2000/.

## Uso 

Após iniciar o aplicativo, você pode fazer uma solicitação GET para o seguinte endpoint:

```
http://localhost:2000/<codigo_de_area>
```

Substitua `<codigo_de_area>` pelo código de área de telefone que você deseja converter.
O aplicativo irá retornar um JSON contendo o estado correspondente àquele código de área.

## Exemplo

Aqui está um exemplo de como fazer uma solicitação usando `python`:

``` python
import requests

  api_key = 'sua_chave_de_api'
  codigo_estado = '31' 

  url = f'http://localhost:2000/{codigo_estado}'
  headers = {'API-Key': api_key}

  response = requests.get(url, headers=headers)

  if response.status_code == 200:
      return response.json()
  else:
      return response.json()
```

Isso retornará o seguinte JSON:

Caso todoas as informações esteja correta:
```json
{
  "Estado": "SP"
}
```
Isso significa que o código de área "11" corresponde ao estado de São Paulo.

Caso UF não exista:

```json
{
  "error": "NENHUMA UF ENCONTRADA"
}

```

Caso a chave da API seja Incorreta: 

```json
{
  "error": "Chave de API inválida."
}

```
com código de `erro` 401

## Contribuição

Se você quiser contribuir para este projeto, fique à vontade para fazer um fork do repositório e enviar um pull request com suas melhorias.


## Agradecimentos

Agradecemos por usar o UF Converter! Se você tiver alguma sugestão ou encontrar algum problema, sinta-se à vontade para abrir uma issue neste repositório.



