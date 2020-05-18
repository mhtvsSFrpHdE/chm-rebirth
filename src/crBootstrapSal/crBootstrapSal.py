from crCoreHeader import *  # NOQA: E402
from crConfigSalHeader import * # NOQA: E402
from crEnvironmentSalHeader import *  # NOQA: E402
from crOutputHeader import *  # NOQA: E402

# Module scope config
environment_config_local = None
magic_value_config_local = None
message_config_local = None


def init_bootstrap_sal(environment_config, magic_value_config, message_config):
    global environment_config_local
    global magic_value_config_local
    global message_config_local

    environment_config_local = environment_config
    magic_value_config_local = magic_value_config
    message_config_local = message_config

    init_environment_sal(magic_value_config, message_config)
    init_core_get_catalog_node(environment_config_local, message_config_local)
    init_core_get_index_html(environment_config_local, message_config_local)
    init_output(environment_config_local, message_config_local)

    environment_config_local = init_config_sal(environment_config_local)

    return environment_config_local, magic_value_config_local, message_config_local