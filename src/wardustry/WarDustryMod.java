package wardustry;

import arc.Core;
import mindustry.Vars;
import mindustry.mod.Mod;
import arc.util.Log;

public class WarDustryMod extends Mod{
    @Override
    public void init(){
        Log.info("WarDustryMod initialized.");
        var mod = Vars.mods.locateMod("wardustry");
        if(mod != null){
            mod.meta.displayName = Core.bundle.get("mod.wardustry.displayName", mod.meta.displayName);
            mod.meta.description = Core.bundle.get("mod.wardustry.description", mod.meta.description);
        }
    }
}
