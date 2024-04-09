# Development &  Production modes

Owner: Levi Nóbrega

Ao [desenvolver extensões](https://www.notion.so/Quoti-Extensions-d3af129ede05415fb370dee8587d758f?pvs=21) utilizando o Quoti os desenvolvedores podem contar com dois ambientes de execução dentro de uma mesma organização para cada extensão.

## Development mode

O ambiente de desenvolvimento é acessível pelo link: `[https://quoti.cloud/{organização}/develop/{path_da_extensão}](https://quoti.cloud/{organização}/develop/{path_da_extensão})`.

Este modo tem como principal finalidade dar agilidade na visualização das alterações de código da sua extensão durante o processo de desenvolvimento. Para isso, este ambiente conta com a funcionalidade de *live reload* que atualiza a página toda vez que uma alteração no código local é feita. **O *live reload* é ativado ao executar o comando `qt serve` da [Quoti CLI](Quoti%20CLI%2012e230f5cbd6471f92e10822e4db210c.md) na pasta de uma extensão.

<aside>
💡 Clique para mais detalhes de como [desenvolver extensões](https://www.notion.so/Quoti-Extensions-d3af129ede05415fb370dee8587d758f?pvs=21) ou como utilizar a [Quoti CLI](Quoti%20CLI%2012e230f5cbd6471f92e10822e4db210c.md).

</aside>

## Production mode

O ambiente de produção é acessível pelo link:`[https://quoti.cloud/{organização}/develop/{path_da_extensão}](https://quoti.cloud/{organização}/develop/{path_da_extensão})`.

Diferente do modo de desenvolvimento, este ambiente não possui funcionalidade de *live reload*, exigindo que o usuário atualize manualmente a página caso queira visualizar a versão aplicada no modo de produção.

O modo de produção conta ainda com um histórico de versões que podem ser renomeadas e ativadas a qualquer momento. 

<aside>
💡 Clique para mais detalhes de como [controlar as versões do ambiente de produção](Versionamento%20de%20extenso%CC%83es%2094718b18bfb74830bc9f37326774dce3.md).

</aside>

## Troubleshooting

- Qualquer usuário da organização tem acesso à extensão no ambiente de desenvolvimento?
    
    Qualquer usuário da organização que conheça o link da sua extensão em ambiente de desenvolvimento poderá executá-la. Caso queira restringir o acesso da sua extensão em ambiente de desenvolvimento para você ou usuários específicos, você deve incluir no código da sua extensão checagens do usuário, [perfil](../home.md), [permissão](ACLs%20&%20Roles%207b116e5c9d9a4fbf937ba3ad57f40da2.md) ou [grupo](../home.md).
    

[FAQ: Developing extensions with Quoti](Development%20&%20Production%20modes%20fa2447cbee4d454e958644a2362230a9/FAQ%20Developing%20extensions%20with%20Quoti%207156657ad2ee407491763905650af4ac.md)