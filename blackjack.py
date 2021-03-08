from random import shuffle

class Deck:
  # 4 suits = clubs, diamonds, hearts, spades
  suits = 'C', 'D', 'H', 'S'

  # 13 ranks = 1..9 + 10,10,10,10
  ranks = [n for n in range(1, 10)] + ([10] * 4)

  def __init__(self):
    # 52 cards: (1, 'C'), (2, 'C'), ..., (10, 'S')
    self.cards = [(r, s) for s in self.suits for r in self.ranks]

    # shuffle cards
    shuffle(self.cards)

  def draw(self, count, target):
    pass

INITIAL_DEALER_BANK = 5000
INITIAL_PLAYER_BANK = 500

class BasePlayer:
  def __init__(self):
    self.hand = []
    self.bank = INITIAL_PLAYER_BANK

  def get_value(self):
    pass

  def add_card(self):
    pass
  

class Dealer(BasePlayer):
  def __init__(self):
    super(self)
    self.bank = INITIAL_DEALER_BANK
    pass

  def hide_cards(self, count):
    pass

class Player(BasePlayer):
  def __init__(self):
    super(self)
    pass

  def get_bet(self):
    pass

  def get_decision(self, game):
    pass

class Blackjack:
  deck = Deck()
  dealer = Dealer()
  player = Player()

  def __init__(self):
    pass
  
  def start(self):
    while self.player.bank > 0:
      # 1 - PLace bets
      self.place_bets()
    
      # 2 - Distribute cards, 2 cards for each player
      self.deck.draw(count=2, target=self.player)

      # 3 - The dealer draws 2 cards, 1 visible and another hidden
      self.deck.draw(count=2, target=self.dealer)
      self.dealer.hide_cards(count=1)

      player_value = self.player.get_value()

      # 4.1 If player burned
      if player_value > 21:
        # Get players money
        self.get_player_money(target=self.player)
      
      # 4.2 Else If player got BLACKJACK
      elif player_value == 21:
        # Pay player with insterest
        self.pay_player(target=self.player)
      
      # 4.3 Get player's decision
      else:
        decision = self.player.get_decision()
        
        # If player wants to Draw
        if decision == 'DRAW':
          stop = False

          while (
            stop is not True 
            and self.player.get_value() <=  21
          ):
            self.deck.draw(count=1, target=self.player)
            stop = self.player.get_draw_again()
        
        # If player wants to Double Down
        if decision == 'DOUBLE':
          self.double_bet(self.player)
          self.deck.draw(count=1, target=self.player)

        if decision == 'HOLD':
          pass

      # 5. Show dealer's remaining card
      self.dealer.show_cards()

      dealer_value = self.dealer.get_value()


      # 6.1 If dealer burned
      if dealer_value > 21:
        # Pay player
        self.dealer.pay_player(self.player)
      
      # 6.2 If dealer got BLACKJACK
      elif dealer_value == 21:
        # If the player also got BLACKJACK
        if player_value  == 21:
          pass
        #  Else get players money
        else:
          self.get_player_money(target=self.player)
      
      # 6.3 Else, the dealer got < 21
      else:
        # Draw until value is at least 17
        while dealer_value < 17:
          self.deck.draw(count=1, target=self.dealer)
          dealer_value = self.dealer.get_value

        # If dealer burned
        if dealer_value > 21:
          # Pay players with interest
          self.dealer.pay_player(self.player)
        # If dealer wins
        elif dealer_value > player_value:
          # Get player's money
          self.get_player_money(target=self.player)

        # If the dealer and the player got the same 
        elif dealer_value == player_value:
          pass

        # Else, the dealer lost (dealer_value < player_value)
        else:
          # Pay player with interest
          self.pay_player(self.player)

  def place_bets(self):
    pass

  def distribute_cards(self, count, target):
    pass

  def get_draw_again(self):
    pass

  def double_bet(self):
    pass

  def pay_player(self, player):
    pass

  def get_player_money(self, player):
    pass