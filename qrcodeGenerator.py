import qrcode

# URL que nunca cambia (apunta al archivo redirect.html)
url_fija = "https://misitio.github.io/redirect.html"

qr = qrcode.make(url_fija)
qr.save("qr_dinamico.png")
