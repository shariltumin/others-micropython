# -freeze("$(PORT_DIR)/modules")
freeze("$(PORT_DIR)/modules", ("_boot.py", "espnow.py", "flashbdev.py", "inisetup.py"))
# -include("$(MPY_DIR)/extmod/asyncio")

# board specific modules
# -freeze("modules", 'app.py')

# Require some micropython-lib modules.
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")
require("umqtt.robust")
require("umqtt.simple")
require("upysh")
require("mip")
require("ntptime")
require("urequests")
# -require("webrepl")

# my extra modules
freeze('$(MPY_DIR)/extra', 'Caesar.py')
freeze('$(MPY_DIR)/extra', 'CryptoXo.py')
# -freeze('$(MPY_DIR)/extra', 'PickleDB.py')
# -freeze('$(MPY_DIR)/extra', 'Tasks.py')
# -freeze('$(MPY_DIR)/extra', 'Guard.py')
freeze('$(MPY_DIR)/extra', 'sdcard.py')
freeze('$(MPY_DIR)/extra', 'dotdict.py')
freeze('$(MPY_DIR)/extra', 'mt_profiler.py')
freeze('$(MPY_DIR)/extra', 'mqueue.py')
freeze('$(MPY_DIR)/extra', 'Worker.py')
freeze('$(MPY_DIR)/extra', 'pipe.py')
freeze('$(MPY_DIR)/extra', 'Telnet.py')
freeze('$(MPY_DIR)/extra', 'Ping.py')
freeze('$(MPY_DIR)/extra', 'Ramdisk.py')
freeze('$(MPY_DIR)/extra', 'tscp.py')
# -freeze('$(MPY_DIR)/extra', 'wifi.py')
# -freeze('$(MPY_DIR)/extra', 'I2CInterface.py')
# -freeze('$(MPY_DIR)/extra', 'AXP2101.py')

