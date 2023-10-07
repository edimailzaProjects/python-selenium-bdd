#language: pt

  @login
  Funcionalidade: Login

     @login_sucesso
     Cenário: Login de sucesso
       Dado que o site carregou
       Quando insiro meu login "admin" e senha "admin123"
       Então eu serei direcionado para a página de dashboard
       E posso me desconectar


      @login_falho
      Esquema do Cenario: Login falho
       Dado que o site carregou
       Quando insiro meu login "<login>" e senha "<senha>"
       Então eu não serei conectado com sucesso
        Exemplos:
          | login  | senha    |
          |  aaa   | bbb      |
          |  admin | aaa      |