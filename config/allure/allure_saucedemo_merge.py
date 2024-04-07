import subprocess
import os
from datetime import datetime

def run_pytest():
    try:
        test_files_path = r"C:\Users\Lena\PycharmProjects\pythonProjectgiiiiiiiiiiit\vzhuh\test_saucedemo"
        subprocess.run(["pytest", "--alluredir=allure-results"], check=True, cwd=test_files_path)
    except subprocess.CalledProcessError as e:
        print(f"Ошибка {e}")
    except Exception as ex:
        print(f"Ошибка {ex}")

def generate_allure_report():
    allure_path = r"C:\Users\Lena\PycharmProjects\pythonProjectgiiiiiiiiiiit\vzhuh\config\allure\allure-2.27.0\bin"
    results_path = r"C:\Users\Lena\PycharmProjects\pythonProjectgiiiiiiiiiiit\vzhuh\test_saucedemo\allure-results"
    report_path = r"C:\Users\Lena\PycharmProjects\pythonProjectgiiiiiiiiiiit\vzhuh\test_saucedemo\allure-reports"
    # Создаем уникальную директорию для результатов текущего прогона
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    current_results_dir = os.path.join(results_path, current_time)
    os.makedirs(current_results_dir, exist_ok=True)
    # Запуск тестов
    run_pytest()
    # Генерация отчета
    subprocess.run(["allure.bat", "generate", results_path, "-o", report_path], shell=True, cwd=allure_path)
    # Открытие отчета в браузере
    subprocess.run(["allure.bat", "open", report_path], shell=True, cwd=allure_path)

if __name__ == "__main__":
    generate_allure_report()