<!-- ## Glossário da Plataforma Quoti -->

Este glossário contém termos e conceitos chave usados na Plataforma Quoti, proporcionando uma visão clara sobre sua arquitetura e funcionalidades.

### Organização
Representa um `tenant` na estrutura multi-tenant da Plataforma Quoti. Cada organização, ou ambiente Quoti, é completamente isolada das demais, assegurando privacidade e segurança dos dados.

### Tabelas
Tabelas são estruturas essenciais para o armazenamento, consulta e gestão de dados dentro do Quoti, classificadas em três tipos:

- **Tabelas de Sistema:** Criadas automaticamente pela plataforma para suportar configurações e recursos adicionais (como perfis de usuários e tipos de produtos).
- **Quoti Databases:** Tabelas definidas por usuários autorizados, apoiando extensões e processos de negócio customizados. A criação de uma tabela gera automaticamente endpoints de API e permite o uso de interfaces do Quoti para manipulação dos dados.
  - **Tabelas Virtuais:** Tabelas comuns que podem ser criadas no Quoti.
  - **Tabelas Materializadas:** Versões avançadas de tabelas, oferecendo robustez e eficiência.

### Extensão
Interfaces complementares desenvolvidas via low-code usando HTML, Vue.js e CSS, permitindo a criação de experiências visuais personalizadas para diferentes necessidades.

### Fluxo ou Workflow
Automatizações e rotinas que implementam a lógica de negócio dentro da plataforma. Um workflow é desencadeado por eventos específicos e pode realizar ações como envio de e-mails, consultas de dados e preenchimento de formulários. [Saiba mais sobre Workflows](home/Workflow%20designer%204db62d3e43b44dda889f50c721426098.md).

### Usuário
Na plataforma Quoti, um *Usuário* é um agente (pessoa ou *service-account*) que realiza acessos autenticados, seja a páginas públicas ou privadas.

### Permissões
Recursos nativos da plataforma que regulam o acesso e as ações dos usuários, podendo ser:

- **Padrão:** Permissões pré-definidas disponíveis na plataforma.
- **Customizadas:** Permissões criadas por usuários com os devidos privilégios, destinadas a validar ações e definir regras de negócio, como a permissão "product.create".

### Aplicação
Conjunto integrado de extensões, fluxos e tabelas que formam uma solução completa dentro do Quoti.

### Recursos
Conjunto de ferramentas fornecidas pela plataforma Quoti, que incluem:

- Segurança
- Serviços Fundamentais (Core)
- No/Low Code
- Pro Code
- Ferramentas de Desenvolvimento
- Serviços de Notificação e Exibição

Esses recursos são fundamentais para criar, personalizar e otimizar aplicações dentro da plataforma Quoti.
