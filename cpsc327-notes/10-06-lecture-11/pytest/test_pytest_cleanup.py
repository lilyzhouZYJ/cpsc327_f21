import pytest
import tempfile
import shutil
import os.path


@pytest.fixture         # both setup and cleanup
def temp_dir():
    temp_dir = tempfile.mkdtemp()       # create temporary directory
    print(temp_dir)
    yield temp_dir          # like return, but can continue with the rest of the function
    shutil.rmtree(temp_dir) # remove the directory

@pytest.fixture
def fixture2(request):      # request: gives initial info on the context of the test
    print()
    print(dir(request))
    print()
    print(dir(request.config))
    print()
    print(str(request.config.invocation_dir))
    print()
    print(request.function)
    

def test_osfiles(temp_dir, fixture2):
    os.mkdir(os.path.join(temp_dir, "a"))
    os.mkdir(os.path.join(temp_dir, "b"))
    dir_contents = os.listdir(temp_dir)
    assert len(dir_contents) == 2
    assert "a" in dir_contents
    assert "b" in dir_contents