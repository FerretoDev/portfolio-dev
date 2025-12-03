import reflex as rx
from reflex.plugins import SitemapPlugin

config = rx.Config(
    app_name="portfolio",
    plugins=[
        SitemapPlugin(),
    ],
    disable_plugins=[],
)
