param keyVaultName string
param location string = 'eastus'

resource keyVault 'Microsoft.KeyVault/vaults@2024-12-01-preview' = {
        name: KeyVaultName
        location: location
        properties: {
                sku: {
                        family: 'A'
                        name: 'standard'
                }
                tenantID: subscription().tenantId
                accessPolicies: []
        }
}