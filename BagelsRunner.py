class BagelsRunner:
  def __init__():
    # not much to do here
  def runBagels():
    eating = True
    samegame = True
    while eating:
      b = Bagels ( randint ( 100, 999 ) )
      samegame = True
      while samegame:
        guess = raw_input ( 'Try guessing: ' )
        correct = b.checkCombo ( guess )
        if ( correct ):
          print ( "You're right!" )
          c = raw_input ( "Want to play again? Y or N" )
          playAgainResponse = c[0]
          if playAgainResponse == 'N' or playAgainResponse == 'n':
            eating = False;
            print ( 'Bye!' )
          else:
            print ( 'Rebooting' )
            samegame = False
        else:
          print ( 'No, but here are some clues: ' )
          print ( b )
def main():
  print "\n\n\n\n\n"
  print "simpleBagels Python"
  print "by Jeffrey Wang"
  print "translated from Java by Jeffrey Wang"
  print "All guesses are 3-digit numbers from 100 to 999."
  print "[Fermi] means your number is at the right position, [Pico] means the position is wrong, [Bagels] means the numbers you added were never within the guess."
  b = BagelsRunner()
  b.runBagels()
