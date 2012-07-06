#
# encounter_tester.py
# July 17, 2007
# Nick Loadholtes
#
# A tester to try out non-fighting encounters
#
import EncounterManager as em


if __name__ == "__main__":
    encounters = {}
    print encounters['encounter']['title']
    encmgr = em.EncounterEngine()
    encmgr.startEncounter(encounters['encounter'])




