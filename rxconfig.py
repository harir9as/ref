import reflex as rx

try:
    from reflex_base.plugins.sitemap import SitemapPlugin
except ImportError:
    SitemapPlugin = rx.plugins.SitemapPlugin

config = rx.Config(
    app_name="hiv",
    disable_plugins=[SitemapPlugin],
)
