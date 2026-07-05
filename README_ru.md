<div align="center">

# ⚙️ WarDustry

**Набор контента о военной технике для [Mindustry](https://mindustrygame.github.io/) — бронемашины, тяжёлое вооружение и техника современной войны.**

[![Game](https://img.shields.io/badge/Mindustry-v146-orange)](https://github.com/Anuken/Mindustry/releases)
[![Type](https://img.shields.io/badge/тип-Java--мод%20(Gradle)-blue)]()
[![Build](https://img.shields.io/badge/сборка-gradlew%20jar-success)]()
[![License](https://img.shields.io/badge/лицензия-MIT-green)](LICENSE)

🌍 **Языки:** [English](README.md) · Русский (этот файл)

</div>

---

## 📖 О моде

**WarDustry** — мод для Mindustry на тему **военной техники**: барражирующие дроны, ганшипы, наземная техника и заводы, которые их производят. Поставляется как **Java-мод** (собирается через Gradle), при этом контент остаётся data-driven (Hjson + PNG).

## 🚁 Контент

| Категория | Контент |
| --- | --- |
| 🛩️ Воздушные дроны | **Шахед** (барражирующий боеприпас), **Дрон-камикадзе**, **Разведдрон**, **Дрон-бомбардировщик**, **Ракетный дрон**, **Дрон-ганшип**, **Дрон-перехватчик** |
| 🚙 Наземная техника | **Джип** (быстрая разведмашина), **Автобус** (бронетранспортёр) |
| 🏭 Заводы | **Завод беспилотников** (строит воздушные дроны), **Завод техники** (строит наземную технику) |

Все названия и описания переведены на английский и русский.

## 📂 Структура проекта

```
wardustry/
├── mod.hjson              # Метаданные (главный класс, java:true, minGameVersion…)
├── build.gradle          # Сборка Gradle (зависит от API Mindustry v146)
├── settings.gradle       # rootProject.name = WarDustry
├── gradlew / gradlew.bat # Обёртка Gradle
├── gradle/wrapper/       # Jar обёртки + properties
├── src/
│   └── wardustry/
│       └── WarDustryMod.java   # Java-точка входа (локализует имя/описание мода)
├── assets/               # Всё, что упаковывается в корень jar
│   ├── icon.png
│   ├── bundles/          # bundle.properties (EN) + bundle_ru.properties (RU)
│   ├── content/          # Контент Hjson: units/ и blocks/
│   └── sprites/          # Спрайты 32-bit RGBA PNG (blocks/, units/, units/weapons/)
├── tools/                # gen_sprites.py / gen_icon.py (генераторы графики)
├── README.md             # Документация на английском
├── README_ru.md          # Документация на русском (этот файл)
└── LICENSE               # Лицензия MIT
```

## 🛠️ Как устроен мод

- **Java-мод с data-driven контентом** — мод поставляется как собранный Gradle Java-jar (`mod.hjson` содержит `java: true` + `main: wardustry.WarDustryMod`), но блоки и юниты по-прежнему описаны в Hjson в `assets/content/`, а графика `.png` — в `assets/sprites/`.
- **Локализация имени/описания мода** — Mindustry берёт имя и описание самого мода прямо из `mod.hjson` и **не** переводит их через bundle-файлы. `WarDustryMod.init()` подставляет `mod.wardustry.displayName` / `mod.wardustry.description` из активного языкового bundle, поэтому в русском клиенте текст будет на русском, иначе — на английском.
- **Двуязычные bundle-файлы** — строки контента лежат в `assets/bundles/bundle.properties` (английский) и `bundle_ru.properties` (русский).

## 🔨 Сборка из исходников

Нужен **JDK 17**. Из корня репозитория:

```bash
./gradlew jar        # -> build/libs/WarDustryDesktop.jar (десктоп)
```

Для кроссплатформенного jar (десктоп + Android) установите Android SDK (задайте `ANDROID_HOME`, `d8` в `PATH`) и выполните `./gradlew deploy`.

## 📦 Установка

1. Соберите jar (см. выше) или скачайте готовый `WarDustryDesktop.jar`.
2. Положите `.jar` в папку модов Mindustry:
   - **Steam:** `steam/steamapps/common/Mindustry/saves/mods/`
   - **Windows (не Steam):** `%appdata%/Mindustry/mods/`
   - **Linux:** `~/.local/share/Mindustry/mods/`
3. Запустите Mindustry → **Моды** → включите **WarDustry** → перезапустите игру.

Также можно импортировать прямо в игре: **Моды → Импорт → Импорт с GitHub**, указав `u7019134065-png/wardustry`.

## 📚 Материалы для изучения

- [Официальная вики по моддингу Mindustry](https://mindustrygame.github.io/wiki/modding/)
- [Исходники Mindustry (Anuken/Mindustry)](https://github.com/Anuken/Mindustry)
- [Формат Hjson](https://hjson.github.io/)
- Родственный проект: **GodDustry** — полноценный пример контент-пака.

## 📄 Лицензия

Распространяется под [лицензией MIT](LICENSE).
