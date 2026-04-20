## Criando o ambiente virtual

- Abra o terminal (cmd)

  ```cmd

  python -m venv venv

  ```

- Para ativar o ambiente virtual

  ```cmd

  venv\Scripts\activate

  ```

- Para desativar o ambiente virtual

  ```cmd

  deactivate

  ```

- Usando um html base usando o {% block nome %} {% endblock %} , pra torar os htmls mais padronizados

  ```html
  {% extends 'base.html' %} {% block body %}
  <div>
    <h1>Comunidade impressionadora</h1>
    <p>Teste de paragrafo</p>
  </div>
  {% endblock %}
  ```

- criar um token aleatorio com o python

  ```python
  import secrets
  secrets.token_hex(16)
  ```

- Criando um arquivo de requisitos (mostrando todas a libs utilizadas )

  ```cmd
  pip freeze > requirements.txt
  ```

- Pra instalar as bibliotecas necessarias para rodar o projeto basta todar o arquivo dentro da Venv, ele vai baixar as bibliotecas do arquivo de requirements

  ```cmd
  pip install -r requirements.txt
  ```
