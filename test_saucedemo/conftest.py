def pytest_configure(config):  # pytest --markers
    config.addinivalue_line("markers", "smoke: Дымовые тесты")