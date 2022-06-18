def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="bit_shift")