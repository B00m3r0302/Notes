```$PDC = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain().PdcRoleOwner.Name
$DN = ([adsi]'').distinguishedName
$LDAP = "LDAP://$PDC/$DN"

$direntry = New-Object System.DirectoryServices.DirectoryEntry($LDAP)

$dirsearcher = New-Object System.DirectoryServices.DirectorySearcher($direntry)
# Can also be "name=<USER_NAME>"
$dirsearcher.filter = "samAccountType=805306368"
$result = $dirsearcher.FindAll()

Foreach($obj in $result)
{
	Foreach($prop in $obj.Properties)
	{
	# If filter is <USER_NAME> this is $prop.memberof
	$prop
	}
	Write-Host "-----------------------------------------------"
}
```