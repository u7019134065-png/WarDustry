<div align="center">

# ⚙️ WarDustry

**A military-tech content pack for [Mindustry](https://mindustrygame.github.io/) — armored vehicles, heavy weaponry and modern warfare machinery.**

[![Game](https://img.shields.io/badge/Mindustry-v146-orange)](https://github.com/Anuken/Mindustry/releases)
[![Type](https://img.shields.io/badge/type-Java%20mod%20(Gradle)-blue)]()
[![Build](https://img.shields.io/badge/build-gradlew%20jar-success)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

🌍 **Languages:** English (this file) · [Русский](README_ru.md)

</div>

---

## 📖 About

**WarDustry** is a Mindustry mod themed around **military technology** — loitering drones, gunships, ground vehicles and the factories that build them. It is packaged as a **Java mod** (built with Gradle) while its content stays data-driven in Hjson + PNG.

## 🚁 Content

| Category | Content |
| --- | --- |
| 🛩️ Air drones | **Shahed** (loitering munition), **Kamikaze Drone**, **Recon**, **Bomber**, **Missile**, **Gunship**, **Interceptor**, **EMP** & **Scout** drones |
| 🚙 Ground vehicles | **Jeep**, **Bus** (armored transport), **Scout Vehicle**, **APC**, **Artillery Vehicle**, **MBT**, **Heavy Gunship** |
| 👑 Boss unit | **Jshon Ban** — 5000 HP + a 3000 HP force-field shield, burns enemies inside the shield, and on death detonates a tiered blast (8000 dmg point-blank, 300 dmg out to a 250-tile radius) |
| 🔫 Turrets | Autocannon, Flak Gun, Railgun, Missile Battery, Mortar, Tesla, Laser, **Plasma Turret** and the **Uranium Launcher** (inflicts the custom **Irradiation** slow) |
| ☢️ Resources | **Uranium** ore + **Plasma Energy** liquid (a new "energy" fluid), **Steel**, **Shell** |
| 🏭 Production & power | Drone/Vehicle factories, tactical drills, steel smelter, munitions factory, **Plasma Reactor**, **Plasma Turbine**, diesel/solar/battery power |
| 🧱 Logistics & defense | Armored conveyor/router/junction/bridge, steel & reinforced walls, blast door, repair / shield / overdrive projectors |

Content spans **40+ blocks and units**. All names and descriptions are localized in **English, Russian and Ukrainian**.

## 📂 Project structure

```
wardustry/
├── mod.hjson              # Mod metadata (main class, java:true, minGameVersion…)
├── build.gradle          # Gradle build (depends on Mindustry v146 API)
├── settings.gradle       # rootProject.name = WarDustry
├── gradlew / gradlew.bat # Gradle wrapper
├── gradle/wrapper/       # Wrapper jar + properties
├── src/
│   └── wardustry/
│       └── WarDustryMod.java   # Java entrypoint (localizes mod name/description)
├── assets/               # Everything packaged into the jar root
│   ├── icon.png
│   ├── bundles/          # bundle.properties (EN) + bundle_ru.properties (RU)
│   ├── content/          # Hjson content: units/ and blocks/
│   └── sprites/          # 32-bit RGBA PNG art (blocks/, units/, units/weapons/)
├── tools/                # gen_sprites.py / gen_icon.py (reusable art generators)
├── README.md             # English documentation (this file)
├── README_ru.md          # Russian documentation
└── LICENSE               # MIT license
```

## 🛠️ How this mod is set up

- **Java mod, data-driven content** — the mod ships as a Gradle-built Java jar (`mod.hjson` has `java: true` + `main: wardustry.WarDustryMod`), but blocks and units are still defined in Hjson under `assets/content/` with `.png` art under `assets/sprites/`.
- **Localized mod name/description** — Mindustry reads the mod's own name/description straight from `mod.hjson` and does **not** translate them through bundles. `WarDustryMod.init()` applies `mod.wardustry.displayName` / `mod.wardustry.description` from the active language bundle at load time, so the mod shows Russian text in a Russian client and English otherwise.
- **Bilingual bundles** — content strings live in `assets/bundles/bundle.properties` (English) and `bundle_ru.properties` (Russian).

## 🔨 Building from source

Requires **JDK 17**. From the repo root:

```bash
./gradlew jar        # -> build/libs/WarDustryDesktop.jar (desktop)
```

For a cross-platform (desktop + Android) jar, install the Android SDK (set `ANDROID_HOME`, with `d8` on your `PATH`) and run `./gradlew deploy`.

## 📦 Installation

1. Build the jar (see above) or download a release `WarDustryDesktop.jar`.
2. Drop the `.jar` into your Mindustry mods directory:
   - **Steam:** `steam/steamapps/common/Mindustry/saves/mods/`
   - **Windows (non-Steam):** `%appdata%/Mindustry/mods/`
   - **Linux:** `~/.local/share/Mindustry/mods/`
3. Launch Mindustry → **Mods** → enable **WarDustry** → restart.

You can also import it in-game via **Mods → Import → Import from GitHub** using `u7019134065-png/wardustry`.

## 📚 Learning resources

- [Official Mindustry Modding Wiki](https://mindustrygame.github.io/wiki/modding/)
- [Mindustry source (Anuken/Mindustry)](https://github.com/Anuken/Mindustry)
- [Hjson format](https://hjson.github.io/)
- Sister project: **GodDustry** — a fully-featured example content pack.

## 📄 License

Released under the [MIT License](LICENSE).
