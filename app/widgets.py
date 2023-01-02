from martor.widgets import AdminMartorWidget

class CustomAdminMartorWidget(AdminMartorWidget):
    class Media(AdminMartorWidget.Media):
        css = {
            'all': ('css/martor.js',)
        }
