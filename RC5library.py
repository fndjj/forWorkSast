from Crypto.Cipher import ARC4
from PIL import Image

def img_byt_encimg(key):
    with Image.open('24.png') as img:
        img = img.convert('RGB')
    byte_array  = []
    byte_array = img.tobytes()
    cioherobj = ARC4.new(key)
    Cipher  =   cioherobj.encrypt(byte_array)
    img = Image.frombytes('RGB', (img.size), Cipher)
    img.save("encryptrc4.png")
def img_byt_decimg(key):
    with Image.open('encryptrc4.png') as img:
        img = img.convert('RGB')
    byte_array  = []
    byte_array = img.tobytes()
    cioherobj = ARC4.new(key)
    Cipher  =   cioherobj.decrypt(byte_array)
    img = Image.frombytes('RGB', (img.size), Cipher)
    img.save("decryptrc4.png")

# key = b'\x78\x33\x48\xE7\x5A\xEB\x0F\x2F\xD7\xEB\x0F\x2F\xD7\xB1\x69\xBB\x8D\xC1\x67\x87'
# img_byt_encimg(key)
# img_byt_decimg(key)
