
def rgb_to_yuv(R, G, B):
    Y = 0.257*R + 0.504*G + 0.098*B + 16
    U = -0.148*R - 0.291*G + 0.439*B + 128
    V = 0.439*R - 0.368*G - 0.071*B + 128
    color = [Y, U, V]
    return color


def yuv_to_rgb(Y, U, V):
    R = 1.164*(Y-16)+1.596*(V-128)
    G = 1.164*(Y-16)-0.813*(V-128)-0.391*(U-128)
    B = 1.164*(Y-16)
    color = [round(R, 3), round(G, 3), round(B, 3)]
    return color
