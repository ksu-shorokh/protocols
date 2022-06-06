import subprocess
from urllib.request import urlopen
from urllib.error import HTTPError
import re


class Tracert:
    def __init__(self, target):
        self.target = target
        self.trace()

    def trace(self):
        a = subprocess.Popen(["tracert", self.target], stdout=subprocess.PIPE)
        count = 0
        while True:
            line = a.stdout.readline().decode('windows-1251', errors='ignore')
            data = line.split()
            if count > 3:
                if not data:
                    break
                if data[1] == '*' and data[2] == '*' and data[3] == '*':
                    break
                ip = data[-1].replace('[', '').replace(']', '')
                system, country, provider = self.get_as_country_provider(ip)
                print(data[0], ip, system, country, provider)
            count += 1

    def get_as_country_provider(self, ip):
        try:
            with urlopen("https://www.nic.ru/whois/?searchWord=" + ip) as web:
                info = web.read().decode('utf-8')
        except HTTPError as e:
            print(e)
        system = re.search(r'AS\d+', info)
        country = re.search(r'country:\s+\w+', info)
        provider = re.search(r'descr:\s+.*', info)
        if system and country and provider:
            system = system.group(0)
            country = country.group(0).replace("country:", '')
            provider = provider.group(0).replace("descr:", '')
            return system, country, provider
        return '', '', ''


if __name__ == '__main__':
    while True:
        try:
            print("Введите конечный узел:")
            node = input()
            ex = Tracert(node)
        except KeyboardInterrupt:
            break
