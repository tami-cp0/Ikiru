# Ikiru

## Testing

### `unittest`
Python `unittest` library were used to run test on all python files
All test files are in `./test` directory.
To run the test
run the following commands:
```
cat setups/setup_mysql_dev.sql | mysql -uroot -p
```
or 
```
cat setups/setup_mysql_dev.sql | mariadb -uroot -p
```
```
echo "quit" | ./console.py
```
```
python3 -m unittest discover tests
```
