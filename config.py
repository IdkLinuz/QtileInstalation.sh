# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from typing import List

import os
import subprocess
mod = "mod4"
terminal = guess_terminal()

color1 = '#282A36'
tipo = 0


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "m", lazy.spawn("/bin/bash /home/idk/.config/rofi/scripts/launcher_t3"), desc="Launch Rofi"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave"),
    Key([mod], "t", lazy.spawn("alacritty -e ranger"), desc="Launch Thunar"),
    Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod], "l", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "p", lazy.spawn("/bin/bash /home/idk/.config/rofi/powermenu/type-3/powermenu.sh"), desc="Launch Power-Menu"),
    Key([mod], "F12", lazy.spawn("coreshot"), desc ="Launch CoreShot"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    #brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]


#LISTADO DE FUENTES

#nf-cod-terminal_bash
#
#nf-dev-visualstudio
#nf-fa-spotify

#groups = [Group(i) for i in "1234567890"]
groups = [Group(i) for i in[
    "", "", "", "", "", "", "", "", ""
]]

for i, group in enumerate(groups):
    numeroEscritorio =str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_width=3,
        border_focus="#7400FF",
        single_border_width=0,
        margin=8,
        margin_on_single=8,
        border_normal="#222222",
        change_size=10,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    #ayout.Floating(border_width=3,border_focus="#7400FF",),
]

widget_defaults = dict(
    font= 'UbuntuMono Nerd Font Bold',
    fontsize=15,
    padding=0,
)
extension_defaults = widget_defaults.copy()
screens = [
    Screen(
        top=bar.Bar(
            [
                #widget.CurrentLayout(),

                widget.TextBox(
                    text = "",
                    fontsize = 25,
                    padding = 15,
                    foreground = "#7BDEFF",
                ),

                widget.GroupBox(
                    active= "#7400FF",
                    inactive= '#6272A4',
                    fontsize = 24,
                    highlight_method='block',
                    block_highlight_text_color = '#282A36',
                    disable_drag =True,
                    borderwidth = 1,
                    this_current_screen_border = '#7400FF',
                    padding = 15,
            ),
                widget.Prompt(),
                widget.WindowName(
                    foreground = '#A4A6FF',
                ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),#001FFFwn", foreground="#d75f
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                #widget.StatusNotifier(),

                widget.TextBox(
                        text="",
                        background = "#000000",
                        foreground = "#FF4141",
                        fontsize = 40,
                        padding = -3, 
                ),
         
                widget.Systray(
                    background = '#FF4141',
                    padding = 5,
                ),

                widget.TextBox(
                        text="",
                        background = "#FF4141",
                        foreground = "#FFF080",
                        fontsize = 40,
                        padding = -3,
                ),

                widget.Battery(
                    foreground = "#000000",
                    background = "#FFF080",
                    format = "{char}{percent:2.0%} {hour:d}:{min:02d}",
                    #fmt = 'Battery:{}',
                    charge_char = "",
                    discharge_char = "",
                    empty_char = "",
                    padding = 3,
                    update_interval = 1,
                    ),

                widget.TextBox(
                        text="",
                        background = "#FFF080",
                        foreground = "#FFA822",
                        fontsize = 40,
                        padding = -3,
                    ),


                widget.Volume(
                    foreground = "#000000",
                    background = "#FFA822",
                    #emoji = True,
                    fmt = 'Volume: {}',
                    padding = 10,
                    #volume_app = "volumeicon",
                ),

                widget.TextBox(
                        text="",
                        background = "#FFA822",
                        foreground = "#7400FF",
                        fontsize = 40,
                        padding = -3,
                    ),

                widget.Clock(
                format="%Y-%m-%d %a %I:%M %p",
                background = '#7400FF',
                foreground = '000000',
                ),

                

                widget.TextBox(
                        text="",
                        background = "#7400FF",
                        foreground = "#282A36",
                        fontsize = 40,
                        padding = -3,
                    ),

                widget.QuickExit(
                    default_text='', countdown_format='',
                    background = '#282A36',
                    borderwidth = 1,
                    fontsize = 25,
                    countdown_start = 1,
                    foreground = '#FF0000',
                    padding = 15,
                ),
            ],
            24,
            background = "#000000",
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
