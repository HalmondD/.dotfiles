from libqtile import qtile, widget, bar
from libqtile.config import Screen

from color_schemes import gruvbox_dark, gruvbox_light
from global_variables import terminal

# Function to make minimal window name
def minimal_window_name(text):
    for string in [" - Chromium", " - Mozilla Firefox"]:
        text = text.replace(string, "")
        return text

bar_size = 20

widget_defaults = dict(
    font='Big Blue Terminal Nerd Font',
    fontsize = 12,
    padding = 3,
    background = gruvbox_dark['bg'],
    foreground = gruvbox_dark['fg']
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bar.Bar(
            [
                widget.Sep(
                    padding = 3,
                    size_percent = 100,
                    foreground = gruvbox_dark['bg'],
                    background = gruvbox_dark['bg']
                    ),
 
                widget.GroupBox(
                    disable_drag = True,
                    use_mouse_wheel = False,
                    borderwidth = 3,
                    margin_y = 4,
                    highlight_method = "line",
                    active = gruvbox_dark['fg'],
                    inactive = gruvbox_dark['gray8'],
                    highlight_color = gruvbox_dark['bg'],
                    this_current_screen_border = gruvbox_dark['orange166'], 
                    background = gruvbox_dark['bg'],
                    ),

                widget.TextBox(
                    text = '\u25e2',
                    fontsize = 46,
                    padding = 0,
                    foreground = gruvbox_dark['bg3'],
                    background = gruvbox_dark['bg'],
                    ),

                widget.Sep(
                    padding = 6,
                    size_percent = 100,
                    foreground = gruvbox_dark['bg3'],
                    background = gruvbox_dark['bg3']
                    ),

                widget.CurrentLayout(
                    padding = 0,
                    foreground = gruvbox_dark['fg'],
                    background = gruvbox_dark['bg3']
                    ),

                widget.TextBox(
                    text = '\u25e2',
                    fontsize = 46,
                    padding = 0,
                    foreground = gruvbox_dark['fg1'],
                    background = gruvbox_dark['bg3'],
                    ),

                widget.Prompt(
                    cursor_color = gruvbox_light['fg'],
                    prompt = 'LAUNCH: ',
                    background = gruvbox_dark['fg1'],
                    foreground = gruvbox_dark['bg'],
                    ),

                widget.WindowName(
                    parse_text = minimal_window_name,
                    background = gruvbox_dark['fg1'],
                    foreground = gruvbox_dark['bg'],
                    padding = 0,
                    ),

                widget.TextBox(
                    text = '\u25e2',
                    fontsize = 46,
                    padding = 0,
                    foreground = gruvbox_dark['blue4'],
                    background = gruvbox_dark['fg1']
                    ),

                widget.Sep(
                    padding = 6,
                    size_percent = 100,
                    foreground = gruvbox_dark['blue4'],
                    background = gruvbox_dark['blue4']
                    ),

                widget.Memory(
                    padding = 0,
                    measure_mem = "M",
                    format = "RAM: {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' htop')},
                    foreground = gruvbox_dark['fg'],
                    background = gruvbox_dark['blue4']
                    ),

                widget.TextBox(
                    text = '\u25e2',
                    fontsize = 46,
                    padding = 0,
                    foreground = gruvbox_dark['blue12'],
                    background = gruvbox_dark['blue4']
                    ),

                widget.Sep(
                    padding = 6,
                    size_percent = 100,
                    foreground = gruvbox_dark['blue12'],
                    background = gruvbox_dark['blue12']
                    ),

                widget.CPU(
                    padding = 0,
                    format="{freq_current}GHz @ {load_percent}%",
                    foreground = gruvbox_dark['bg'],
                    background = gruvbox_dark['blue12']
                ),

                widget.TextBox(
                    text = '\u25e2',
                    fontsize = 46,
                    padding = 0,
                    foreground = gruvbox_dark['aqua6'],
                    background = gruvbox_dark['blue12']
                    ),

                widget.Sep(
                    padding = 6,
                    size_percent = 100,
                    foreground = gruvbox_dark['aqua6'],
                    background = gruvbox_dark['aqua6']
                    ),

                widget.Clock(
                    padding = 0,
                    format='%d-%m-%Y %a %I:%M %p',
                    foreground = gruvbox_dark['fg'],
                    background = gruvbox_dark['aqua6']
                    ),

                widget.TextBox(
                    text = '\u25e2',
                    fontsize = 46,
                    padding = 0,
                    foreground = gruvbox_dark['aqua14'],
                    background = gruvbox_dark['aqua6']
                    ),

                widget.BatteryIcon(
                    background = gruvbox_dark['aqua14']
                    ),

                widget.Battery(
                    format = '{char} {percent:2.0%}',
                    charge_char = '',
                    discharge_char = '',
                    empty_char = '',
                    show_short_text = False,
                    padding = 0,
                    foreground = gruvbox_dark['bg'],
                    background = gruvbox_dark['aqua14'],
                    ),

                widget.Sep(
                    padding = 6,
                    size_percent = 100,
                    foreground = gruvbox_dark['aqua14'],
                    background = gruvbox_dark['aqua14']
                    ),
            ],
            bar_size,
        ),
    ),
]
