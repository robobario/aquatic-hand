__author__ = 'python'

def inventory(snapshot, hero_id):
    character = snapshot.arena.find(hero_id)
    return character.inventory

