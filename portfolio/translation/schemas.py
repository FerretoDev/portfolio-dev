from dataclasses import dataclass
#import reflex as rx

# 1. Definir estructura de datos para traducciones
@dataclass
class Translation:
    home: str
    projects: str
    experience: str
    welcome_title: str
    welcome_subtitle: str
    # ... +50 campos

# 2. Instancias de traducciones
class Translations:
    ES = Translation(
        home="Inicio",
        projects="Proyectos",
        experience="Experiencia",
        welcome_title="Desarrollador de Software y Modelado Matemático",
        welcome_subtitle="Especializado en soluciones data-driven con Python"
    )

    EN = Translation(
        home="Home",
        projects="Projects",
        experience="Experience",
        welcome_title="Software Developer & Mathematical Modeling",
        welcome_subtitle="Specialized in Python data-driven solutions"
    )

# 3. Estado global con dataclass
class LangState(rx.State):
    current_lang: Translation = Translations.ES

    def switch_to_english(self):
        self.current_lang = Translations.EN
        self.set_cookie("lang", "en")

    def switch_to_spanish(self):
        self.current_lang = Translations.ES
        self.set_cookie("lang", "es")

    def on_load(self):
        lang = self.get_cookie("lang", "es")
        self.current_lang = Translations.ES if lang == "es" else Translations.EN

# 4. Componente de cambio de idioma
def language_switcher() -> rx.Component:
    return rx.hstack(
        rx.button(
            "ES",
            on_click=LangState.switch_to_spanish,
            variant="soft" if LangState.current_lang == Translations.ES else "outline"
        ),
        rx.button(
            "EN",
            on_click=LangState.switch_to_english,
            variant="soft" if LangState.current_lang == Translations.EN else "outline"
        ),
        spacing="2"
    )

# 5. Uso en componentes
def hero() -> rx.Component:
    return rx.vstack(
        rx.heading(LangState.current_lang.welcome_title, size="2xl"),
        rx.text(LangState.current_lang.welcome_subtitle),
        language_switcher()
    )