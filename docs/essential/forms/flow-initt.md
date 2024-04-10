# Quoti FormFlows

## O Básico de FormFlows

Os **Quoti FormFlows** representam uma funcionalidade avançada da Plataforma Quoti que permite criar workflows complexos dentro dos formulários. Essencialmente, são scripts JSON que definem a lógica a ser seguida após um formulário ser carregado e enquanto é preenchido pelo usuário.

### Introdução

**FormFlows** transformam formulários estáticos em ferramentas dinâmicas e interativas. Eles são particularmente úteis para:

- Automatizar ações com base na interação do usuário com o formulário.
- Validar dados em tempo real e fornecer feedback instantâneo.
- Integrar com outros sistemas e processos durante o preenchimento do formulário.

### Onde Utilizar

FormFlows são configurados diretamente na página de edição de um formulário no Quoti. No editor de formulários, procure pelo campo "Workflow do formulário" para inserir e editar seu JSON de FormFlow.

## Sessão Completa Sobre FormFlows

### Conceitos

#### Flows

Flows são como estradas dentro de um mapa de navegação, definindo as rotas que os dados seguem. Um arquivo JSON pode conter múltiplos flows, cada um podendo conter condições para sua execução.

#### Nodes

São os pontos de parada ou interseções dentro de um Flow. Cada Node pode realizar uma ou mais ações, operando de forma paralela até sua conclusão antes de passar para o próximo Node.

#### Actions

As Actions são as atividades realizadas em cada Node. Pense nelas como as tarefas que você realiza em cada ponto de parada em uma viagem.

#### Wires

Wires são as conexões entre Nodes, como as estradas que ligam cidades. Eles definem a sequência de navegação entre os Nodes, e podem seguir caminhos diferentes baseados em condições específicas.

### Analogia

Imagine um FormFlow como um parque temático. Cada **Flow** é um caminho pelo parque, cada **Node** é uma atração e as **Actions** são as atividades que você pode realizar em cada atração. Os **Wires** são os caminhos que conectam as atrações, e você pode escolher diferentes caminhos (Wires) baseados nas condições do dia (lógica condicional).

### Utilização e Tipos de Nós e Ações

Quoti FormFlows são incrivelmente versáteis, oferecendo uma variedade de nós e ações para lidar com quase qualquer necessidade de um formulário interativo. Aqui está uma visão mais aprofundada dos tipos de nós e ações disponíveis:

#### Tipos de Nós:

- `fieldWatch`: Para observar mudanças em campos do formulário.
- `watcher`: Para monitorar variáveis específicas.
- `fieldModifier`: Usado para modificar campos do formulário.
- `startup`: Executado quando o formulário é carregado.
- `onSent`: Ativado quando o formulário é enviado.

#### Tipos de Ações:

- `eq` e `notEq`: Para comparações de igualdade ou diferença.
- `cond`: Avalia uma condição e decide o próximo passo.
- `replace`, `visibility`, `required`: Alteram propriedades dos campos do formulário.
- `allowed`: Verifica permissões do usuário.
- `action`: Executa uma ação da loja do Quoti.
- `req`: Realiza uma requisição HTTP.
- `set`: Define valores em variáveis.

### Variáveis e Execução

Você pode definir variáveis que serão usadas durante a execução do FormFlow, bem como definir as condições sob as quais diferentes partes do Flow serão executadas.

### Exemplos Práticos

Incluir exemplos detalhados ajuda os usuários a entenderem melhor como implementar FormFlows. Por exemplo, um `fieldWatch` pode ser configurado para observar um campo de "data de início" e, se a data for alterada, um `fieldModifier` pode automaticamente ajustar um campo de "data de término".

