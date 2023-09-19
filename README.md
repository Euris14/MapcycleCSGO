
# Mapcycle Maker
This python script scans your csgo/maps directory, asks the user to select 
maps, checks maps against mariadb database, and then appends them to ~/csgo/addons/sourcemod/adminmenu_maplist.ini.
## Deployment

To deploy this project place the repository in your csgo server's user, and run

```bash
  cd Maplist-Creator-CSGO/
  python3 maprotation.py
```
    
## Demo

sudo python3 maprotation.py

adminmenu_maplist.ini
```bash
    surf_aircontrol_ksf
    surf_andromeda
    surf_atrium
    surf_aweles_inferno_fix
    surf_beginner
    surf_benevolent
    surf_bewatermyfriend
    surf_beyond
    surf_calycate2
    surf_calycate_ksf
    surf_chaos_refix
    surf_classics
    surf_classics2
    surf_colum_2
    surf_deathstar
    surf_delusional
    surf_deoa
    surf_derpis_ksf
    surf_dragon
    surf_elites_v2_fix
    surf_flow
    surf_forbidden_ways_ksf
    surf_fortum
    surf_frost
    surf_glass9
    surf_gold1
    surf_grassland
    surf_guitar_hi
    surf_hearth_fix
    surf_how2surf
    surf_impact_tnn
    surf_ing_njv
    surf_island
    surf_ivory
    surf_kitsune_nb
    surf_lessons
    surf_life_of_duck
    surf_lullaby_ksf
    surf_lux
    surf_me
    surf_mesa
    surf_mesa_mine
    surf_mesa_revo_go
    surf_minecraft_2016_final
    surf_mom_fix
    surf_orthodox_fix
    surf_paddy
    surf_palm
    surf_paradise
    surf_pox_revamp
    surf_prelude_ksf
    surf_quark_rc
    surf_rainbow
    surf_rebel_resistance_njv
    surf_reprise
    surf_reytx
    surf_rooftopsv2
    surf_simpsons_go_rc2
    surf_skyborn
    surf_southpark_refix
    surf_spacejam
    surf_summit
    surf_sunnyhappylove
    surf_superbia_new
    surf_tensile_njv
    surf_utopia_night
    surf_utopia_v3
    surf_volvic
    surf_whiteout
    surf_xiv_blood
    surf_zor

```
## Installation
```bash
  cd Maplist-Creator-CSGO/
  pip3 install -r requirements
```
Next make a secrets.json file;
```bash
  {
    "mysql":{
        "ip" : "127.0.0.1",
        "user" : "user",
        "pass" : "pass",
        "port" : "3306",
        "database" : "surftimer"
    }
}
```
## License

[MIT](https://choosealicense.com/licenses/mit/)

