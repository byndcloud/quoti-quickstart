# Alterações e melhorias na autenticação de usuários

Status: Done
Type: Improvement
Assign: QUOTI

Este lançamento inclui mudanças no código relacionadas à autenticação do usuário. As mudanças se concentram em melhorias nas buscas de usuários e em obter informações sobre eles, incluindo permissões, grupos e formulários de perfil. O código também foi atualizado para lançar uma exceção personalizada **`UserNotFound`** quando um usuário não é encontrado. Além disso, o código foi otimizado para atualizar o horário de login do usuário em vez de criar um novo registro sempre que o usuário fizer login.

As seguintes funções foram atualizadas:

- **`getUser()`**: inclui a opção de pesquisar um usuário pelo e-mail e lançar uma exceção personalizada **`ResponseUnauthenticated`** quando o usuário não é encontrado.
- **`getUserFromAuthCredentials()`**: esta função não foi alterada, mas uma exceção personalizada **`UserNotFound`** agora é lançada em vez de **`ResponseNotFound`**.
- **`getSequelizeUser()`**: inclui uma exceção personalizada **`ResponseUnauthenticated`** quando o usuário não é encontrado.
- **`AuthController.getUserByToken()`**: inclui novos parâmetros de consulta que permitem obter informações adicionais sobre o usuário, como grupos e formulários de perfil. Também foi atualizado para lidar com diferentes tipos de tokens, incluindo **`Bearer`** e **`BearerStatic`**.