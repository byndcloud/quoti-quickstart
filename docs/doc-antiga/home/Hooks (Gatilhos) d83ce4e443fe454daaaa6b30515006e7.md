# Hooks (Gatilhos)

!!! warning "Documentação descontinuada"
    Esta página faz parte de uma versão descontinuada da documentação. Está presente neste acervo e neste formato enquanto seu conteúdo não é inteiramente migrado para as demais sessões desta documentação.





# Definição

Em computação, "hooks" (também conhecidos como "ganchos" em português) são pontos de entrada ou saída de um software, onde é possível inserir ou modificar o comportamento padrão do sistema. Os hooks permitem que desenvolvedores de software possam personalizar ou estender a funcionalidade de um sistema, ou aplicativo sem a necessidade de modificar o código original.

No Quoti existe 2 tipos básicos para hooks descritos a seguir:

## 1. Hooks para tabelas ou tabelas do sistema

Para adicionar um hook para uma tabela, podemos ir na tela `/databases` e apertar no botão Webhooks da tabela desejada.

![Untitled](Hooks%20(Gatilhos)%20d83ce4e443fe454daaaa6b30515006e7/Untitled.png)

Em seguida, aperte no botão de criar um novo hook

![Untitled](Hooks%20(Gatilhos)%20d83ce4e443fe454daaaa6b30515006e7/Untitled%201.png)

Preencha o formulário abaixo escolhendo a URL na qual deseja cadastrar um hook e quando essa URL irá ser chamado (beforeCreate, beforeFind, beforeUpdate..). Caso não deseja utilizar esse webhook temporariamente, existe a opção para desativar.

![Untitled](Hooks%20(Gatilhos)%20d83ce4e443fe454daaaa6b30515006e7/Untitled%202.png)

## 2. Hooks para conectividade do usuário

1. Na tela de /hooks é possível criar qualquer tipo de hook, inclusive hooks para a conecttividade do usuário.

![Untitled](Hooks%20(Gatilhos)%20d83ce4e443fe454daaaa6b30515006e7/Untitled%203.png)

1. Caso queira adicionar um hook para a conectividade do usuário, selecione o tipo do hook igual a system

![Untitled](Hooks%20(Gatilhos)%20d83ce4e443fe454daaaa6b30515006e7/Untitled%204.png)
