# E-Valid :tada:

Este é um simples validador de e-mails em JavaScript que utiliza um padrão de expressão regular para garantir a validação básica de endereços de e-mail.

## Como Usar

### Instalação :package:

Antes de usar o E-Valid, certifique-se de ter o Node.js e o npm instalados em sua máquina.

```bash
npm install e-valid
```

### Exemplo de Uso

```javascript
const { EValid } = require('./index')

const email = 'usuario@dominio.com'
if(EValid(email)){
    console.log('email valido')
}
else{
    console.log('email invalido')
}
```

## Função `EValid`

A função `EValid` aceita uma string contendo um endereço de e-mail e retorna `true` se o e-mail for válido, conforme o padrão definido pela expressão regular, e `false` caso contrário.

```javascript
const emailValido = EValid('usuario@dominio.com');
console.log(emailValido);  // Saída: true
```

## Contribuição

Se encontrar problemas ou melhorias potenciais, sinta-se à vontade para contribuir para este projeto. Abra uma issue para discussão ou envie um pull request com suas alterações.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE.md).
