using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dice
{
    class Dice
    {
        protected int sides;
        public int nbr;
    
        public int side
        {
            get {return sides;}
            set{if (sides <= 0){
            side = 0;
            }
            else
            {
                side = value;
            }
            }
         }
         public void dice()
            {
            nbr = 0;
            }
  public int Roll()
    {
      Random rnd = new Random();
      nbr = rnd.Next(1,7);
      switch(nbr)
      {
        case 1: return 1;
                      break;
        case 2: return 2;
                      break;
        case 3: return 3;
                      break;
        case 4: return 4;
                      break;
        case 5: return 5;
                      break;
        case 6: return 6;
                      break;
        default: return 0;  
            break;

      }
    }
    public static void Main(string[] args)
  {
    Dice d = new Dice();
    d.sides = 6;
    Console.WriteLine("number is {0}", d.Roll());
  }
}
}
