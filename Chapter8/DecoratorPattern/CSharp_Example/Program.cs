using System;

namespace CSharp_Example
{
    class Program
    {
        static void Main(string[] args)
        {
            Beverage LatteWithMilkAndCream = new Cream(new Milk(new Latte()));
            Beverage EspressoWithCream = new Cream(new Espresso());
            Beverage EspressoWithMilkAndCream = new Cream(new Milk(new Espresso()));
            Beverage LatteWithMilk = new Milk(new Latte());
        }
    }

    abstract class Beverage
    {
        protected int cost;
        public string description;

        public virtual int getCost()
        {
            return this.cost;
        }
        public string getDescription()
        {
            return this.description;
        }
    }
    class Espresso : Beverage
    {
        public Espresso()
        {
            this.cost = 3;
            this.description = "Espresso coffee/";
        }
    }
    class Latte : Beverage
    {
        public Latte()
        {
            this.cost = 5;
            this.description = "Latte coffee/";
        }
    }
    abstract class AddOnDecorator : Beverage
    {
        protected Beverage beverage;

        public override int getCost()
        {
            return this.cost + beverage.getCost();
        }

        public AddOnDecorator(Beverage beverage)
        {
            this.beverage = beverage;
        }
    }
    class Milk : AddOnDecorator
    {
        public Milk(Beverage beverage) : base(beverage)
        {
            this.cost = 3;
            this.description = this.beverage.description + "With Milk/";
        }
    }
    class Cream : AddOnDecorator
    {
        public Cream(Beverage beverage) : base(beverage)
        {
            this.cost = 5;
            this.description = this.beverage.description + "With Cream/";
        }
    }
}
