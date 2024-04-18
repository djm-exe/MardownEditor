import flet as ft

class MarkdownEditor(ft.UserControl):
    def __init__(self) -> None:
        super().__init__()

        self.text_value: ft.Ref[str] = ft.Ref[str]()

    def build(self):
        self.txtEditor = ft.TextField(
            hint_text="Type your markdown here...",
            on_change=self.updateText,
            multiline=True,
            border=ft.InputBorder.NONE,
            expand=True
        )

        self.md = ft.Markdown(value=self.get_text, extension_set='default')

        self.controls = [self.txtEditor, self.md]

    def updateText(self, e):
        self.text_value.current = e.value

    def get_text(self) -> str:
        return self.text_value.current


def main(page: ft.Page):
    editor = MarkdownEditor()
    page.add(*editor.controls)


if __name__ == "__main__":
    ft.app(target=main)
