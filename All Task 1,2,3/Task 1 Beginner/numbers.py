{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e6f92cda",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "145 , o\n"
     ]
    }
   ],
   "source": [
    "#NUMBERS\n",
    "\n",
    "def format_string(arg1, arg2):\n",
    "    formatted_string = \"{} , {}\".format(arg1, arg2)\n",
    "    return formatted_string\n",
    "\n",
    "result = format_string(145, 'o')\n",
    "print(result)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "edb2e087",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total amount of water in the pond: 31033\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "radius = 84\n",
    "water_per_square_meter = 1.4\n",
    "\n",
    "# Calculate the area of the pond\n",
    "circle_area = math.pi * radius**2\n",
    "\n",
    "# Calculate the total amount of water in the pond\n",
    "total_water = circle_area * water_per_square_meter\n",
    "\n",
    "# Print the result without any decimal point\n",
    "print(\"Total amount of water in the pond:\", int(total_water))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "1162c50e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Speed: 1\n"
     ]
    }
   ],
   "source": [
    "distance = 490\n",
    "time_minutes = 7\n",
    "\n",
    "# Convert time to seconds\n",
    "time_seconds = time_minutes * 60\n",
    "\n",
    "speed = distance / time_seconds\n",
    "\n",
    "# Print the result without any decimal point\n",
    "print(\"Speed:\", int(speed))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2f23907",
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
