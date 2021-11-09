import pytest


@pytest.fixture(scope="class")
def test_requirements():
    print(" this is the pre requisit and will be executed first")
    yield
    print("execution completed and all files closed")


@pytest.fixture(scope="class")
def test_dataload():
    return["Revathi","NS","revathi.akshay@gmail.com"]


##to give multiple data sets, use param inside the fixture seclaration
##inside the fixture function use request keyword
##inside the body, use retur request.param
@pytest.fixture(params=[["chrome","RevathiNS","Ananya111"],["IE","Akshay","Akshay123"],["FireFox","Ananya","1JM123"]])
def test_dataload1(request):
    return request.param
