{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "fibonacci.py",
      "authorship_tag": "ABX9TyO/18SnafKw+fycwrwoMWVP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/casc12/StudyPhyton/blob/main/fibonacci2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fibo(lastnum):\n",
        "  a = 0\n",
        "  b = 1\n",
        "\n",
        "  while a < lastnum:\n",
        "    print(a)\n",
        "    r = a + b\n",
        "    #p0 r = 0 + 1  = 1\n",
        "    #p1 r = 1 +1 = 2\n",
        "    #p2 r = 1 + 2 = 3\n",
        "    a = b\n",
        "    # p0 a = 1\n",
        "    #p1 a =1\n",
        "    #p2 = 2\n",
        "    b = r\n",
        "    #p0 b = 1\n",
        "    #p1 b = 2\n",
        "    #p2 = 3\n",
        "\n",
        "    #print(a)\n",
        "    #p0 = 1\n",
        "    #p1 = 1\n",
        "    #p2 = 2\n",
        "\n",
        "\n",
        "fibo(100)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GhuME0JUKmiR",
        "outputId": "0395376c-242d-4e22-ec6d-83cb4fad40f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "1\n",
            "2\n",
            "3\n",
            "5\n",
            "8\n",
            "13\n",
            "21\n",
            "34\n",
            "55\n",
            "89\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "JJXA-cHhLFAm"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}