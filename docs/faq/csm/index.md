# 🏗️ Dúvidas frequentes sobre ambientes CSM

Nessa página encontra-se uma lista de perguntas frequentes para integrações e uso da Plataforma Quoti em ambientes CSM.

## Possui dúvidas que ainda não estão nesta documentação?

Abra uma Issue neste repositório: [Clique aqui para abrir uma Issue](https://github.com/byndcloud/quoti-docs/issues)

## Dúvidas sobre catalogo de serviços

### Qual endpoint utilizar para listar as informações do catalogo de Serviço?

Para listar os itens do catálogo de serviços do Quoti, você pode fazer uma solicitação GET para a seguinte URL: `GET https://api.quoti.cloud/api/v1/{orgSlug}/resources/service_catalog_item?where[parent]=home`. Esta solicitação retornará uma lista dos itens de serviço principais no catálogo.

Se você estiver interessado em encontrar os sub-serviços relacionados a um item específico no catálogo, pode usar o parâmetro `where[parent]=<idDoItemPai>`. Substitua <idDoItemPai> pelo ID do item pai do qual você deseja recuperar os sub-serviços. Isso retornará uma lista dos sub-serviços associados ao item pai especificado.

Portanto, com essas duas opções, você pode acessar tanto os itens principais quanto os sub-serviços do catálogo de serviços do Quoti, permitindo uma navegação completa e detalhada através dos serviços disponíveis.

Link da documentação na API do Quoti: [https://api.quoti.cloud/api-explorer/?orgSlug={orgSlug}#/Service_catalog_item/get_{orgSlug}_resources_service_catalog_item](https://api.quoti.cloud/api-explorer/?orgSlug={orgSlug}#/Service_catalog_item/get_{orgSlug}_resources_service_catalog_item)


## Dúvidas a respeito de chamados

### Qual endpoint utilizar para fazer atualizações em um chamado existente?

Resposta em andamento

### Qual endpoint utilizar para consultar status de um chamado específico?

Resposta em andamento

### Como fazer uma consulta por chamados que estão vinculados a um usuário especifico?

Resposta em andamento

### Como fazer uma consulta por chamados que são de um tipo especifico?

Resposta em andamento