pytest tests\test_home_page.py --alluredir=allure_results
pytest -s tests\test_flow_ordering_scoote.py --alluredir=allure_results
allure serve allure_results