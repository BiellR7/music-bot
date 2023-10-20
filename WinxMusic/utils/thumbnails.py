from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

# ... (seu código anterior) ...

# Texto a ser adicionado com fundo transparente e borda preta
text = "Devs: Biell & Henx"

# Crie uma imagem com o texto
mask = Image.new("L", (500, 100), 0)
draw = ImageDraw.Draw(mask)
font = ImageFont.truetype("assets/RobotoBold.ttf", 40, encoding="utf-8")

# Desenhe o texto no fundo preto
draw.text((10, 10), text, 255, font=font)

# Crie uma imagem RGB com fundo transparente
text_image = Image.new("RGBA", (500, 100))
draw = ImageDraw.Draw(text_image)

# Cole a máscara na imagem com um fundo transparente
text_image.paste((0, 0, 0, 255), (0, 0, 500, 100), mask)

# Defina a posição do texto na imagem de fundo
text_x = 530
text_y = 5

# Cole a imagem do texto na imagem de fundo com um fundo transparente
background.paste(text_image, (text_x, text_y), text_image)

# ... (continuação do seu código) ...
