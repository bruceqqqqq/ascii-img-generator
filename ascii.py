from PIL import Image, ImageDraw, ImageFont
import math

caracteres = "!@#$%&*)_abcdefghijlopqmnrs "[::-1]
caracteresList = list(caracteres)
caracteresTamanho = len(caracteresList)
caracterLargura = 5
caracterAltura = 5
fatorEscala = 1

intervalo = caracteresTamanho / 256


def recebeCaracter(pixelInt):
    return caracteresList[math.floor(pixelInt * intervalo)]


arquivo_txt = open('resultado.txt', 'w')

imagem = Image.open('boku_no_Hero.jpg')

fonte = ImageFont.truetype('C:\\Windows\\Fonts\\Lucon.ttf', 15)

largura, altura = imagem.size
imagem = imagem.resize((int(fatorEscala * largura), int(fatorEscala * altura * (caracterLargura / caracterAltura))),
                       Image.NEAREST)
largura, altura = imagem.size
pixels = imagem.load()

gerandoImagem = Image.new('RGB', (caracterLargura * largura, caracterAltura * altura), color=(0, 0, 0))
desenho = ImageDraw.Draw(gerandoImagem)

for i in range(altura):
    for j in range(largura):
        red, green, blue = pixels[j, i]
        grey = int(red / 3 + green / 3 + blue / 3)
        pixels[j, i] = (grey, grey, grey)
        arquivo_txt.write(recebeCaracter(grey))
        desenho.text((j * caracterLargura, i * caracterAltura), recebeCaracter(grey),
                     font=fonte, fill=(red, green, blue))

    arquivo_txt.write('\n')

gerandoImagem.save("boku_no_hero.png")
