# check_proxies.py
import requests
import time
import json

PROXIES = [
    "http://123.141.181.12:5031",
    "http://103.51.205.168:8080",
    "http://149.86.151.151:8080",
    "http://144.22.175.71:1111",
    "http://190.97.232.248:999",
    "http://190.2.57.97:3128",
    "http://118.70.12.171:53281",
    "http://103.136.244.178:8080",
    "http://187.251.130.140:8080",
    "http://210.79.146.82:8085",
    "http://103.131.16.108:8080",
    "http://161.49.116.131:1337",
    "http://190.5.96.154:999",
    "http://4.156.78.45:80",
    "http://103.125.39.93:8080",
    "http://38.183.146.97:8090",
    "http://103.102.12.105:8080",
    "http://185.14.47.247:80",
    "http://181.119.93.50:999",
    "http://103.122.60.213:8080",
    "http://103.121.199.138:62797",
    "http://193.178.210.188:3128",
    "http://45.121.43.193:8080",
    "http://103.114.98.146:8889",
    "http://117.4.244.249:8080",
    "http://51.195.236.200:21688",
    "http://43.245.95.178:53805",
    "http://103.172.121.52:8083"
]


def check_proxies(proxies_list, test_url="https://httpbin.org/ip", timeout=5):
    working_proxies = []

    for proxy in proxies_list:
        try:
            response = requests.get(
                test_url,
                proxies={"http": proxy, "https": proxy},
                timeout=timeout
            )

            if response.status_code == 200:
                working_proxies.append(proxy)
                print(f"✓ Рабочий прокси: {proxy}")
            else:
                print(f"✗ Прокси {proxy} вернул код: {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Ошибка с прокси {proxy}: {e}")

        time.sleep(0.1)

    return working_proxies


def save_working_proxies(proxies_list, filename="working_proxies.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(proxies_list, f, ensure_ascii=False, indent=2)
    print(f"Сохранено {len(proxies_list)} рабочих прокси в {filename}")


if __name__ == "__main__":
    working = check_proxies(PROXIES)
    save_working_proxies(working)