import crConfigSal as _crConfigSal  # NOQA: E402
import crCoreHeader as crCore  # NOQA: E402
import crEnvironmentSalHeader as crEnvironmentSal  # NOQA: E402
import crOutputHeader as crOutput  # NOQA: E402
import crUnpack  # NOQA: E402

# The method will modify config files generated by crBootstrap to add custom preprocessor


def apply_config_preprocessor(environment_config, magic_value_config, message_config):
    # Create modified config
    myConfigGroup = environment_config, magic_value_config, message_config
    environment_config_local, magic_value_config_local, message_config_local = _crConfigSal.init_config_sal(myConfigGroup, crEnvironmentSal)

    # Use modified config to initialize other module
    crEnvironmentSal.init_environment_sal(magic_value_config_local, message_config_local)

    crCore.init_core_get_catalog_node(environment_config_local, message_config_local)
    crCore.init_core_get_index_html(environment_config_local, message_config_local)

    crOutput.init_output(environment_config_local, message_config_local)

    crUnpack.init_crUnpack(environment_config_local)

    # Transfer modified config back to main level scope
    return environment_config_local, magic_value_config_local, message_config_local
