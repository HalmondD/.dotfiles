from libqtile.lazy import lazy
from libqtile.config import Key, Drag, Click

from global_variables import mod, terminal, browser, file_manager
from groups import groups
from layouts import layouts

keys = [
    # Switch between windows
    Key([mod], "j",
        lazy.layout.left(),
        desc="Move focus to left"
        ),
    Key([mod], "semicolon",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    Key([mod], "k",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    Key([mod], "l",
        lazy.layout.up(),
        desc="Move focus up"
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
        ),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_left(),
        lazy.layout.section_left(),
        desc="Move focus to left"
        ),
    Key([mod, "shift"], "semicolon",
        lazy.layout.shuffle_right(),
        lazy.layout.section_right(),
        desc="Move focus to right"
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc="Move focus down"
        ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc="Move focus up"
        ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "semicolon",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),
   Key([mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
        ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
        ),

    # Run application
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    Key([mod], "b",
        lazy.spawn(browser),
        desc="Launch firefox"
        ),
    Key([mod], "p",
        lazy.spawn("firefox -private-window"),
        desc="Launch firefox in private"
        ),
    Key([mod], "f",
        lazy.spawn(file_manager),
        desc="Launch pcmanfm"
        ),

    # Function
    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
        ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),
    Key([mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
        ),
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
        ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
        ),
    Drag([mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
        ),
    Click([mod], "Button2",
        lazy.window.bring_to_front()
        )
]
