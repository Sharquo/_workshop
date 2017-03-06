using System;

class MagicSquare
{
    // 2016-04-04 Daily Programmer Challenge #261 [Easy] Verifiying magic squares
    // Not my work quite yet.
    // And it sort of doesnt quite work yet.

    private int[,] magicSquare;

    public MagicSquare()
    {
        this.magicSquare = new int[3, 3];
    }

    public bool TestForSquare(int[,] inputSquare)
    {
        this.magicSquare = new int[inputSquare.GetLength(0), inputSquare.GetLength(0)];
        Array.Copy(inputSquare, this.magicSquare, inputSquare.Length);

        return TestForSquare();
    }

    private bool TestSquare()
    {
        int totalRow, totalCol, totalMainDiagonal = 0, totalReverseDiagonal = 0;
        bool test = true;

        int constant = MagicConstant();
        for (int a = 0; a < this.magicSquare.GetLength(0); a++)
        {
            totalCol = totalRow = 0;
            for (int b = 0; b < this.magicSquare.GetLength(0); b++)
            {
                totalRow += this.magicSquare[a, b];
                totalCol += this.magicSquare[b, a];
            }
            totalMainDiagonal += this.magicSquare[a, a];
            totalReverseDiagonal += this.magicSquare[a, this.magicSquare.GetLength(0) - a - 1];

            test = totalRow == constant && totalCol == constant;
            if (!test)
                break;
        }

        test = test && totalMainDiagonal == constant && totalReverseDiagonal == constant;
        return test;
    }

    private int MagicConstant()
    {
        int c = this.magicSquare.GetLength(0);
        return (c * (c * c + 1) / 2);
    }
}

class TestClass
{
    public void TestMagicSquare()
    {
        MagicSquare magic = new MagicSquare();
        int[][,] threeByThree = new int[4][,];
        threeByThree[0] = new int[3, 3] { { 8, 1, 6 },{ 3, 5, 7 },{ 4, 9, 2 } };
        threeByThree[1] = new int[3, 3] { { 2, 7, 6 },{ 9, 5, 1 },{ 4, 3, 8 } };
        threeByThree[2] = new int[3, 3] { { 3, 5, 7 },{ 8, 1, 6 },{ 4, 9, 2 } };
        threeByThree[3] = new int[3, 3] { { 8, 1, 6 },{ 7, 5, 3 },{ 4, 9, 2 } };

        for (int a = 0; a < threeByThree.Length; a++)
        {
            bool result = magic.TestForSquare(threeByThree[a]);
            string resultString = result ? "true" : "false";
            Console.WriteLine(resultString);
        }

        int[][,] fourByFour = new int[2][,]
        {
            new int[4,4] { { 16, 9, 6, 3 },{ 5, 4, 15, 10 },{ 11, 14, 1, 8 },{ 2, 7, 12, 13 } },
            new int [4,4] { { 1, 15, 14, 4 },{ 12, 6, 7, 9 },{ 10, 8, 11, 5 },{ 13, 3, 2, 16 } }
        };

        Console.WriteLine();

        for (int a = 0; a < fourByFour.Length; a++)
        {
            bool result = magic.TestForSquare(fourByFour[a]);
            string resultString = result ? "true" : "false";
            Console.WriteLine(resultString);
        }
    }
}
