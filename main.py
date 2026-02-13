from nicegui import ui

@ui.page('/')
def index():
    ui.label('Hello NiceGUI World (now using CI/CD)!')
    ui.button('Click me!', on_click=lambda: ui.notify('I have been clicked!'))

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(host='0.0.0.0', port=8080, reload=False)