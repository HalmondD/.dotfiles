import os
import subprocess

from typing import List  # noqa: F401
from libqtile import hook
from libqtile.lazy import lazy
from libqtile.config import Key

# Import custom options from different folder
import sys
sys.path.append('/home/anh-khoa/.config/qtile/options')
from global_variables import mod, terminal, browser
from layouts import layouts, floating_layout
from bar import screens, widget_defaults
from key_bindings import keys, mouse
from groups import groups

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
for group in groups:
    keys.extend([
        Key([mod], group.name, lazy.group[group.name].toscreen(toggle=True),
            desc=f"Switch to group {group.name}"),
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name),
            desc=f"move focused window to group {group.name}"),
    ])

# Startup applications
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
