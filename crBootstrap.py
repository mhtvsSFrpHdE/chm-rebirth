# 3rd
import logging  # NOQA: E402

# Prepare everything about environment, logging, config, international
# Result in one line `from crBootstrap import *` in the main method or file
#
# Prepare logging at the very beginning
# We do not dealing with external error, just print and crash
logging.basicConfig(filename="log.txt")  # NOQA: E402

# My
from crConfigHeader import *
from crEnvironmentHeader import *
from crCoreHeader import *

# Some module require config file to initialize,
# call the init method here
init_environment(message_config, magic_value_config)
init_core_get_catalog_node(message_config)
init_core_get_catalog_html(message_config)