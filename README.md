# UF Converter

Este é um aplicativo simples em Flask que converte um código de área de telefone brasileiro para a sigla do estado correspondente. 
Ele fornece um endpoint de API RESTful que aceita um código de área de telefone como entrada e retorna a sigla do estado correspondente.

## Requisitos

Antes de executar o aplicativo, verifique se você tem os seguintes requisitos instalados:

1- Python 3.x

2- Flask

3- requests

Você pode instalar o Flask e as dependências do projeto executando o seguinte comando:
```python
pip install flask requests
```
## Executando o aplicativo

Para executar o aplicativo, siga as etapas abaixo:

1- Clone este repositório para o seu diretório local.

2- Navegue até o diretório do projeto:

```bash
cd uf-converter
```

3 - Execute o seguinte comando para iniciar o servidor Flask:

```bash
python app.py
```
4 - O servidor estará sendo executado em http://localhost:2000/.

## Uso 

Após iniciar o aplicativo, você pode fazer uma solicitação GET para o seguinte endpoint:

```
http://localhost:2000/<codigo_de_area>
```

Substitua `<codigo_de_area>` pelo código de área de telefone que você deseja converter.
O aplicativo irá retornar um JSON contendo o estado correspondente àquele código de área.

## Exemplo

Aqui está um exemplo de como fazer uma solicitação usando o cURL:

```
curl http://localhost:2000/11
```

Isso retornará o seguinte JSON:

```json
{
  "Estado": "SP"
}
```

Isso significa que o código de área "11" corresponde ao estado de São Paulo.


## Contribuição

Se você quiser contribuir para este projeto, fique à vontade para fazer um fork do repositório e enviar um pull request com suas melhorias.


## Agradecimentos

Agradecemos por usar o UF Converter! Se você tiver alguma sugestão ou encontrar algum problema, sinta-se à vontade para abrir uma issue neste repositório.



