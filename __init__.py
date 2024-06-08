from aqt import browser, gui_hooks, qt, mw
from . import edge_tts_gen
from anki.utils import is_win
import os.path
import sys


def on_browser_will_show_context_menu(browser: browser.Browser, menu: qt.QMenu):
    menu.addSeparator()
    menu.addAction(
        "Generate edge-tts Audio", lambda: edge_tts_gen.onEdgeTTSOptionSelected(browser)
    )


def load_edge_tts():
    edge_tts_path = os.path.join(mw.pm.addonFolder(), "edge-tts")
    if is_win is True:
        edge_tts_site_packages_path = os.path.join(
            edge_tts_path, "Lib", "site-packages"
        )
    else:
        edge_tts_site_packages_path = os.path.join(
            edge_tts_path,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            "site-packages",
        )

    sys.path.append(edge_tts_site_packages_path)
    import edge_tts
    import asyncio
    if is_win is True:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


gui_hooks.browser_will_show_context_menu.append(on_browser_will_show_context_menu)
load_edge_tts()
