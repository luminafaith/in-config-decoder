import os, subprocess

# from src.i18n import decode_locres
from src.lua import decode_luas, decode_lua_bytecode
from src.config import decode_configs, decode_helper
# from src.sound import generate_bank_data, load_bank_xml, resort_event_wems

CURRENT_VERSION = '1_7'

LOCALES = [
    'zh',
    'zh-Hant',
    # 'zh-SG', // Singapore Chinese is actually the same as Simplified Chinese
    'en',
    'ja-JP',
    'ko',
    'th',
    'id',
    'pt',
    'es',
    'fr',
    'de',
    'it',
]

LOCALE_REPLACE = {
    'zh': 'zhs',
    'zh-Hant': 'zht',
    # 'zh-SG': 'zh-Hans',
    'en': 'en',
    'ja-JP': 'ja',
    'ko': 'ko',
    'th': 'th',
    'id': 'id',
    'pt': 'pt',
    'es': 'es',
    'fr': 'fr',
    'de': 'de',
    'it': 'it',
}

def decode_lua_and_configs(I_N_CORE_DATA_PATH):
    decode_luas(I_N_CORE_DATA_PATH)
    decode_configs(I_N_CORE_DATA_PATH, version=CURRENT_VERSION)
    decode_helper(I_N_CORE_DATA_PATH, version=CURRENT_VERSION)

def decode_infinity_nikki_data_repo(I_N_CORE_DATA_PATH):
    decode_lua_bytecode(r'cfg/script', os.path.join(I_N_CORE_DATA_PATH, r'X6Game/Content/Script/GenV2', CURRENT_VERSION, 'Cfg/1634995571.lua'))
    decode_configs(I_N_CORE_DATA_PATH, True, CURRENT_VERSION)
    decode_locres(I_N_CORE_DATA_PATH)

def decode_just_configs(I_N_CORE_DATA_PATH):
    decode_lua_bytecode(r'cfg/script', os.path.join(I_N_CORE_DATA_PATH, r'X6Game/Content/Script/GenV2', CURRENT_VERSION, 'Cfg/1634995571.lua'))
    decode_configs(I_N_CORE_DATA_PATH, version=CURRENT_VERSION)

def decode_just_helper(I_N_CORE_DATA_PATH):
    decode_lua_bytecode(r'cfg/script', os.path.join(I_N_CORE_DATA_PATH, r'X6Game/Content/Script/GenV2', CURRENT_VERSION, 'Cfg/1759129374.lua'))
    decode_helper(I_N_CORE_DATA_PATH, version=CURRENT_VERSION)

# def resort_audio(I_N_CORE_DATA_PATH, I_N_STRM_DATA_PATH):
#     generate_bank_data(I_N_CORE_DATA_PATH)
#     load_bank_xml()
#     resort_event_wems(I_N_CORE_DATA_PATH, I_N_STRM_DATA_PATH)

def decodeLocres(I_N_CORE_DATA_PATH):
    os.makedirs('ol', exist_ok=True)
    for locale in LOCALES:
        subprocess.run(['./UnrealLocres', 'export',
                        os.path.join(I_N_CORE_DATA_PATH, f'X6Game/Content/Localization/Game/{locale}/Game.locres'), '-f',
                        'csv', '-o', f'ol/Game_{locale}.csv'], encoding='utf-8')

if __name__ == '__main__':
    I_N_CORE_DATA_PATH = r'C:\Users\leahy\Downloads\FModel\Output\Exports'  # change here to your path, where .pak files are extracted
    I_N_STRM_DATA_PATH = r'D:/Program Files/FModel/Output/Exports'  # change here to your path, where .utoc & .ucas files are extracted
    # decode_just_configs(I_N_CORE_DATA_PATH)
    # decode_just_helper(I_N_CORE_DATA_PATH)
    decodeLocres(I_N_CORE_DATA_PATH)
    # decode_infinity_nikki_data_repo(I_N_CORE_DATA_PATH)
    # resort_audio(I_N_CORE_DATA_PATH, I_N_STRM_DATA_PATH)