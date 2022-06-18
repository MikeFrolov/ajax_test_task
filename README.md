# Ajax test task
Test task for the position of QA Automation engineer from Ajax
___
Python Versions - 3.9

    Additional libraries: 
        bitstring==3.1.9
        pytest==7.1.2
___
The solution of the task is implemented in two versions:

    - parsing_bytes_ver1.py (Used a slicer to split the bit string)
    - parsing_bytes_ver2.py (Used bit shifting)

Project structure:

    - The test data file is located at: data/test_data.py;
    - The device settings is located at file: configuration.py;
    - Test configuration is located at file: tests/conftest.py;
    - Tests if located at file: tesys/test_sensor_data.py
___
Testing methods:

    for testing method 'slicer' use command: 
        
         pytest --name slicer

    for testing method 'bit_shifting' use command: 
        
         pytest --name bit_shift (or postpone the name option)