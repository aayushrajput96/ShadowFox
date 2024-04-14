{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c878d284",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#VARIABLES\n",
    "\n",
    "pi = 22/7\n",
    "\n",
    "print(type(pi))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "161c98b0",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1227568896.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[5], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    for = 4\u001b[0m\n\u001b[1;37m        ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "for = 4\n",
    "print(for)\n",
    "\n",
    "# 'for' is a reserved keyword in Python and cannot be used as a variable name.\n",
    "# This will result in a syntax error."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e970bb48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple Interest: 150.0\n"
     ]
    }
   ],
   "source": [
    "p = 1000  # Example principal amount\n",
    "r = 5     # Example rate of interest\n",
    "t = 3                 # Time in years\n",
    "\n",
    "# Calculate Simple Interest\n",
    "simple_interest = (p * r * t) / 100\n",
    "print(\"Simple Interest:\", simple_interest)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "062d3c6e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
