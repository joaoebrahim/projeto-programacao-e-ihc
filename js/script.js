// Estado "carregando" do formulário Registrar estudo.
// O navegador só chama esta função se todos os campos estiverem certos.
function mostrarCarregando() {
    const botao = document.getElementById("botao-registrar");
    const aviso = document.getElementById("carregando");

    botao.disabled = true;
    botao.innerText = "Salvando...";
    aviso.style.display = "block";

    // espera 1,5 segundo e envia o formulário
    setTimeout(() => {
        document.getElementById("form-registro").submit();
    }, 1500);

    // não envia agora (o setTimeout envia depois)
    return false;
}
