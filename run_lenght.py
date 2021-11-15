def run_lenght(bytes):
    encoded_bytes = []
    count = 1
    bit = bytes[0]  # agafem el primer bit
    for i in range(1, len(bytes)):  # per tota la sequencia de bits
        if bytes[i] == bit:  # si el seguent bit es igual count+1
            count = count + 1
        else:  # si el seguent bit no es igual fem el append del count final
            encoded_bytes.append([bit, count])
            bit = bytes[i]
            count = 1

    encoded_bytes.append([bit, count])  # fer append de l'ultima sequencia
    return encoded_bytes
