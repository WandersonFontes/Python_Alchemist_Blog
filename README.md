# :mage: Python_Alchemist_Blog 
Blog focused on skills enhancement and knowledge sharing. Tech Stack's: Vue.js, Django and Django-Ninja

[:world_map: Documentação](https://lapis-request-c58.notion.site/Python-Alquimist-4e9bb6d297c042a984dae66bbeab0f6f)

# Como executar o porjeto?

Para conseguir realizar os próximos passos primeiro clone o repositório!
```console
git clone https://github.com/WandersonFontes/Python_Alchemist_Blog.git
```
Logo em seguida iremos preparar o back e o front-end da aplicação.

:warning: Execute os comandos na ordem listada para evitar possíveis problemas. :warning:

:warning: É necessário que os comandos sejão executados em janelas separadas um terminal para Back-End outro para o Front-End. :warning:


### :man_technologist: Back-End
1. Crie um virtualenv com Python 3.X.
```console
cd Python_Alchemist_Blog\back_end\python\django-ninja
python -m venv .venv
```
2. Ative o virtualenv.
```console
source .venv/bin/activate
```
3. Instale as dependências.
```console
python -m pip install -r requirements.txt
```
4. Execute as migrações no banco de dados.
```console
python manage.py makemigrations
python manage.py migrate
```
5. Criar um Super Usuário
```console
python manage.py createsuperuser
```
6. Execute o teste.
```console
python manage.py test
```

## :man_technologist: Front-End
1. Instale as dependências do projeto.
```console
cd Python_Alchemist_Blog\front_end\vue\spa
npm install
```
2. Execute o server.
```console
npm run serve
```
