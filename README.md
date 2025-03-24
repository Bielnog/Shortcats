# Shortcats - Gerenciador de Atalhos Rápidos

<img src="assets/cato.png" width="100">

## 📌 Visão Geral

**Shortcats** é um aplicativo desktop desenvolvido em Python com Tkinter, que facilita a criação, o gerenciamento e o acesso instantâneo aos seus atalhos para programas, scripts e comandos mais usados. Com um sistema de autocompletar super intuitivo, você abre seus programas favoritos sem precisar passar minutos procurando o “filho perdido”.

## ✨ Funcionalidades

- 🔍 Busca rápida com autocompletar
- ➕ Adição de novos atalhos personalizados
- 🎨 Interface dark mode elegante
- 🗃️ Armazenamento em banco de dados SQLite
- ⚡ Execução rápida de comandos

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Tkinter (Interface gráfica)
- SQLite3 (Armazenamento de dados)
- subprocess (Execução de comandos)

## 📦 Instalação

1. **Pré-requisitos**:

   - Python 3.x instalado
   - Pip (gerenciador de pacotes)

2. **Clonar o repositório**:

   ```bash
   git clone https://github.com/Bielnog/Shortcats.git
   cd Shortcats
   ```

3. **Instalar dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Executar o aplicativo**:

   ```bash
   python main.py
   ```

## 🖥️ Como Usar

1. **Abrir o Shortcats**:

   - Execute o programa (`python main.py`)
   - A janela aparecerá no centro da tela

2. **Buscar atalhos**:

   - Digite parte do nome do atalho
   - Use `Tab` para autocompletar
   - Pressione `Enter` para executar

3. **Adicionar novo atalho**:

   - Clique no botão "Adicionar Atalho"
   - Preencha o nome e o comando/caminho `(Ex: python "C:\\caminho-do-script")`
     ou simplesmente o caminho do executável `(C:\\Program Files (x86)\\Everything\\Everything.exe)`
   - Clique em "Salvar"

4. **Atalhos do teclado**:
   - `Esc`: Fechar a aplicação
   - `↓`: Navegar para a lista de sugestões
   - `Tab`: Autocompletar
   - `Enter`: Executar atalho selecionado

## 🏗️ Estrutura do Projeto

```txt
shortcats/
├── controllers/          # Lógica de controle
│   └── shortcats_controller.py
├── models/               # Modelos e acesso a dados
│   └── shortcats_model.py
├── views/                # Interface do usuário
│   └── shortcats_view.py
├── main.py               # Ponto de entrada
├── shortcuts.db          # Banco de dados (gerado automaticamente)
└── README.md             # Este arquivo
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## ✉️ Contato

Link do Projeto: [https://github.com/Bielnog/Shortcats](https://github.com/Bielnog/Shortcats)

---

### 🎨 Créditos do Ícone

O ícone utilizado neste projeto foi adaptado de:

[Black Cat Icon por Aha-Soft](https://www.iconfinder.com/icons/205616/animal_animals_avatar_black_cat_catty_danger_evil_fantasy_halloween_head_horror_kitty_lovely_monster_pet_phh_problem_pussy_scary_spooky_tomcat_icon)

Licença: Creative Commons (Attribution 3.0 Unported)
