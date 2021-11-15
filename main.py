from rgb_yuv import rgb_to_yuv
from rgb_yuv import yuv_to_rgb
from run_lenght import run_lenght
from scipy.fftpack import dct, idct

# ctrl+shift+b to run
if __name__ == '__main__':
    print("#RGB to YUV")
    RGB = [1.0, 1.0, 1.0]
    print("RGB:" + str(RGB))
    YUV = rgb_to_yuv(RGB[0], RGB[1], RGB[2])
    print("YUV:" + str(YUV))
    RGB = yuv_to_rgb(YUV[0], YUV[1], YUV[2])
    print("RGB:" + str(RGB))

    print("\n#Run-Length encoding")
    bytes = [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]
    print("Bytes:" + str(bytes))
    encoded_bytes = run_lenght(bytes)
    print("Encoded Bytes:" + str(encoded_bytes))

    print("\n#DCT i IDCT")
    x = [4, 3, 5, 3, 4]
    print("x:" + str(x))
    X = dct(x, norm='ortho')
    print("X_dct:" + str(X))
    x = idct(X, norm='ortho')
    print("x_idct:" + str(x))
