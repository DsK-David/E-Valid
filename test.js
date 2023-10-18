const {EValid} = require('./index')

const email = 'usuario@dominio.com'
if(EValid(email)){
    console.log('email valido')
}
else{
    console.log('email invalido')
}