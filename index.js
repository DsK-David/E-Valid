function EValid(email){
    const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexEmail.test(email)
}
module.exports = {
    EValid
}
