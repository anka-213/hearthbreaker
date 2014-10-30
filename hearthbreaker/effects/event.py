from hearthbreaker.effects.base import MinionEvent, PlayerEvent
from hearthbreaker.effects.selector import FriendlyPlayer, Player


class DidDamage(MinionEvent):
    def __init__(self, condition=None):
        super().__init__("did_damage", condition)


class SpellCast(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("spell_cast", condition, player)


class Either(PlayerEvent):
    def __init__(self, event1, event2, player=FriendlyPlayer()):
        super().__init__("either", None, player)
        self.event1 = event1
        self.event2 = event2

    def bind(self, target, func):
        self.event1.bind(target, func)
        self.event2.bind(target, func)

    def unbind(self, target, func):
        self.event1.unbind(target, func)
        self.event2.unbind(target, func)

    def __to_json__(self):
        return {
            'event_name': self.event_name,
            'event1': self.event1,
            'event2': self.event2,
            'player': self.player
        }

    def __from_json__(self, **kwargs):
        event1 = self.from_json(**kwargs['event1'])
        event2 = self.from_json(**kwargs['event2'])
        player = Player.from_json(kwargs['player'])
        return Either(event1, event2, player)


class CardPlayed(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("card_played", condition, player)


class TurnEnded(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("turn_ended", condition, player)


class TurnStarted(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("turn_started", condition, player)


class MinionDied(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("minion_died", condition, player)


class MinionPlaced(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("minion_placed", condition, player)


class MinionSummoned(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("minion_summoned", condition, player)


class MinionDamaged(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("minion_damaged", condition, player)


class Overloaded(PlayerEvent):
    def __init__(self, condition=None, player=FriendlyPlayer()):
        super().__init__("overloaded", condition, player)