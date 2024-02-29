# Структура проекта:


## Стуруктура проекта test_saucedemo
"Интуитивно понятная" диаграма работы проекта и его внутренней связанности
```mermaid
erDiagram
    PyTestProject }|..|{ config : Have
    config }|..|{ action : Have
    config }|..|{ geckodriver : Have
    config }|..|{ config_saucedemo : Have
    config_saucedemo ||--o{ geckodriver : Uses-in-Browser-Class
    config_saucedemo ||--o{ action : Import-SeleniumAction-Class
    config_saucedemo ||--o{ test_data : Import-All
    PyTestProject }|..|{ test_saucedemo : Have
    test_saucedemo }|..|{ test_step : Have
    test_saucedemo }|..|{ test_check : Have
    test_saucedemo }|..|{ test_data : Have
    test_step ||--o{ config_saucedemo : Import-Browser-Driver-Action
    test_check ||--o{ test_step : Import-All
```