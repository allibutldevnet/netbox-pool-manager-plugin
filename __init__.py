from extras.plugins import PluginConfig

class PoolManagerConfig(PluginConfig):
    name = 'netbox_pool_manager'
    verbose_name = 'Pool Manager'
    description = 'Simple pool manager'
    version = '1.0.2'
    base_url = 'pool-manager'
    min_version = '4.0.9'

config = PoolManagerConfig
