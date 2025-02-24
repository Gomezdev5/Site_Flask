# Site_Flask

# Amor em Pontos

Bem-vindo ao repositório do **Am@r em P@nt@s**! Este projeto é um site dedicado ao artesanato, onde você pode explorar peças únicas feitas à mão com muito amor e carinho. O site foi desenvolvido usando **Flask**, **Bootstrap** e **HTML/CSS**.

## 📸 Capturas de Tela

### Página Inicial
![Página Inicial](static/fotos/screenshot_index.png)

### Galeria
![Galeria](static/fotos/screenshot_galeria.png)

### Contato
![Contato](static/fotos/screenshot_contato.png)

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar o projeto localmente.

### Pré-requisitos

- Python 3.x instalado.
- Pip (gerenciador de pacotes do Python).

### Passos para Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/amor-em-pontos.git
   cd amor-em-pontos
Crie um ambiente virtual (opcional, mas recomendado):

bash
Copy
python -m venv .venv
Ative o ambiente virtual:

No Windows:

bash
Copy
.venv\Scripts\activate
No Linux/Mac:

bash
Copy
source .venv/bin/activate
Instale as dependências:

bash
Copy
pip install -r requirements.txt
Execute o aplicativo Flask:

bash
Copy
flask run
Acesse o site:
Abra o navegador e acesse:

Copy
http://127.0.0.1:5000/
🛠️ Estrutura do Projeto
Copy
amor-em-pontos/
│
├── app.py                  # Arquivo principal do Flask
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
│
├── templates/              # Páginas HTML
│   ├── index.html          # Página inicial
│   ├── sobre.html          # Página "Sobre"
│   ├── galeria.html        # Página "Galeria"
│   └── contato.html        # Página "Contato"
│
└── static/                 # Arquivos estáticos
    ├── css/                # Estilos CSS
    │   └── style.css
    └── fotos/              # Imagens do site
        ├── foto1.jpeg
        ├── foto2.jpeg
        └── ...
🧩 Funcionalidades
Página Inicial: Apresentação do projeto e links para outras seções.

Sobre: Informações sobre o Amor em Pontos e a história por trás do artesanato.

Galeria: Exibição de fotos dos artesanatos.

Contato: Formulário para entrar em contato.

📝 Formulário de Contato
O formulário de contato permite que os usuários enviem mensagens. No momento, as mensagens são exibidas no console do Flask. Você pode expandir essa funcionalidade para enviar emails ou salvar os dados em um banco de dados.

🤝 Como Contribuir
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Faça commit das suas alterações (git commit -m 'Adiciona nova feature').

Faça push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

🙏 Agradecimentos
Bootstrap: Para o design responsivo.

Flask: Para o backend do site.

Font Awesome: Para os ícones.

Feito com por Anderson Gomes.