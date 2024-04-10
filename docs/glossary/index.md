**Organização:** Representa um tenant na estrutura multi-tentant da Plataforma Quoti. Cada organização é completamente isolada da outra. Também pode ser chamado de ambiente Quoti.  ****

**Tabelas:** São tabelas auxiliares às funcionalidades e recursos da Plataforma Quoti permitindo armazenamento, consulta e gestão de dados com muita simplicidade. Existem três tipos de tabelas:

- *Tabelas de sistema*: tabelas que a Plataforma Quoti gera automaticamente ao configurar dados adicionais de algum recurso da plataforma (perfis de usuários, tipos de produtos, tipos de grupos, etc.)
- *Quoti Databases*: tabelas criadas por usuários com permissão para criar novas tabelas em organizações do Quoti. Podem ser utilizadas para os mais diversos fins, especialmente apoiando extensões e fluxo próprios das aplicações desenvolvidas no Quoti. Ao criar uma tabela utilizando esse recurso automaticamente são gerados endpoints para consulta, atualização e criação de dados. Telas e componentes do Quoti para visualização e manipulação de dados, também, podem ser utilizados para facilitar o uso.
    - Tabelas virtuais: Modelo comum de tabela que pode ser criada utilizando esse recurso.
    - Tabelas materializadas: Versão mais recente e robusta de tabela que pode ser criada utilizando esse recurso.

**Extensão:** São interfaces (telas) complementares desenvolvidas com low-code em HTML, Vue.js e CSS. É através das extensões que é possível construir experiências visuais completamente personalizadas para os seus clientes.

**Fluxo ou Workflow:** É a forma de criar automações, rotinas e lógica de negócio dentro da plataforma Quoti. Um fluxo é sempre iniciado a partir de um evento, como: intervalo de tempo, data e hora específica, chamada de API, entre outros. A partir do seu acionamento, é possível executar atividades sequenciais e/ou paralelas como: enviar emails, consultar dados, criar documentos, preencher formulários e muito mais! [Saiba mais sobre Workflows](home/Workflow%20designer%204db62d3e43b44dda889f50c721426098.md).

**Usuário**: Para a plataforma Quoti, um *Usuário* é a representação de algo (*service-accounts*) ou alguém que realiza um acesso autenticado à plataforma (páginas públicas ou privadas).

**Permissões**: É um dos recursos nativos da plataforma e podem ser de dois tipos:

- Padrão: permissões já vem por padrão na plataforma;
- Customizadas: permissões criadas pelos usuários que possuem permissão para criar outras permissões.
    
    Na prática são palavras que podem ser atribuídas à perfis de usuários ou à grupos de usuários e são utilizadas para lógicas de validação e regras de negócio. Por exemplo, uma permissão como "product.create" permite que um usuário crie novos produtos.
    

**Aplicação:** É o conjunto de extensões, fluxos e tabelas.


**Recursos:** São o conjunto de ferramentas (interfaces e APIs) disponibilizadas pela plataforma Quoti para que você utilize ou modifique de acordo com as suas necessidades. São de 6 (seis) tipos:

- Segurança
- Serviços fundamentais (core)
- No/Low code
- Pro code
- Ferramentas de desenvolvimento
- Serviços de notificação e exibição
