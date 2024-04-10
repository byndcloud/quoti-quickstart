# Versionamento de extensões




💡 No desenvolvimento de extensões para o Quoti é possível atribuir versões a medida que você realiza o *deploy* de uma extensão. Portanto, é possível retornar a versão de uma extensão no [ambiente de produção](Development%20&%20Production%20modes%20fa2447cbee4d454e958644a2362230a9.md), caso necessário.



## Tutoriais

- Como ver as versões de uma extensão?
    
    
    1. Acesse `https://quoti.cloud/{organização}/extension`;
    
    1. Encontre, na lista, a extensão que você deseja e clique no ícone de editar:
        
        ![Captura de Tela 2021-12-11 às 08.13.47.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.13.47.png)
        
    1. Em "Versões anteriores", você irá encontrar todas as versões de uma extensão:
        
        ![Captura de Tela 2021-12-11 às 08.16.27 (1).png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.16.27_(1).png)
        
- Como renomear uma versão?
    1. Em "Versões anteriores", clique no nome atual de uma versão que você deseja renomear:
        
        ![Captura de Tela 2021-12-11 às 08.16.27 (2).png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.16.27_(2).png)
        
    2. Digite o novo nome da versão e clique no botão `ENTER` do seu teclado:
        
        ![Captura de Tela 2021-12-11 às 08.45.40.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.45.40.png)
        
    3. A versão da sua extensão foi renomeada. Você pode fechar o popup de edição da extensão.
    
- Como aplicar em produção uma versão anterior?
    1. Em "Versões anteriores", clique no ícone da coluna "Versão utilizada" para selecionar uma versão diferente da atual:
        
        ![Captura de Tela 2021-12-11 às 08.16.27 (3).png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.16.27_(3).png)
        
    2. A versão selecionada está em produção. Você pode fechar o popup de edição da extensão.
- Como nomear o deploy de uma extensão através da [Quoti CLI](Quoti%20CLI%2012e230f5cbd6471f92e10822e4db210c.md)?
    
    Ao [desenvolver extensões](https://www.notion.so/Quoti-Extensions-d3af129ede05415fb370dee8587d758f?pvs=21) utilizando a Quoti CLI é disponibilizado o comando `qt deploy` que permite criar uma nova versão da extensão com base no código local do seu projeto e enviá-la para o [ambiente de produção](Development%20&%20Production%20modes%20fa2447cbee4d454e958644a2362230a9.md).
    
    Para atribuir um nome a nova versão que você está executando o *deploy*:
    
    1. No seu terminal, execute o comando abaixo:
        
        ```bash
        qt deploy
        ```
        
    2. O seu terminal retornará a mensagem: 
        
        ```bash
        Version Name:
        ```
        
    3. Digite o nome da sua versão no terminal e pressione a tecla `ENTER` do seu teclado.

## Troubleshooting

- Como aplicar em [ambiente de desenvolvimento](Development%20&%20Production%20modes%20fa2447cbee4d454e958644a2362230a9.md) o código de uma versão anterior?
    
    Atualmente, **não** é possível aplicar o código de uma versão anterior em seu [ambiente de desenvolvimento](Development%20&%20Production%20modes%20fa2447cbee4d454e958644a2362230a9.md).
    
    Porém, caso você queira checar o funcionamento de uma versão anterior antes de liberá-la para produção é possível realizar um *workaround*:
    
    1. Em "Versões anteriores", localize a versão que você deseja e clique no ícone de "Baixar":
        
        ![Captura de Tela 2021-12-11 às 08.16.27.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.16.27.png)
        
    2. Feche o popup de edição da extensão
        
        ![Captura de Tela 2021-12-11 às 08.19.53.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.19.53.png)
        
    3. No canto inferior direito, clique no botão para criar uma nova extensão:
        
        ![Captura de Tela 2021-12-11 às 08.21.09.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.21.09.png)
        
    4. Defina o "Título" e o "Tipo da sua extensão":
        
        
        1. A opção **Sem build** possibilita o uso de um único arquivo para carregar toda sua extensão.
        2. A opção **Com build** permite que o usuário crie sua extensão como se fosse um projeto, ou seja, sua extensão pode ter componentes em arquivos separados, dependências extras que ficam em um *package.json*, etc. Nessa opção, um *build* da extensão é feito antes de enviar o código dela para o Quoti.
        
        ![Captura de Tela 2021-12-11 às 08.24.35.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.24.35.png)
        
    5. No campo "Área de upload" arraste ou selecione o arquivo baixado no [passo 3](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3.md):
        
        ![Captura de Tela 2021-12-11 às 08.30.40.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.30.40.png)
        
    6. Clique no botão "Criar extensão"
        
        ![Captura de Tela 2021-12-11 às 08.32.53.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.32.53.png)
        
    7. Teste a versão na sua nova extensão, clicando no ícone de "Abrir":
        
        ![Captura de Tela 2021-12-11 às 08.34.42.png](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3/Captura_de_Tela_2021-12-11_as_08.34.42.png)