// Localize the mod's own display name and description from the active bundle.
var mod = Vars.mods.locateMod("wardustry");
if(mod != null){
    mod.meta.displayName = Core.bundle.get("mod.wardustry.displayName", mod.meta.displayName);
    mod.meta.description = Core.bundle.get("mod.wardustry.description", mod.meta.description);
}
