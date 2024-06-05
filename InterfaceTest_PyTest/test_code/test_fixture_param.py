import pytest

@pytest.fixture(params=[1, 2, 3, 'linda'])
def prepare_data(request):
    return request.param

def test_one(prepare_data):
    print('testdata:%s' % prepare_data)


def test_two(prepare_data):
    if type(prepare_data) is str:
        print('testdata:%s' % prepare_data)