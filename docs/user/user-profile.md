# Criação de Perfis de Usuário no Quoti

Para começar a configurar perfis de usuário na plataforma Quoti, você precisa navegar até o endereço `orgSlug`/userprofiles, substituindo `orgSlug` pelo identificador da sua organização.

## Como Criar um Novo Perfil de Usuário

### Acesso ao Módulo de Perfis
Dirija-se à seção específica dentro do painel de controle Quoti inserindo a URL fornecida acima. Este será o seu ponto de partida para gerenciar perfis de usuário.

### Definição das Informações do Perfil

1. **Nome**: Defina um nome claro e representativo para o perfil, como 'Administrador'.

2. **Nome no Plural**: Especifique como o nome do perfil deve aparecer no plural, por exemplo, 'Administradores', para facilitar a referência a múltiplos usuários com o mesmo perfil.

3. **Slug**: Este é o apelido único para o perfil que serve como identificador no sistema, como 'admin'.

### Configurações de Acesso e Autenticação

1. **Tela Principal**: Escolha a página que os usuários deste perfil verão primeiro após o login. Selecione-a a partir de um menu dropdown, como 'Página do Item de Menu → Solicitações (Novo!)'.

2. **Método de Login**: Determine o método de login que os usuários deverão utilizar, o qual pode variar dependendo das opções do sistema.

3. **Tipo de Autenticação**: Opte pelo método padrão de autenticação, 'Padrão (Usuário e Senha)', ou por outro método disponível na lista.

4. **Força de Senha Mínima**: Escolha o nível de complexidade exigido para as senhas dos usuários, ajudando a garantir melhores práticas de segurança.

### Opções de Configuração Avançada

- **Filtragem**: Se necessário, utilize a opção 'Filtrar por grupo' para associar o perfil a grupos de usuários específicos.
- **Criação Automática de Conta**: Ative 'Habilitar auto criação de conta sem autorização prévia' caso deseje permitir que usuários se cadastrem sem necessidade de aprovação manual.
- **Integração com Webhooks**: Selecione 'Chamar Webhook para novos usuários' para integrar ações automáticas de terceiros quando um novo usuário for criado.

### Atribuição de Permissões

Configure as permissões que os usuários com esse perfil terão dentro da plataforma. Use o campo 'Permissões' para especificar estas ações.

### Dados Adicionais

Se houver necessidade de coletar informações adicionais dos usuários, utilize o botão 'Configurar dados adicionais'.

### Salvamento do Perfil

Após completar as configurações, não esqueça de salvar o novo perfil clicando em 'Salvar alterações' ou equivalente.

Siga estas etapas para garantir que cada perfil de usuário no Quoti seja configurado com as informações e permissões adequadas para suas funções dentro da organização.
