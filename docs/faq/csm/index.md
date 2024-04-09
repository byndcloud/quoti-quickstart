# 🏗️ Dúvidas frequentes sobre ambientes CSM

Nessa página encontra-se uma lista de perguntas frequentes para integrações e uso da Plataforma Quoti em ambientes CSM.

## Possui dúvidas que ainda não estão nesta documentação?

Abra uma Issue neste repositório: https://github.com/byndcloud/quoti-docs/issues

## Dúvidas sobre catalogo de serviço

### Qual endpoint utilizar para listar as informações do catalogo de Serviço?

Resposta em andamento

## Dúvidas a respeito de chamados

### Qual endpoint utilizar para fazer atualizações em um chamado existente?

Resposta em andamento

### Qual endpoint utilizar para consultar status de um chamado específico?

Resposta em andamento

### Como fazer uma consulta por chamados que estão vinculados a um usuário especifico?

Resposta em andamento

### Como fazer uma consulta por chamados que são de um tipo especifico?

Resposta em andamento


Aqui está a FAQ organizada e formatada em Markdown para a plataforma Quoti, com os textos aprimorados para clareza e precisão:

---

## FAQ - Quoti

### Verificação dos Serviços no Catálogo e Listagem

**Como consultar os serviços no catálogo?**
- **Endpoint**: `GET api.quoti.cloud/resources/service_catalog_item?where[parent]=home`
- **Descrição**: Use este endpoint para listar os serviços disponíveis no catálogo. Para acessar sub-serviços, substitua `home` pelo `idDoItemPai` desejado no parâmetro `where[parent]`.

### Informações do Catálogo de Serviço

**Como listar as informações do catálogo de serviço?**
- **Endpoint**: `GET api.quoti.cloud/resources/service_catalog_item/<id>`
- **Descrição**: Este endpoint fornece detalhes sobre um item específico do catálogo de serviços, incluindo FAQs e textos descritivos encontrados em `pageBody`.
- Para categorias e formulários relacionados:
  - Use `GET api.csm.quoti.cloud/resources/categories/<categoryId>` para listar uma categoria e obter o ID do formulário de perguntas.
  - Para as perguntas de um formulário específico, utilize `GET api.quoti.cloud/resources/forms/<formId>`.

### Consulta por Chamados de um Usuário Específico

**Como fazer uma consulta por chamados vinculados a um usuário específico?**
- **Endpoint**: `GET api.csm.quoti.cloud/tickets?where[assignedToUser][0]=<idDoUsuario>`
- **Descrição**: Este endpoint permite listar chamados atribuídos a um usuário específico, substituindo `<idDoUsuario>` pelo ID apropriado do usuário.

### Atualizações em um Chamado Existente

**Qual endpoint utilizar para fazer atualizações em um chamado?**
- **Endpoint**: `PUT api.csm.quoti.cloud/tickets/<ticketId>`
- **Descrição**: Use este endpoint para atualizar as informações de um chamado existente. Substitua `<ticketId>` pelo ID do chamado que você deseja atualizar.

### Consulta de Status de um Chamado Específico

**Como consultar o status de um chamado específico?**
- **Endpoint**: `GET api.csm.quoti.cloud/tickets/<ticketId>`
- **Descrição**: Este endpoint fornece o status atual de um chamado específico. O status é retornado no corpo da resposta da requisição.

---

