```
# Store the domain object in the $domainObj variable 
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()

# Print the domain
$domainObj
```