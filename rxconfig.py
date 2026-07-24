import reflex as rx
from reflex_components_radix.plugin import RadixThemesPlugin
from reflex.plugins.sitemap import SitemapPlugin


config = rx.Config(
    app_name="portfolio",
    plugins=[
        SitemapPlugin(),
        RadixThemesPlugin(),
    ],
    disable_plugins=[],
)

