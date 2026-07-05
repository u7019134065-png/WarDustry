package wardustry;

import arc.math.*;
import arc.scene.ui.layout.Table;
import arc.util.*;
import mindustry.content.*;
import mindustry.entities.*;
import mindustry.entities.abilities.Ability;
import mindustry.gen.*;
import mindustry.type.*;
import mindustry.world.meta.*;

import static mindustry.Vars.tilesize;

public class EnemyStatusFieldAbility extends Ability{
    public StatusEffect effect;
    public float duration = 60f, reload = 100f, range = 20f;
    public boolean onShoot = false;
    public Effect applyEffect = Fx.none;
    public Effect activeEffect = Fx.overdriveWave;
    public float effectX, effectY;
    public boolean parentizeEffects, effectSizeParam = true;

    protected float timer;

    public EnemyStatusFieldAbility(){
    }

    public EnemyStatusFieldAbility(StatusEffect effect, float duration, float reload, float range){
        this.duration = duration;
        this.reload = reload;
        this.range = range;
        this.effect = effect;
    }

    @Override
    public void addStats(Table t){
        t.add("[lightgray]" + Stat.reload.localized() + ": [white]" + Strings.autoFixed(60f / reload, 2) + " " + StatUnit.perSecond.localized());
        t.row();
        t.add("[lightgray]" + Stat.shootRange.localized() + ": [white]" + Strings.autoFixed(range / tilesize, 2) + " " + StatUnit.blocks.localized());
        t.row();
        if(effect != null){
            t.add(effect.emoji() + " " + effect.localizedName);
        }
    }

    @Override
    public void update(Unit unit){
        timer += Time.delta;

        if(timer >= reload && (!onShoot || unit.isShooting)){
            Units.nearbyEnemies(unit.team, unit.x - range, unit.y - range, range * 2f, range * 2f, other -> {
                other.apply(effect, duration);
                if(applyEffect != Fx.none){
                    applyEffect.at(other, parentizeEffects);
                }
            });

            float x = unit.x + Angles.trnsx(unit.rotation, effectY, effectX), y = unit.y + Angles.trnsy(unit.rotation, effectY, effectX);
            if(activeEffect != Fx.none){
                activeEffect.at(x, y, effectSizeParam ? range : unit.rotation, parentizeEffects ? unit : null);
            }

            timer = 0f;
        }
    }
}
