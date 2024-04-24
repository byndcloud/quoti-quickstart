Instalando NVM na sua maquina.

1. **Abra o Terminal:**
   Você pode encontrar o Terminal na pasta "Utilitários" dentro da pasta "Aplicativos" ou pesquisar por "Terminal" usando o Spotlight (Command + Espaço).

2. **Instale o NVM via script de instalação:**
   Execute o seguinte comando no Terminal para baixar e executar o script de instalação do nvm diretamente do repositório GitHub:
   ```bash
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
   ```

3. **Siga as instruções:**
   O script de instalação do nvm exibirá instruções e informações durante o processo de instalação. Siga as instruções na tela para concluir a instalação do nvm.

4. **Verifique a instalação:**
   Após a instalação, feche e reabra o Terminal para garantir que as alterações tenham sido aplicadas. Em seguida, você pode verificar se o nvm foi instalado corretamente digitando:
   ```bash
   nvm -v
   ```

5. **Instale uma versão do Node.js:**
   Com o nvm instalado, você pode instalar uma versão específica do Node.js usando o comando `nvm install` seguido pela versão desejada. Por exemplo, para instalar o Node.js versão 16.14.0, você pode usar:
   ```bash
   nvm install 16.14.0
   ```

6. **Verifique a instalação do Node.js:**
   Após a instalação, verifique se o Node.js foi instalado corretamente digitando:
   ```bash
   node -v
   ```

7. **Defina uma versão padrão (opcional):**
   Se você deseja definir uma versão específica do Node.js como padrão para todas as novas sessões do Terminal, pode fazer isso com o comando `nvm alias`. Por exemplo, para definir a versão 16.14.0 como padrão, use:
   ```bash
   nvm alias default 16.14.0
   ```

Com esses passos, você terá instalado o Node Version Manager (nvm) e configurado o Node.js em seu ambiente macOS. O nvm permite alternar entre diferentes versões do Node.js conforme necessário para diferentes projetos.