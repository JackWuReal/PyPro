import requests
import pytest


def test_get():
    r = requests.get("https://api.github.com/events")
    print(r.status_code)
    # print(r.text)
    print(r.json())

if __name__ == '__main__':
    pytest.main()

