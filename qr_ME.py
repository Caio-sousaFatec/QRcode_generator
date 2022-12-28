import qrcode



link_rede = {
    "github" : "https://github.com/Caio-sousaFatec",
    "linkedIn" : "https://www.linkedin.com/in/caio-sousa-75b631124/"
}

for produtos in link_rede:
    imagem_qrcode = qrcode.make(link_rede[produtos])
    imagem_qrcode.save(f'qrcodeSocial{produtos}.png')
