```powershell
$SUBSCRIPTION_ID = "00000000-0000-0000-0000-000000000000"
$DNS_ZONE_NAME = "youdomain.com"
$KEY_VAULT_NAME = "kv-youdomain-certificate"
$APP_NAME = "youdomain-certificate-letsencrypt"
$AZURE_ROLE = "Contributor"
$RESOURCE_GROUP_NAME = "rg-letsencrypt"

# Login to Azure:

az login
az account set --subscription $SUBSCRIPTION_ID

# Create a resource group and deploy the Bicep template:

az group create --name $RESOURCE_GROUP_NAME --location eastus
az deployment group create --resource-group $RESOURCE_GROUP_NAME --template-file main-AzureDNS.bicep --parameters dnsZoneName=$DNS_ZONE_NAME keyVaultName=$KEY_VAULT_NAME

# Create a Service Principal for automation and grant it access to the Key Vault:

$result = az ad sp create-for-rbac --name "http://$($APP_NAME)-1" --role $AZURE_ROLE --scopes /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP_NAME | ConvertFrom-Json
az keyvault set-policy --name $KEY_VAULT_NAME --object-id $result.appId --secret-permissions get list set delete
```