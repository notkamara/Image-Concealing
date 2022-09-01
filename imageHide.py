from PIL import Image

targetDir = "cat.bmp"
encryptionDir = "evil.bmp"
encryptedDir = "encrypted.bmp"


def hideImage(targetDir, encryptionDir):
    img = Image.open(targetDir)
    image = img.load()

    img2 = Image.open(encryptionDir)
    hiddenImage = img2.load()

    print("Please wait...")
    
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            hiddenRGB =  hiddenImage[x, y]
            currentRGB = image[x, y]
            
            r = currentRGB[0]
            g = currentRGB[1]
            b = currentRGB[2]

            hR = hiddenRGB[0]
            hG = hiddenRGB[1]
            hB = hiddenRGB[2]

            if ~(240|(~hiddenRGB[0])) >= 8:
                hR = (~(15|~(hiddenRGB[0] + 16))) >> 4
            else:
                hR = (~(15|~(hiddenRGB[0]))) >> 4
            if ~(240|(~hiddenRGB[0])) >= 8:
                hG = (~(15|~(hiddenRGB[1] + 16))) >> 4
            else:
                hG = (~(15|~(hiddenRGB[1]))) >> 4
            if ~(240|(~hiddenRGB[0])) >= 8:
                hB = (~(15|~(hiddenRGB[2] + 16))) >> 4
            else:
                hB = (~(15|~(hiddenRGB[2]))) >> 4
        
            if ~(240|(~currentRGB[0])) >= 8:
                r = (~(15|(~(currentRGB[0] + 16)))) | hR
            else:
                r = (~(15|(~(currentRGB[0])))) | hR
            if ~(240|(~currentRGB[1])) >= 8:
                g = (~(15|(~(currentRGB[1] + 16)))) | hG
            else:
                g = (~(15|(~(currentRGB[1])))) | hG
            if ~(240|(~currentRGB[2])) >= 8:
                b = (~(15|(~(currentRGB[2] + 16)))) | hB
            else:
                b = (~(15|(~(currentRGB[2])))) | hB

            currentRGB = (r, g, b)
            image[x, y] = currentRGB
    img.save("encrypted.bmp", "BMP")
    print("Image hidden.")
    
def revealImage(encryptedDir):
    img = Image.open(encryptedDir)
    image = img.load()

    print("Please wait...")

    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            currentRGB = image[x, y]

            r = currentRGB[0]
            g = currentRGB[1]
            b = currentRGB[2]
            
            r = (~(240|(~r))) << 4
            g = (~(240|(~g))) << 4
            b = (~(240|(~b))) << 4

            currentRGB = (r, g, b)
            image[x, y] = currentRGB
    img.save("revealed.bmp", "BMP")
    print("Image revealed.")
    
#hideImage(targetDir, encryptionDir)

revealImage(encryptedDir)
