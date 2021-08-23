# Python_Alchemist_Blog
 Blog focused on skills enhancement and knowledge sharing. Tech Stack's: Vue.js, Django and Django-Ninja
 
## Como executar
1. Clone o repositório.
2. Crie um virtualenv com Python 3.X.
3. Ative o virtualenv.
4. Instale as dependências.
6. Execute as migrações no banco de dados.
7. Criar um Super Usuário
8. Execute o teste.

```console
git clone https://github.com/WandersonFontes/Python_Alchemist_Blog.git
cd Python_Alchemist_Blog
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py test
```
