import flet as ft
import threading
from pathlib import Path

# Asset paths
ASSETS_DIR = Path("Assets")
LOADING_ANIMATION = ASSETS_DIR / "Loading Animation.gif"
ASSETS = [
    ASSETS_DIR / "1.png",
    ASSETS_DIR / "2.png",
    ASSETS_DIR / "3.png",
    ASSETS_DIR / "4.png",
    ASSETS_DIR / "5.gif",
    ASSETS_DIR / "6.gif",
    ASSETS_DIR / "7.gif",
]

# Preloaded assets dictionary
preloaded_assets = {}
assets_loaded = False


def preload_assets(page: ft.Page):
    """Preload all assets in the background."""
    global preloaded_assets, assets_loaded
    
    for i, asset_path in enumerate(ASSETS):
        try:
            if asset_path.exists():
                if asset_path.suffix == '.gif':
                    preloaded_assets[i] = ft.Image(src=str(asset_path))
                else:
                    preloaded_assets[i] = ft.Image(src=str(asset_path))
        except Exception as e:
            print(f"Error loading {asset_path}: {e}")
    
    assets_loaded = True
    print("All assets preloaded")


def main(page: ft.Page):
    page.title = "UX to UI Slider"
    page.window_width = 1024
    page.window_height = 768
    page.window_resizable = True
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "white"
    
    # Create loading screen
    loading_animation = ft.Image(
        src=str(LOADING_ANIMATION.absolute()), 
        fit=ft.ImageFit.CONTAIN,
        width=400,
        height=400
    )
    progress_bar = ft.ProgressBar(value=0, width=800, height=20)
    
    loading_container = ft.Container(
        content=ft.Column(
            controls=[
                loading_animation,
                ft.Container(height=40),
                progress_bar,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            tight=True,
        ),
        width=1024,
        height=768,
        bgcolor="white",
        alignment=ft.alignment.center,
    )
    
    # Main screen (initially hidden)
    current_asset_index = [0]  # Use list to make it mutable
    
    def create_main_screen():
        current_image = ft.Image(
            src=str(ASSETS[0].absolute()) if ASSETS[0].exists() else "",
            fit=ft.ImageFit.CONTAIN
        )
        
        # Track GIF animations to restart them
        gif_timers = {}
        
        def on_slider_change(e):
            """Handle slider value changes."""
            value = int(e.control.value)
            current_asset_index[0] = value
            
            asset_path = ASSETS[value]
            if asset_path.exists():
                current_image.src = str(asset_path.absolute())
            
            page.update()
        
        # Create a responsive slider with UX/UI labels
        def create_slider_control():
            # Use Row with Expanded for responsive design
            return ft.Row(
                controls=[
                    # UX label
                    ft.Container(
                        content=ft.Text(
                            "UX", 
                            size=16, 
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
                        ),
                        width=60,
                        alignment=ft.alignment.center,
                    ),
                    # Slider that expands to fill space
                    ft.Container(
                        content=ft.Slider(
                            min=0,
                            max=6,
                            value=0,
                            divisions=6,
                            label="{value}",
                            on_change=on_slider_change,
                        ),
                        expand=True,
                        padding=ft.padding.symmetric(horizontal=10),
                    ),
                    # UI label
                    ft.Container(
                        content=ft.Text(
                            "UI", 
                            size=16, 
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
                        ),
                        width=60,
                        alignment=ft.alignment.center,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )
        
        slider_row = create_slider_control()
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    # Top section: Image (responsive)
                    ft.Container(
                        content=current_image,
                        alignment=ft.alignment.center,
                        expand=True,
                        padding=ft.padding.only(bottom=20),
                        width=800,
                        height=500,
                        bgcolor="white",
                    ),
                    # Bottom section: Slider control (responsive)
                    ft.Container(
                        content=slider_row,
                        padding=ft.padding.symmetric(horizontal=20, vertical=20),
                        alignment=ft.alignment.bottom_center,
                        width=800,
                        bgcolor="white",
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
                expand=True,
            ),
            expand=True,
            padding=0,
            bgcolor="white",
            visible=False,
        )
    
    main_screen = create_main_screen()
    
    # Add both screens to the page
    page.add(loading_container)
    page.add(main_screen)
    
    # Start preloading assets in background
    def load_assets_thread():
        def update_progress(progress):
            progress_bar.value = progress
            page.update()
        
        import time
        
        # Simulate loading progress with enough time to see the GIF animation
        # Slower progress to ensure the animation plays at least once
        for i in range(101):
            update_progress(i / 100)
            time.sleep(0.05)  # Increased delay to show progress longer
        
        # Actually preload assets
        preload_assets(page)
        
        # Switch to main screen
        loading_container.visible = False
        main_screen.visible = True
        page.update()
    
    # Start loading in a separate thread
    threading.Thread(target=load_assets_thread, daemon=True).start()


if __name__ == "__main__":
    ft.app(target=main)
