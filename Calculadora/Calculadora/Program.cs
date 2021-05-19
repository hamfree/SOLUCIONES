using System;

namespace Calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
            // Declarar variables y después inicializarlas a cero.
            int num1 = 0; int num2 = 0;

            // Mostrar título como la aplicación de calculadora en C#.
            Console.WriteLine("Calculadora de Consola en C#");
            Console.WriteLine("----------------------------");

            // Pedimos al usuario que teclee el primer número.
            Console.WriteLine("Teclee un número, y después presione Intro");
            num1 = Convert.ToInt32(Console.ReadLine());

            // Pedimos al usuario que teclee el segundo número.
            Console.WriteLine("Teclee otro número, y después presione Intro");
            num2 = Convert.ToInt32(Console.ReadLine());

            // Pedimos al usuario que seleccione una opción.
            Console.WriteLine("Seleccione una opción de la siguiente lista:");
            Console.WriteLine("\ta Agregar");
            Console.WriteLine("\tr Restar");
            Console.WriteLine("\tm Multiplicar");
            Console.WriteLine("\td Dividir");
            Console.WriteLine("¿Su opción?");

            // Usamos una expresión switch para hacer las matemáticas
            switch (Console.ReadLine())
            {
                case "a":
                    Console.WriteLine($"Su resultado: {num1} + {num2} = " + (num1 + num2));
                    break;
                case "r":
                    Console.WriteLine($"Su resultado: {num1} - {num2} = " + (num1 - num2));
                    break;
                case "m":
                    Console.WriteLine($"Su resultado: {num1} * {num2} = " + (num1 * num2));
                    break;
                case "d":
                    Console.WriteLine($"Su resultado: {num1} / {num2} = " + (num1 / num2));
                    break;
            }

            // Esperamos a que el usuario responda antes de cerrar
            Console.WriteLine("Pulse cualquier tecla para cerrar la aplicación de consola Calculadora...");
            Console.ReadKey();

        }
    }
}
