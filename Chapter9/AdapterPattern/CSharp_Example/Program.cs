using System;

namespace CSharp_Example
{
    class Program
    {
        static void Main(string[] args)
        {
            // Client 
            ITarget target = new Adapter(new Adaptee());
            target.request();
        }
    }
    interface ITarget
    {
        void request();
    }
    class Adapter : ITarget
    {
        private Adaptee adaptee;
        public Adapter(Adaptee a)
        {
            this.adaptee = a;
        }
        public void request()
        {
            this.adaptee.specificRequest();
        }
    }
    class Adaptee
    {
        public void specificRequest()
        {
            // Code
        }
    }
}
