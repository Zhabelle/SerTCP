import nacl.utils as pynacl
import socket


#se modificó el código de la tarea de aleatorios para convertirlo en una función
#que regrese lo generado como cadena de texto
def getRand() -> str:
    bs = pynacl.random(size=128)
    r = 0
    for c in bs:
        r += c
    return '{0:X}'.format(r)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 65432))
    s.listen()
    c,a = s.accept()
    print(f"{a} conectado")
    ale = getRand().encode()
    print(f'Enviando aleatorio {ale}...')
    c.sendall(ale)
    c.close()
    s.close()
