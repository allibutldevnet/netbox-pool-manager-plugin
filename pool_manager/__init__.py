from netbox.plugins import PluginConfig

class PoolManagerConfig(PluginConfig):
    name = 'pool_manager'
    verbose_name = 'Pool Manager'
    description = 'Simple pool manager'
    version = '1.0.3'
    base_url = 'pool-manager'
    min_version = '4.0.9'

config = PoolManagerConfig
