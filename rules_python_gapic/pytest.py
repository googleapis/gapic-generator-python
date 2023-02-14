import sys
import pytest
import os


if __name__ == '__main__':
    # import sys
    # raise Exception(sys.path)
    #raise Exception("test")
    os.environ['PYTHONNOUSERSITE'] = 'True'

    sys.exit(pytest.main([
        '--disable-pytest-warnings',
        '--quiet',
        os.path.dirname(os.path.abspath(__file__))
    ]))
