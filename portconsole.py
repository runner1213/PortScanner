import sys
import socket
import threading
from queue import Queue
try:
    from mcstatus import JavaServer
except ImportError as e:
    print(e)

def scan_port(ip, port, output_queue):
    """Функция для проверки состояния порта."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((ip, port)) == 0:
                print(f"Порт {port} открыт")
                output_queue.put(port)
            else:
                print(f"Порт {port} закрыт")
    except Exception:
        pass  # Ошибки обработки можно не выводить


def check_minecraft_server(ip, port):
    """Проверяет, является ли открытый порт сервером Minecraft и получает информацию о нём."""
    try:
        server = JavaServer.lookup(f"{ip}:{port}")
        status = server.status()
        return {
            "port": port,
            "description": status.description,
            "online": f"{status.players.online}/{status.players.max}",
            "address": f"{ip}:{port}"
        }
    except Exception:
        return None


def port_scanner(ip, start_port, end_port, thread_count):
    """Основная функция для сканирования портов с многопоточностью."""
    queue = Queue()
    open_ports = Queue()  # Потокобезопасная очередь для результатов

    def worker():
        while not queue.empty():
            port = queue.get()
            scan_port(ip, port, open_ports)
            queue.task_done()

    for port in range(start_port, end_port + 1):
        queue.put(port)

    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()
        threads.append(thread)

    queue.join()

    return list(open_ports.queue)  # Возвращаем список открытых портов


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Использование: python portconsole.py <домен> <начальный_порт> <конечный_порт> <количество_потоков>")
        sys.exit(1)

    domain = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])
    thread_count = int(sys.argv[4])

    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Сканирование {domain} ({ip_address}) с портов {start_port} до {end_port} с {thread_count} потоками...")

        open_ports = port_scanner(ip_address, start_port, end_port, thread_count)

        if open_ports:
            print("Открытые порты:", ", ".join(map(str, open_ports)))

            # Проверяем каждый открытый порт на наличие Minecraft-сервера
            for port in open_ports:
                mc_info = check_minecraft_server(ip_address, port)
                if mc_info:
                    print(f"\nПорт {mc_info['port']}.:")
                    print(f"Описание: {mc_info['description']}")
                    print(f"Онлайн: {mc_info['online']}")
                    print(f"Айпи: {mc_info['address']}")
                    input("Нажмите Enter, чтобы продолжить...")
        else:
            print("Открытых портов не найдено.")
    except socket.gaierror:
        print("Ошибка: Невозможно получить IP-адрес домена.")

    input("Нажмите Enter, чтобы закрыть это окно...")
