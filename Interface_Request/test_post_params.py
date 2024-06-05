import requests
import pytest

param = {
    'shouji': '13456755448',
    'appkey': '0c818521d38759e1'
}

def test_post_params():
    r = requests.post('http://sellshop.5istudy.online/sell/shouji/query', params=param)

    print(r.status_code)
    print(r.json())
if __name__ == '__main__':
    pytest.main()