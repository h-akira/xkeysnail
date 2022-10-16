# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] Change modifier keys as in xmodmap
# CapsLockをCtrlにして，Superと左Altを入れ替える
left_alt=Key.LEFT_ALT
define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
    Key.LEFT_ALT: Key.LEFT_META,
    Key.LEFT_META: left_alt
})

define_keymap(lambda wm_class: wm_class not in ("Code", "Xfce4-terminal"), {
    # Cursor
    K("C-b"): with_mark(K("left")),
    K("C-f"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    K("C-h"): with_mark(K("backspace")),
    # Beginning/End of line
    K("C-a"): with_mark(K("home")),
    K("C-e"): with_mark(K("end")),
    # Page up/down
    ## K("C-r"): with_mark(K("page_up")),
    ## K("C-w"): with_mark(K("page_down")),
    # Newline
    K("C-m"): K("enter"),
    K("C-j"): K("enter"),
    ## K("C-o"): [K("enter"), K("left")],
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    # Kill line
    K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    K("C-u"): [K("Shift-home"), K("C-x"), set_mark(False)],
    # Cancel
    K("C-g"): [K("esc"), set_mark(False)],
}, "Almost")
    
define_keymap(re.compile("Google-chrome"), {
    K("Alt-n"): K("C-n"),
    K("Alt-Shift-n"): K("C-Shift-n"),
}, "Chrome")


define_keymap(None, {
  # Copy
    K("Super-x"): [K("C-x"), set_mark(False)],
    K("Super-c"): [K("C-c"), set_mark(False)],
    K("Super-v"): [K("C-v"), set_mark(False)],
}, "ALL")
