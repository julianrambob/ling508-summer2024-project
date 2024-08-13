from db.mysql_repository import *
from app.service import Service

service = Service()
repo = MysqlRepository()

#tests for use case 1
def test_is_cyrillic():

    assert service.is_cyrillic('собака') == True
    assert service.is_cyrillic('hello') == False


#test for use case 2
def test_convert_cyrillic():

    assert service.convert_to_cyrillic('rabotoyi') == 'работой'
    assert service.convert_to_cyrillic('privyet rabotnik!') == 'привет работник!'
    assert service.is_cyrillic(service.convert_to_cyrillic('dom')) == True

