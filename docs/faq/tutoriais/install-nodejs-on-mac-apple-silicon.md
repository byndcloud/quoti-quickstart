**Tutorial: Instalação do Node.js em Macs Apple Silicon**

Se você está utilizando um Mac com chip Apple Silicon e precisa instalar o Node.js para compatibilidade com aplicativos e projetos existentes, siga este tutorial para realizar a instalação de forma correta.

1. **Instale o Rosetta (caso ainda não tenha feito)**

   O Rosetta é um tradutor de binários que permite que aplicativos feitos para processadores Intel funcionem em Macs com chip Apple Silicon. Para instalá-lo, abra o Terminal e execute o seguinte comando:
   ```bash
   $ softwareupdate --install-rosetta
   ```

2. **Abra um Terminal usando Rosetta**

   É importante abrir um Terminal que execute com o Rosetta para garantir a compatibilidade durante a instalação do Node.js. Você pode fazer isso utilizando o comando `arch -x86_64` seguido do nome do shell que deseja abrir, por exemplo, o zsh:
   ```bash
   $ arch -x86_64 zsh
   ```
   Alternativamente, você pode configurar o Terminal ou iTerm para abrir automaticamente usando o Rosetta nas propriedades do aplicativo.

3. **Configure o ambiente do Node.js**

   Se você usa o gerenciador de versões Node Version Manager (nvm) e não está sendo carregado automaticamente no Terminal aberto com Rosetta, execute o seguinte comando para carregá-lo manualmente:
   ```bash
   $ source "${NVM_DIR}/nvm.sh"
   ```

4. **Instale uma versão antiga do Node.js**

   Vamos instalar a versão 12.22.1 do Node.js como exemplo. Use o nvm para fazer isso:
   ```bash
   $ nvm install v14 --shared-zlib
   ```
   O parâmetro `--shared-zlib` resolve um problema conhecido com a compilação do Node.js em sistemas Apple recentes.  


### Links Úteis
- [Como instalar **nvm**](editlink)
