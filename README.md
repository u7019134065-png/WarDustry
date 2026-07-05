<div align="center">

# ⚙️ WarDustry

**A military-tech content pack for [Mindustry](https://mindustrygame.github.io/) — armored vehicles, heavy weaponry and modern warfare machinery.**

[![Game](https://img.shields.io/badge/Mindustry-v146-orange)](https://github.com/Anuken/Mindustry/releases)
[![Type](https://img.shields.io/badge/type-JSON%2FHjson%20content%20mod-blue)]()
[![Status](https://img.shields.io/badge/status-scaffold%20(no%20content%20yet)-lightgrey)]()
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

🌍 **Languages:** English (this file) · [Русский](README_ru.md)

</div>

---

## 📖 About

**WarDustry** is a work-in-progress content mod for Mindustry themed around **military technology** — tanks and armored vehicles, artillery, autocannons, missile systems and the factories that build them.

> ⚠️ **This repository is currently a scaffold.** It contains the mod metadata, the folder structure and bilingual documentation only. **No blocks, items, liquids or units have been added yet** — that content will come in future updates.

## 📂 Project structure

```
wardustry/
├── mod.hjson              # Mod metadata (name, version, minGameVersion…)
├── README.md              # English documentation (this file)
├── README_ru.md           # Russian documentation
├── LICENSE                # MIT license
├── bundles/
│   ├── bundle.properties      # English display names/descriptions
│   └── bundle_ru.properties   # Russian display names/descriptions
├── scripts/
│   └── main.js            # Localizes the mod's own name/description
├── content/               # Data-driven content definitions (empty for now)
│   ├── items/
│   ├── liquids/
│   ├── blocks/
│   └── units/
└── sprites/               # 32-bit RGBA PNG art (empty for now)
    ├── items/
    ├── liquids/
    ├── blocks/
    └── units/
        └── weapons/
```

## 🧭 Planned content

Nothing is implemented yet. The intended direction for future updates:

| Category | Ideas |
| --- | --- |
| 🪖 Resources | Steel, gunpowder, alloys and other war materials |
| 🏭 Production | Foundries and munition factories |
| 🔫 Turrets | Autocannons, artillery, missile and flak batteries |
| 🚚 Units | Tanks, armored transports, gunships and support vehicles |
| ⚡ Power | Generators to feed the war machine |

## 🛠️ How this mod is set up

- **Pure data-driven content mod** — content is defined in `.hjson`/`.json` files under `content/`, with matching `.png` sprites under `sprites/`. No Java compilation required.
- **Localized mod name/description** — Mindustry reads the mod's own name/description straight from `mod.hjson` and does **not** translate them through bundles. `scripts/main.js` works around this by applying `mod.wardustry.displayName` / `mod.wardustry.description` from the active language bundle at load time, so the mod shows Russian text in a Russian client and English otherwise.
- **Bilingual bundles** — content strings (once added) belong in `bundles/bundle.properties` (English) and `bundles/bundle_ru.properties` (Russian).

## 📦 Installation

1. Download this repository as a `.zip` (or clone it).
2. Drop the folder/zip into your Mindustry mods directory:
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
