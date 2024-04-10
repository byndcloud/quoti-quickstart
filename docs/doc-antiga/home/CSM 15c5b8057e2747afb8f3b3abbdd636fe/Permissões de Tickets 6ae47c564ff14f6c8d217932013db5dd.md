# Permissões de Tickets

!!! warning "Documentação descontinuada"
    Esta página faz parte de uma versão descontinuada da documentação. Está presente neste acervo e neste formato enquanto seu conteúdo não é inteiramente migrado para as demais sessões desta documentação.





Para nomenclatura das permissões segue-se o [Padrão de Permissões](https://www.notion.so/Permiss-es-Naming-Convetion-em-desenvolvimento-37d59a55f38d43bba6631720ec8c8873?pvs=21)

# Relações das Permissões

## Create

Permissão exclusiva para criação de novo ticket

1. Permite criar um novo ticket
    
    `ticket.create`
    

## List

Permissões exclusivas para listagem

1. Permite listar todos os tickets, independente de status e atribuição
    
    `ticket.list`
    
2. Permite listar todos os tickets criados pelo usuário logado na plataforma
    
    `ticket.createdByIsMe.list`
    
3. Permite listar todos os tickets atribuídos à mim
    
    `ticket.assignedUserIsMe.list`
    
4. Permite listar todos os tickets pertencentes à filas (grupos) do qual eu sou membro
    
    `ticket.onMyQueues.list`
    
5. Permite listar todos os tickets não atribuídos à ninguém
    
    `ticket.assignedUserIsNull.list`
    
6. Permite listar os tickets cujo o recipient é o usuário da requisição
    
    `ticket.recipientUserIsMe.list`
    
7. Permite listar as interações (eventos) do chamado:
    
    `ticketUserAction.list`
    

## Update

Permissões exclusivas para atualização de um ticket

### Permissões para mudar informações Básicas (não inclui Status)

1. Permite editar as informações base de qualquer ticket (não pode alterar o status)
    
    `ticket.update`
    
2. Permite editar as informações base de tickets atribuídos para mim
    
    `ticket.assignedUserIsMe.update`
    
3. Permite editar a propriedade “body” do ticket, que representa o corpo do chamado
    
    `ticket.updateBody`
    
4. Permite adicionar um anexo a um chamado que o usuário possua acesso
    
    `ticket.addFile`
    

### Permissões para mudar o Status (apenas o status)

1. Permite alterar o status de qualquer ticket
    
    `ticket.updateStatus`
    
2. Permite alterar o status de um ticket atribuído à mim
    
    `ticket.assignedUserIsMe.updateStatus`
    
3. Permite alterar o status de um ticket do tipo “Aprovação”
    
    `ticket.isApproval.updateStatus`
    

### Permissões para mudar AssignedToUser (Responsável)

1. Permite atribuir um ticket para qualquer outro usuário
    
    `ticket.updateAssignedUserToAnyUser`
    
2. Permite atribuir um ticket para o próprio usuário
    
    `ticket.updateAssignedUserToMe`
    
3. Permite remover a sua atribuição a um ticket específico
    
    `ticket.assignedUserIsMe.updateAssignedUserToNull`
    
4. Permite editar as informações base de qualquer ticket (não pode alterar o status)
    
    `ticket.update`
    
5. Permite editar as informações base de tickets atribuídos para mim
    
    `ticket.assignedUserIsMe.update`
    

## Delete

Permissões exclusivas para deleção

1. Permite deletar qualquer ticket
    
    `ticket.delete`
    
2. Permite deletar um ticket criado pelo usuário autenticado
    
    `ticket.createdByIsMe.delete`
