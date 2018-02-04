#!/bin/python3

import sys


class MatrixLayer:
    """
    Class for storing matrices and converting between matrix and layers representations.
    """
    def __init__(self, matrix):
        self.data = matrix
        self.rowCount = len(matrix)
        self.colCount = len(matrix[0])
        self.layerCount = min(self.rowCount, self.colCount) // 2

    def getLayers(self):
        """
        Get the layer representation of the matrix.
        :return:
        """
        layerArrays = []
        for layer in range(self.layerCount):
            newLayer = self._getLayer(self.data, layer)
            layerArrays.append(newLayer)
        self.data = layerArrays

    def getMatrix(self):
        """
        Get the matrix representation from the layers
        :return:
        """
        matrix = [[0 for _ in range(self.colCount)] for _ in range(self.rowCount)]
        for layer in range(self.layerCount):
            matrix = self._getMatrix(self.data, matrix, layer)
        self.data = matrix

    def rotateLayers(self, rotations):
        """
        Rotate the layers by some number of rotations
        :param rotations: int of rotations
        :return:
        """
        for i in range(len(self.data)):
            self.data[i] = self._layerRotate(self.data[i], rotations)

    @staticmethod
    def _getLayer(matrix, layer):
        """
        Get the desired layer as a list from the matrix.
        :param matrix: input matrix
        :param layer: 0 index layer id
        :return: list of layer
        """
        colCount = len(matrix[layer])
        rowCount = len(matrix)
        top = []
        bottom = []
        for col in range(layer, colCount - layer):
            top.append(matrix[layer][col])
            bottom.append(matrix[rowCount - 1 - layer][colCount - 1 - col])
        right = []
        left = []
        for row in range(layer + 1, rowCount - layer - 1):
            right.append(matrix[row][colCount - 1 - layer])
            left.append(matrix[rowCount - 1 - row][layer])

        layer = top + right + bottom + left
        return layer

    def _getMatrix(self, layers, matrix, layer):
        """
        Iteratively get the matrix from the layers
        :param layers:
        :param matrix:
        :param layer:
        :return:
        """
        # top row
        for col in range(layer, self.colCount - layer):
            tempRow = layer
            tempCol = col
            matrix[tempRow][tempCol] = layers[layer].pop(0)
        # right side
        for row in range(layer + 1, self.rowCount - layer - 1):
            tempRow = row
            tempCol = self.colCount - 1 - layer
            matrix[tempRow][tempCol] = layers[layer].pop(0)
        # bottom row
        for col in range(layer, self.colCount - layer):
            tempRow = self.rowCount - 1 - layer
            tempCol = self.colCount - 1 - col
            matrix[tempRow][tempCol] = layers[layer].pop(0)
        # left side
        for row in range(layer + 1, self.rowCount - layer - 1):
            tempRow = self.rowCount - 1 - row
            tempCol = layer
            matrix[tempRow][tempCol] = layers[layer].pop(0)

        return matrix

    @staticmethod
    def _layerRotate(layer, rotations):
        modRotations = rotations % len(layer)

        return layer[modRotations:] + layer[:modRotations]

    def print(self):
        for row in self.data:
            print(" ".join(map(str, row)))

def matrixRotation(matrix, rotations):
    newMatrix = MatrixLayer(matrix)
    newMatrix.getLayers()
    newMatrix.rotateLayers(rotations)
    newMatrix.getMatrix()
    newMatrix.print()

if __name__ == "__main__":
    m, n, r = input().strip().split(' ')
    m, n, r = [int(m), int(n), int(r)]
    matrix = []
    for matrix_i in range(m):
        matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
        matrix.append(matrix_t)
    matrixRotation(matrix, r)