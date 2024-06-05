import requests
import pytest

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
}
params = {
    "qtype":"movie",
    "tag":"周星驰",
    "page_limit":20,
    "page_start":0

}

def test_post_params():
    r = requests.get('https://movie.douban.com/j/search_subjects',params=params, headers=headers)
    print(r.status_code)
    print(r.json())

if __name__ == '__main__':
    pytest.main()