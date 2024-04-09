# Quoti Auth

Owner: Levi Nóbrega

É o sistema de autenticação built-in que pode ser usado como middleware de autenticação nas suas APIs desenvolvidas e hospedadas em qualquer lugar.

Atualmente o Quoti Auth conta com um [SDK público](https://www.npmjs.com/package/quoti-auth) para ser utilizado em *web servers* desenvolvidos utilizando [node.js](https://nodejs.org/en/download/) e [express.js](https://expressjs.com/pt-br/) como um *middleware*.

## Tutoriais

- **Como instalar o SDK do Quoti Auth?**
    
    ## **Instalação**
    
    Pelo terminal, acesse a pasta onde está o seu projeto [node.js](https://nodejs.org/en/download/) & [express.js](https://expressjs.com/pt-br/). Você pode usar o gerenciador de pacotes NPM para fazer a instação do SDK utilizando o terminal:
    
    ```bash
    npm install quoti-auth
    ```
    
- **Como utilizar nos seus *endpoints*?**
    
    ## **Inicializando o Quoti Auth**
    
    ```jsx
    const { quotiAuth } = require('quoti-auth')
    
    quotiAuth.setup({
        orgSlug: 'someOrgSlug',
        apiKey: 'some-api-key',
        logger: console 
    })
    ```
    
    ## **Usando**
    
    Injetando dados do usuário em `req.user`:
    
    ```jsx
    app.post('/', QuotiAuth.middleware(), async (req, res) => {
      console.log('User:', req.user.name)
      res.send('OK!')
    })
    ```
    
    Na prática, esse middleware fará a autenticação com a API do Quoti usando o **[Authorization Header](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Authorization)** que já estaria contido no seu `req.headers`. Este header pode ser:
    
    - Authorization: Bearer TOKEN
    - Authorization: BearerStatic TOKEN
- **Como checar as permissões do usuário no Quoti automaticamente?**
    
    ## **Checando permissões do usuário**
    
    Neste exemplo, o middleware vai checar se o usuário tem a permissão `posts.filter`. Caso ele não tenha, o Quoti Auth vai retornar um erro 401 no endpoint:
    
    ```jsx
    app.post('/', QuotiAuth.middleware([['posts.filter']]), async (req, res) => {
      res.send(`OK! O usuário ${req.user.name} tem a permissão 'posts.filter'`)
    })
    ```
    
- **Configurações avançadas**
    
    ### **Substituindo a função getUserData**
    
    ```jsx
    const { quotiAuth } = require('quoti-auth')
    
    // Esta função será chamada passando o token do usuário que você está consultando para retornar os dados do usuário.
    async getUserData (bearerToken) {
      const url = process.env['api_url'] || 'https://api.quoti.cloud/api/v1/'
      const headers = {
        ApiKey: 'some-api-key'
      }
      const { data } = await axios.post(`${url}${this.orgSlug}/auth/login/getuser`, 
    		{ token: bearerToken }, 
    		{ headers }
      )
    
      // O retorno dessa função será injetado em req.user
      return data.user
    }
    
    quotiAuth.setup({
        orgSlug: 'someOrgSlug',
        apiKey: 'some-api-key',
        getUserData: getUserData,
        logger: console 
    })
    ```
    

## Troubleshooting

- Como utilizar o Quoti Auth em projetos sem [express.js](https://expressjs.com/pt-br/)?
    
    Atualmente, disponibilizamos o pacote de [NPM do Quoti Auth](https://www.npmjs.com/package/quoti-auth) apenas para express.js. Porém, é possível utilizar os mesmos recursos em outros plugins de web servers, como o [fastify.js](https://www.fastify.io/).
    
    Para isso, você deverá criar seu próprio *middleware* e realizar requisições REST passando o *token* do usuário para a [API de autenticação do Quoti](https://api.quoti.cloud/api-explorer/#/Auth/post__orgSlug__auth_login_getuser) (`https://quoti.cloud/{organização}/auth/login/getuser`). 
    
    Com o resultado dessa API o seu *middleware* poderá retornar para o endpoint os dados do usuário que foram retornados, como: `nome, email, permissões e grupos`.
    
    Você também pode analizar os [códigos do middleware disponibilizado por nós](https://github.com/byndcloud/quoti-auth) e realizar pequenas adaptações para ser utilizado no seu webserver:
    
    [https://github.com/byndcloud/quoti-auth](https://github.com/byndcloud/quoti-auth)
    
- Como utilizar o Quoti Auth em projetos em outras linguagens (Python, C#, GO, etc.)?
    
    Atualmente, disponibilizamos o Quoti Auth como pacote apenas para a linguagem Node.js. Porém, é possível utilizar os mesmos recursos de autenticação encapsulados em *endpoints* de *web servers* desenvolvidos em outras linguagens.