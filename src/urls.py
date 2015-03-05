from views import IndexView


URL_RULES = (
    # Add url rules here. Use the same key/attributes blueprint.add_url_rule
    # uses.
    {
        'rule': '/',
        'endpoint': 'index',
        'view_func': IndexView.as_view('documents'),
    },
)
