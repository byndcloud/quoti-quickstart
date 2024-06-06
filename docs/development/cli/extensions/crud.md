## Como desenvolver um CRUD utilizando Quoti Extensions

### Exemplo utilizando o qt-database

```javascript
<template lang="pug">
div
  qt-header(title="Atalhos da plataforma")
  v-container
    qt-database(:headers="headers" storeModule="shortcuts")
</template>

<script>
export default {
  data() {
    return {
      headers: {
        name: {
          label: 'Nome',
          required: true,
          type: {
            name: 'text'
          }
        },
        icon: {
          label: 'Icone',
          required: true,
          type: {
            name: 'icon'
          }
        },
        link: {
          label: 'Link',
          required: true,
          type: {
            name: 'text'
          }
        },
        edit: {
          label: 'Editar',
          width: '100',
          align: 'center',
          sortable: false
        },
        delete: {
          label: 'Deletar',
          width: '100',
          align: 'center',
          sortable: false
        }
      }
    }
  }
}
</script>
```