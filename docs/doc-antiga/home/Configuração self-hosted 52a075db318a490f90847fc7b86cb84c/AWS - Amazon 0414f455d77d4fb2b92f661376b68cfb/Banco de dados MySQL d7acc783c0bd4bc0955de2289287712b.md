# Banco de dados MySQL

Owner: Levi Nóbrega

Para configurarmos nosso banco de dados em ambiente Amazon, utilizaremos o Amazon RDS.

<aside>
💡 **Amazon RDS** facilita a configuração, a operação e o dimensionamento de um banco de dados relacional na nuvem.

</aside>

[2022-02-16 11-11-37.mp4](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/2022-02-16_11-11-37.mp4)

Em serviços encontre RDS

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled.png)

Escolha a opção “Create Database” e lembre-se de estar na região de nuvem que você deseja instanciar seu ambiente

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled%201.png)

Após confirmar que está na região de nuvem que você deseja, selecione “Create database”

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled%202.png)

Escolha o modo de criação de banco de dados padrão. Além disso, recomendamos utilizar o MySQL 8.0. Porém, também suportamos MySQL 5.7 e MariaDB 10.7

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled%203.png)

Após escolher a versão e modelo do banco de dados, devemos definir o modelo de instância e também as configurações padrões do usuário root do banco de dados.

Todos os campos de settings podem ser definidos de acordo

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled%204.png)

Em instance size, recomendamos utilizar as seguintes configurações:

db.t3.micro - 0 a 10.000 usuários diários

db.t3.medium - 10.0001 a 50.000 usuários diários

db.t3.xlarge - acima de 50.001 usuários diários

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled%205.png)

Em Storage indicamos alocar 20 GB e manter selecionada a opção de autoscaling.

![Untitled](Banco%20de%20dados%20MySQL%20d7acc783c0bd4bc0955de2289287712b/Untitled%206.png)