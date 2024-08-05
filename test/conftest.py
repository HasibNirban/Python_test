import pytest

def pytest_html_report_title(report):
    report.title = "Failed Tests Report"

def pytest_runtest_makereport(item, call):
    # hook for collecting results after each test
    if call.when == "call":
        if call.excinfo is not None:
            # if the test failed, add it to the report
            item._store['failed'] = True

def pytest_html_results_table_row(report, cells):
    # Remove passed tests from the report
    if report.passed:
        cells[:] = []

def pytest_html_results_table_header(cells):
    cells.insert(1, 'Description')
    cells.pop()  # Remove the last element (link to test file)
