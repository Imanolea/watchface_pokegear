AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'diorite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'diorite'
BUNDLE_NAME = 'watchface_gameandwatch.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['diorite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = []
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'dummy': 10000}
MESSAGE_KEYS_DEFINITION = '/home/imanolea/Documentos/Repositorios/watchface_gameandwatch/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/home/imanolea/Documentos/Repositorios/watchface_gameandwatch/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/home/imanolea/Documentos/Repositorios/watchface_gameandwatch/build/js/message_keys.json'
NODE_PATH = '/home/imanolea/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/imanolea/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/imanolea/.pebble-sdk/SDKs/current/sdk-core/pebble/diorite'
PEBBLE_SDK_ROOT = '/home/imanolea/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['diorite', 'bw', 'rect', 'mic', 'strap', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'diorite', 'BUNDLE_BIN_DIR': 'diorite', 'BUILD_DIR': 'diorite', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_DIORITE', 'PBL_BW', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_HEALTH', 'PBL_SMARTSTRAP', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'diorite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'dummy': 10000}, u'watchapp': {u'watchface': True}, u'displayName': u'Game & Watch', u'uuid': u'2910099c-a1b4-4a25-8a83-c3bd6ff30f51', u'messageKeys': {u'dummy': 10000}, 'companyName': u'Imanolea', u'enableMultiJS': True, u'sdkVersion': u'3', 'versionLabel': u'1.2', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], 'longName': u'Game & Watch', 'shortName': u'Game & Watch', u'resources': {u'media': [{u'memoryFormat': u'1Bit', u'menuIcon': True, u'type': u'bitmap', u'name': u'IMAGE_MENU_ICON', u'file': u'images/icon.png'}, {u'type': u'font', u'name': u'FONT_PERFECT_DOS_25', u'file': u'fonts/game-and-watch-regular.ttf', u'compatibility': u'2.7'}, {u'type': u'font', u'name': u'FONT_PERFECT_DOS_12', u'file': u'fonts/ampm.ttf', u'compatibility': u'2.7'}, {u'type': u'bitmap', u'name': u'IMAGE_BACKGROUND', u'file': u'images/background.png'}, {u'type': u'bitmap', u'name': u'IMAGE_BACKGROUND_ROUND', u'file': u'images/background_round.png'}]}, 'name': u'watchface_gameandwatch'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite']
RESOURCES_JSON = [{u'memoryFormat': u'1Bit', u'menuIcon': True, u'type': u'bitmap', u'name': u'IMAGE_MENU_ICON', u'file': u'images/icon.png'}, {u'type': u'font', u'name': u'FONT_PERFECT_DOS_25', u'file': u'fonts/game-and-watch-regular.ttf', u'compatibility': u'2.7'}, {u'type': u'font', u'name': u'FONT_PERFECT_DOS_12', u'file': u'fonts/ampm.ttf', u'compatibility': u'2.7'}, {u'type': u'bitmap', u'name': u'IMAGE_BACKGROUND', u'file': u'images/background.png'}, {u'type': u'bitmap', u'name': u'IMAGE_BACKGROUND_ROUND', u'file': u'images/background_round.png'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['chalk', 'diorite', 'aplite', 'basalt', 'emery']
TARGET_PLATFORMS = ['diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1496447239
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/imanolea/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
