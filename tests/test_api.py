import pytest

from www import create_app


@pytest.fixture
def client():
    app = create_app("testing")
    return app.test_client()


def test_welcome(client):
    """
    测试首页

    :param client: 测试对象

    :return:
    """
    assert client.get("/").status_code == 200


def test_author_info(client):
    """
    测试获取作者信息

    :param client: 测试对象

    :return:
    """
    assert client.get("/api/v3/template/info").status_code == 200
