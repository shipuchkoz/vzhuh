def pytest_configure(config):  # pytest --markers
    config.addinivalue_line("markers", "smoke_bankxyz: Дымовые тесты банка xyz")