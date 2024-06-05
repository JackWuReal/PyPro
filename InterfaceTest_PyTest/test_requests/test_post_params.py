import requests
import pytest

param = {
    'shouji': '13456755448',
    'appkey': '0c818521d38759e1'
}


def test_post_params():
    r = requests.post('http://sellshop.5istudy.online/sell/shouji/query', params=param)
    req  = r.json()
    assert r.status_code == 200
    assert req.get('msg') == "ok"
    assert req["result"]["shouji"] == "13456755448"
    assert req["result"]["city"] == "北京"


if __name__ == '__main__':
    pytest.main(["-v","-s"])