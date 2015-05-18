class Bagels:
  bagel = ""
  result = ""
  guess = ""
  def __init__ ( bagelin ):
    bagel = bagelin
  def checkCombo ( guessin ):
    guess = guessin
    inresult = ""
    chunks = []
    for i in xarray ( 0, len(bagel) ):
      chunks.append(bagel[i:i+1])
    for j in xarray ( 0, len(bagel) ):
      if guess[j:j+1] == chunks[j]:
        inresult += bagel[j:j+1]
      else:
        within = False
        k = 0
        while ( not within and k < len(bagel) ):
          if guess[j:j+1] == chunks[k]:
            inresult += "!"
            within = True
          k = k + 1
      if not within:
        inresult += "?"
    result = inresult
    if guess == result:
      return True
    else:
      return False

  public String toString () {
    String ret = "";
    if ( this.guess != this.result ) {
      for ( int i = 0; i < this.result.length(); i++ ) {
        if ( this.result.charAt(i) == this.guess.charAt(i) ) {
          ret += "[Fermi]";
        } else if ( this.result.charAt(i) == '!' ) {
          ret += "[Pico]";
        }
      }
    }
    if ( ret == "" ) {
      ret += "[Bagels]";
    }
    return ret;
  }
}
