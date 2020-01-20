# Python Console utility project

Run command from project directory:
```
python generator.py --path_to_save_files=test --data_schema="{\"date\":\"timestamp:\", \"name\": \"str:rand\", \"type\":\"str:['client', 'partner', 'government']\", \"age\": \"int:rand(1, 90)\"}"
```

Command for running unit test:
`python -m unittest discover`

Test result:
```
C:\Users\projects\python_cmd>python -m unittest -v
test_should_clean_dir (test.test_file_utils.FileUtilsTestCase) ... ok
test_should_throw_exception (test.test_file_utils.FileUtilsTestCase) ... ok
test_should_create_data (test.test_schema.SchemaTestCase) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.012s
```