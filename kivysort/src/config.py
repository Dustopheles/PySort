"""Config parser."""

import os
from configparser import ConfigParser

CONFIG_PATH = 'config.ini'
CONFIG = ConfigParser()

settings_dict = {}
bar_dict = {}
animation_dict = {}

def read_config() -> None:
    """Read config file if exists."""
    if not os.path.exists(CONFIG_PATH):
        print(f"[ERR] {CONFIG_PATH} not found!")
        return
    CONFIG.read(CONFIG_PATH)

def write_config() -> None:
    """Write config to file if exists."""
    if not os.path.exists(CONFIG_PATH):
        print(f"[ERR] {CONFIG_PATH} not found!")
        return
    with open(CONFIG_PATH, 'w', encoding='utf8') as file:
        CONFIG.write(file)

def update_all() -> None:
    """Update all config dictionaries."""
    update_settings()
    update_bar()
    update_animation()

def update_settings() -> None:
    """Update settings dictionary."""
    config = {
        'members': CONFIG.getint('settings', 'members', fallback=10), 
        'lower_limit': CONFIG.getint('settings', 'lower_limit', fallback=1),
        'upper_limit': CONFIG.getint('settings', 'upper_limit', fallback=30)
    }
    settings_dict.update(config)

def fixed_lists(i_list: list) -> list:
    """Fixes stringyfication of lists and returns as list."""
    for index, value in enumerate(i_list):
        if isinstance(value, list):
            continue
        value = value.strip('()[]')
        value = value.replace(' ', '')
        fixed_list = value.split(',')
        fixed_list = [float(x) if x.count('.') == 1 else int(x) for x in fixed_list]
        i_list[index] = fixed_list
    return i_list

def update_bar() -> None:
    """Update bar dictionary."""
    states = []
    states.append(CONFIG.get('bar', 'color_passive', fallback=[90, 90, 90, 0.9]))
    states.append(CONFIG.get('bar', 'color_active', fallback=[180, 180, 180, 0.9]))
    states.append(CONFIG.get('bar', 'color_switch', fallback=[255, 165, 0, 0.9]))
    states.append(CONFIG.get('bar', 'color_sorted', fallback=[60, 179, 113, 0.9]))
    states = fixed_lists(states)

    config = {
        'color_passive':states[0],
        'color_active': states[1],
        'color_switch': states[2],
        'color_sorted': states[3]
    }
    bar_dict.update(config)

def update_animation() -> None:
    """Update animation dictionary."""
    config = {
        'switch_duration': CONFIG.getfloat('animation', 'switch_duration', fallback=1),
        'pause_duration': CONFIG.getfloat('animation', 'pause_duration', fallback=0.1),
        'compare_duration': CONFIG.getfloat('animation', 'compare_duration', fallback=0.25)
    }
    animation_dict.update(config)

def update_value(section: str, key: str, value: str) -> None:
    """Update value in config."""
    CONFIG.set(section, key, value)
    write_config()
    read_config()
    update_all()

read_config()
update_all()
