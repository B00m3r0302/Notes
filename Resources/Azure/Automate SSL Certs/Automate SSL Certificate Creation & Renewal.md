- Install azure CLI
```bash
sudo apt update && sudo apt install -y python3 python3-venv curl openssl
```
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```
- install Azure Bicep
```bash
az install bicep
```
- EnsureKeyVault and DNSZone are set up or use the template main-AzureDNS.bicep template
- Deploy the bicep file to your resource group
	- Create config.ps1 with the content in config.ps1 to configure and deploy the resources
- Installing dependancies
```bash
sudo apt update && sudo apt install -y python3 python3-venv curl openssl libaugeas0
```
- Remove certbot-auto and any Certbot-OS packages
```bash
sudo apt remove -y certbot
```
- Setting up certbot
```bash
sudo python3 -m venv /opt/certbot
```
```bash
sudo /opt/certbot/bin/pip install --upgrade pip
```
```bash
sudo /opt/certbot/bin/pip install certbot dns-azure
```
- Prepare the Certbot command
```bash
sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot
```
- modified script is in modified_config.ps1
- Then just run the create-certificate-azuredns.sh
## For Manual Install
- Azure login
- Deploy the key vault to the existing resource group with the edited bicep template
```bash
az deployment group create --resource-group HomeServer --template-file main-AzureDNS.bicep --parameters keyVaultName="KEY_VAULT_NAME"
```
- create az ad service principal
```bash
result=$(az ad sp create-for-rbac --name "http://DOMAIN_NAME-certificate-letsencrypt-1" --role $AZURE_ROLE --scopes /subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP_NAME --output json)
```
- Set Key Vault Policy for the SP
```bash
az keyvault set-policy --name $KEY_VAULT_NAME --object-id $(echo $result | jq -r .appId) --secret-permissions get list set delete
```
- login
```bash
az login --service-principal -u APP_ID -p PASSWORD_FOR_SP --tenant TENANT_ID --output none
```
```bash
az account set --subscription SUBSCRIPTION_ID
```
```bash
az account show --output json
```
- create a azure_certbot_credentials.ini that looks like the file in this folder based on the az account show --output json command
- Generate/Refresl SSL Certificate
	- Generates or renews SSL certificates
```
certbot certonly --authenticator dns-azure --preferred-challenge dns --dns-azure-credentials azure_certbot_credentials.ini --force-renew -d DOMAIN_NAME -d *.DOMAIN_NAME --config-dir /home/user/letsencrypt --work-dir /home/user/letsencrypt/work --logs-dir /home/user/letsencrypt/logs --non-interactive --agree-tos --email "EMAIL_ADDRESS"
```
- Install the ACL package and add permissions for your user
```bash
sudo apt install -y acl
```
```bash
sudo setfacl -R -m u:hwoomer:rwx /home/hwoomer/letsencrypt/
```
```bash
sudo setfacl -d -m u:hwoomer:rwx /home/hwoomer/letsencrypt/
```
- Check permissions with
```bash
getfacl /home/hwoomer/letsencrypt/
```
- Convert Certificates to PFX
	- converts generated certificates to PFX format for use in various services
```bash
openssl pkcs12 -export -out /home/user/letsencrypt/live/DOMAIN_NAME/certificate.pfx -inkey /home/user/letsencrypt/live/DOMAIN_NAME/privkey.pem -in /home/user/letsencrypt/live/DOMAIN_NAME/cert.pem -certfile /home/user/letsencrypt/live/DOMAIN_NAME/chain.pem -passout pass:PASSWORD_FOR_SP
```
- Store certificates in Azure Key Vault
```bash
az keyvault secret set --vault-name KEY_VAULT_NAME --name "PEM-Certificate" --file /home/user/letsencrypt/live/DOMAIN_NAME/cert.pem
```
```bash
az keyvault secret set --vault-name KEY_VAULT_NAME --name "PEM-PrivateKey" --file /home/user/letsencrypt/live/DOMAIN_NAME/privkey.pem
```
```bash
az keyvault secret set --vault-name KEY_VAULT_NAME --name "PEM-FullChain" --file /home/user/letsencrypt/live/DOMAIN_NAME/fullchain.pem
```
```bash
az keyvault secret set --vault-name KEY_VAULT_NAME --name "PEM-Chain" --file /home/user/letsencrypt/live/DOMAIN_NAME/chain.pem
```
```bash
az keyvault secret set --vault-name KEY_VAULT_NAME --name "PFX-Certificate-b64" --file /home/user/letsencrypt/live/DOMAIN_NAME/certificate.pfx --encoding base64
```
```bash
az keyvault certificate import --vault-name KEY_VAULT_NAME --name "DOMAIN-SUFFIX (woomer-org)" --file /home/user/letsencrypt/live/$domainName/certificate.pfx --password $clientSecret
```
- Give the appropriate permissions to SP 
```bash
az keyvault set-policy --name kv-woomer-certificate --spn SP_ID
-e3694bfd1ebd --certificate-permissions get list import delete
```
```bash
az keyvault certificate import --vault-name "KEY_VAULT_NAME" --name "DOMAINNAME-SUFFIX" --file "/home/user/letsencrypt/live/DOMAINNAME.SUFFIX/certificate.pfx" --password "PASSWORD_FOR_SP"
```
- in Azure navigate to the azuredevops organizations click my organizations and make a new project
- within the project go to settings service connections and create a new service connection of type 'Azure ResourceManager'
	- Choose Service Principal for authentication and slect the subscription and key vault resource. This service connection will be used to authenticate AzureDevOps to your KeyVault
# Or Just deploy acmebot for automated management