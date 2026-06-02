from pynput.keyboard import Key, KeyCode, Listener as KeyboardListener
from pynput.mouse import Button, Listener as MouseListener

# on_move: 0–3 args
MouseListener(on_move=lambda: None)
MouseListener(on_move=lambda x: None)
MouseListener(on_move=lambda x, y: None)
MouseListener(on_move=lambda x, y, injected: None)

# on_click: 0–5 args
MouseListener(on_click=lambda: None)
MouseListener(on_click=lambda x: None)
MouseListener(on_click=lambda x, y: None)
MouseListener(on_click=lambda x, y, button: None)
MouseListener(on_click=lambda x, y, button, pressed: None)
MouseListener(on_click=lambda x, y, button, pressed, injected: None)

# on_scroll: 0–5 args
MouseListener(on_scroll=lambda: None)
MouseListener(on_scroll=lambda x: None)
MouseListener(on_scroll=lambda x, y: None)
MouseListener(on_scroll=lambda x, y, dx: None)
MouseListener(on_scroll=lambda x, y, dx, dy: None)
MouseListener(on_scroll=lambda x, y, dx, dy, injected: None)

# on_press / on_release: 0–2 args
KeyboardListener(on_press=lambda: None)
KeyboardListener(on_press=lambda key: None)
KeyboardListener(on_press=lambda key, injected: None)
KeyboardListener(on_release=lambda: None)
KeyboardListener(on_release=lambda key: None)
KeyboardListener(on_release=lambda key, injected: None)
