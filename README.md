# StudyPlan

Projeto da disciplina de Programação e IHC — CESMAC.

O StudyPlan é um site open source para alunos se organizarem. O aluno cadastra as
matérias, registra cada sessão de estudo (tempo, exercícios feitos e acertos) e vê o
que precisa revisar antes das provas.

## Tecnologias

- Python + Flask (templates com Jinja)
- HTML5 semântico
- Bootstrap 5 e Bootstrap Icons (pelo CDN)
- CSS próprio em `static/css/style.css`

## Como rodar (Windows)

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
flask --app main run --debug
```

Depois abra http://127.0.0.1:5000 no navegador.

## Páginas

| Página | Endereço |
|---|---|
| Início | `/` |
| Sobre | `/sobre` |
| Entrar | `/entrar` |
| Criar conta | `/cadastro` |
| Painel | `/painel` |
| Minhas matérias | `/materias` |
| Detalhe da matéria | `/materia/1` (1 a 5) |
| Registrar estudo | `/registrar` |

Nesta versão os dados ficam numa lista no `main.py` e os formulários ainda não salvam
nada. Banco de dados e login de verdade entram nas próximas etapas da disciplina.

## Estrutura

```
main.py                  dados (listas) e rotas do site
templates/base.html      estrutura comum a todas as páginas
templates/_partials/     menu (navbar), rodapé (footer) e selo de situação
templates/home.html      página inicial
templates/about.html     página Sobre
templates/entrar.html    formulário de entrada (e-mail e senha)
templates/cadastro.html  formulário de criação de conta
templates/painel.html    resumo dos estudos e o que revisar
templates/materias.html  tabela com as matérias e o aproveitamento
templates/materia.html   detalhe da matéria com o histórico de estudos
templates/registrar.html formulário para registrar um estudo
static/css/style.css     cores e estilos próprios
static/js/script.js      aviso "carregando" do formulário Registrar estudo
static/img/logo.svg      logo do StudyPlan
```

## Licença

Código aberto sob a licença MIT (veja o arquivo `LICENSE`).
