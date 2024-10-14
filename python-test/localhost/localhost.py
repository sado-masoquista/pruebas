import http.server
import socketserver
import os
import socket

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0)
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip
def start_server(ip_address='127.0.0.1', port=8000, directory='.'):
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer((ip_address, port), handler) as httpd:
        print(f"Servidor iniciado en {ip_address}:{port}")
        print(f"Sirviendo archivos desde: {directory}")
        print("Presiona Ctrl+C para detener el servidor.")
        httpd.serve_forever()
if __name__ == "__main__":
    local_ip = get_local_ip()
    print(f"\nTu IP local es: {local_ip}")
    ip_address = input(f"Ingresa la dirección IP (por defecto: {local_ip}): ") or local_ip
    port = input("Ingresa el puerto (por defecto: 8000): ")
    port = int(port) if port else 8000
    directory = input("Ingresa la ruta de la carpeta a servir para el Localhost (por defecto: carpeta actual): ") or '.'
    start_server(ip_address, port, directory)
