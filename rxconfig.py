import reflex as rx
import reflex.plugins.sitemap.SitemapPlugin as SitemapPlugin

config = rx.Config(
    app_name="portfolio",
    plugins=[
        SitemapPlugin(),
    ],
    disable_plugins=[],
)
