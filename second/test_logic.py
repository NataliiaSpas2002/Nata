# Topic 21
# Task 3

import pytest
from homework_021 import FileContextManager
from logic import process_file


@pytest.fixture
def file_obj_fixture(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as file:
        file.write("Line 1\nLine 2\nLine 3\nLine 4")

    with FileContextManager(file_path) as file_obj:
        yield file_obj


def test_process_file(file_obj_fixture):
    result = process_file(file_obj_fixture)
    assert result == 4  # The file has 4 lines






