# Banco de Dados para extensões

Owner: Levi Nóbrega

Por padrão o Quoti tem integração com o Firebase Firestore como banco de dados para extensões. Para utilizar o Firestore veiculado a sua instância do Quoti:

1. Crie um projeto do Firebase, se você ainda não fez isso: no [Console do Firebase](https://console.firebase.google.com/) (em inglês), clique em **Adicionar projeto** e siga as instruções na tela para criar um projeto ou adicionar serviços do Firebase a um projeto do GCP.
2. Navegue até a seção **Cloud Firestore** do [Console do Firebase](https://console.firebase.google.com/project/_/firestore). Aparecerá uma solicitação para selecionar um projeto atual do Firebase. Siga o fluxo de trabalho de criação do banco de dados.
3. Coloque como variável de ambiente a chave do seu projeto Firebase nos dockers do frontend e do backend: