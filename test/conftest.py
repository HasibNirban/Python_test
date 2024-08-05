import pytest

def pytest_html_report_title(report):
    report.title = "Failed Tests Report"

def pytest_runtest_makereport(item, call):
    # Hook for collecting results after each test
    if call.when == "call":
        if call.excinfo is not None:
            # if the test failed, add it to the report
            item._store['failed'] = True

def pytest_html_results_table_row(report, cells):
    # Only keep rows in the report for failed tests
    if report.passed:
        cells[:] = []

def pytest_html_results_table_header(cells):
    # Adjust header to include description and remove unnecessary columns
    cells.insert(1, 'Description')
    cells.pop()  # Remove the last element (link to test file)

def pytest_html_results_table_html(report, data):
    # Ensure that detailed output is included for failed tests
    if report.failed:
        data.append(pytest_html.extras.text(report.longreprtext, 'Traceback'))
