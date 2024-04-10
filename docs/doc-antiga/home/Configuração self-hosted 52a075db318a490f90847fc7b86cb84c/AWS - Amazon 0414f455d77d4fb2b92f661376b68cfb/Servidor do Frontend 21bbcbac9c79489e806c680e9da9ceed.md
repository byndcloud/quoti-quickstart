# Servidor do Frontend

!!! warning "Documentação descontinuada"
    Esta página faz parte de uma versão descontinuada da documentação. Está presente neste acervo e neste formato enquanto seu conteúdo não é inteiramente migrado para as demais sessões desta documentação.





Para configurarmos os containers utilizaremos o Amazon ECS


💡 **Amazon ECS** facilita a implantação, o gerenciamento e o dimensionamento de contêineres do Docker que executam aplicativos, serviços e processos em lote. O Amazon ECS coloca contêineres em seu cluster com base em suas necessidades de recursos e é integrado a recursos conhecidos como Elastic Load Balancing, grupos de segurança do EC2, volumes do EBS e funções do IAM.



**→ Nosso container é construído utilizando a tecnologia Docker**

- Utilizamos o Container Registiry do Google Cloud como repositório de imagens de container, disponibilizaremos a URL para download das imagens e chaves de autenticação para que possa ser integrado via CI/CD o deployment automático de imagens do nosso container.
- Dentro do container temos:
    - Imagem
        - node:14-alpine
    - Softwares instalados
        - python3
- O Container requer as seguintes variáveis de ambiente para bom funcionamento

```jsx
NODE_ENV=production
VUE_APP_APP_NAME=Whitelabel Solution
VUE_APP_APP_DISPLAY_NAME=Whitelabel Solution
VUE_APP_GCLOUD_PROJECT=client-marketplace
VUE_APP_FIREBASE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
VUE_APP_FIREBASE_AUTH_DOMAIN=beyond-xxxxx.firebaseapp.com
VUE_APP_FIREBASE_DATABASE_URL=https://beyond-xxx.firebaseio.com
VUE_APP_FIREBASE_PROJECT_ID=beyond-xxx
VUE_APP_FIREBASE_STORAGE_BUCKET=beyond-xxx.appspot.com
VUE_APP_FIREBASE_MESSAGING_SENDER_ID=40570897776
VUE_APP_FIREBASE_APP_ID=1:xxxxxxxxxxx:web:xxxxxxxxxxxxxx
VUE_APP_FIREBASE_MEASUREMENT_ID=
VUE_APP_API_BASE_URL=https://your-api-url.com/api/v1/
VUE_APP_EXTENSION_ENVIRONMENT=production
```
