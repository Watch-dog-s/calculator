import unittest
import Calculator1


class MyTestCase(unittest.TestCase):



    def test_matrix(self):

        calculator = Calculator1.Calculator()

        matrix1 = calculator.Matrix(3, 3)
        matrix2 = calculator.Matrix(3, 3)


        matrix1.set_value(0, 0, 0)
        matrix1.set_value(0, 1, 0)
        matrix1.set_value(0, 2, 0)

        matrix1.set_value(1, 0, 1)
        matrix1.set_value(1, 1, 1)
        matrix1.set_value(1, 2, 1)

        matrix1.set_value(2, 0, 0)
        matrix1.set_value(2, 1, 0)
        matrix1.set_value(2, 2, 0)




        matrix2.set_value(0, 0, 1)
        matrix2.set_value(0, 1, 1)
        matrix2.set_value(0, 2, 1)

        matrix2.set_value(1, 0, 0)
        matrix2.set_value(1, 1, 0)
        matrix2.set_value(1, 2, 0)

        matrix2.set_value(2, 0, 1)
        matrix2.set_value(2, 1, 1)
        matrix2.set_value(2, 2, 1)


        result_matrix1 = calculator.Matrix.addition(self,matrix1, matrix2)

        expected_result = [[1,1,1], [1,1,1],[1,1,1]]

        for i in range(3):
            for j in range(3):
                self.assertEqual(result_matrix1.get_value(i, j), expected_result[i][j])




        result_matrix2 = calculator.Matrix.subtraction(self, matrix1, matrix2)
        expected_result1 = [[-1, -1, -1], [1, 1, 1], [-1, -1, -1]]

        for i in range(3):
            for j in range(3):
                self.assertEqual(result_matrix2.get_value(i, j), expected_result1[i][j])





        result_matrix3 = calculator.Matrix.multiplication(self, matrix1, matrix2)
        expected_result3 = [[0, 0, 0], [2, 2, 2], [0, 0, 0 ]]

        for i in range(3):
            for j in range(3):
                self.assertEqual(result_matrix3.get_value(i, j), expected_result3[i][j])

        result_matrix4 = calculator.Matrix.kronecker_multiplication(matrix1, matrix2)


        expected_result4 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        for i in range(6):
            for j in range(9):
                self.assertEqual(result_matrix4.get_value(i, j), expected_result4[i][j])



            result_det = calculator.Matrix.determinant(matrix1)
            expected_det = 0

            self.assertEqual(result_det, expected_det)

    def test_Statistics(self):
        calculator = Calculator1.Calculator()


        result= calculator.Statistics.max_num([1,2,3,4,5,6,7,8,9])
        expected_result=9
        self.assertEqual(result, expected_result)


        result=calculator.Statistics.variance([1,2,3,4,5,6,7,8,9])
        expected_result = 6.67
        self.assertEqual(result, expected_result)

        result = calculator.Statistics.average_quadratic([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected_result = 5.63
        self.assertEqual(result, expected_result)

        result = calculator.Statistics.distribution_mode([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected_result = 1
        self.assertEqual(result, expected_result)

        result = calculator.Statistics.standart_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected_result = 2.58
        self.assertEqual(result, expected_result)








if __name__ == '__main__':
    unittest.main()
