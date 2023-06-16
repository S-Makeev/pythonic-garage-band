  
class Musician():
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument


class Band(Musician):
  instances = []
  def __init__ (self, name, members):
      self.name = name
      self.members = members
      Band.instances.append(self)

  def play_solos(self):
        # unable to find a way to incorporate template literal into an array
        solos = ["face melting guitar solo", "bom bom buh bom", "rattle boom crash"]
        return solos
  
  @classmethod
  def to_list(cls):
  
    return cls.instances      
      



class Guitarist(Musician):
    def __init__(self, name):
       super().__init__(name, "guitar")

    def __str__(self):
      guitar_string = f"My name is {self.name} and I play {self.instrument}"
      return guitar_string

    def __repr__(self):
        repr_guitar = f"Guitarist instance. Name = {self.name}"
        return repr_guitar

    def get_instrument(self):
        get_guitar= f"{self.instrument}"
        return get_guitar
     
    def play_solo(self):
        guitar_solo = f'face melting {self.instrument} solo'
        return guitar_solo
      


class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, "bass")

    def __str__(self):
        bass_string = f"My name is {self.name} and I play {self.instrument}"
        return bass_string
    
    def __repr__(self):
        repr_bass = f"Bassist instance. Name = {self.name}"
        return repr_bass

    def get_instrument(self):
        get_Bass= f"{self.instrument}"
        return get_Bass

    def play_solo(self):
        bass_solo = "bom bom buh bom"
        return bass_solo

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, "drums")

    def __str__(self):
        drumm_string = f"My name is {self.name} and I play {self.instrument}"
        return drumm_string
    
    def __repr__(self):
        repr_drummer = f"Drummer instance. Name = {self.name}"
        return repr_drummer

    def get_instrument(self):
        get_Drums= f"{self.instrument}"
        return get_Drums

    def play_solo(self):
        drums_solo = "rattle boom crash"
        return drums_solo


if __name__ == '__main__':
    pass