
"""
Bitmap Message, by Al Sweigart
Displays a text message according to the provided bitmap image.
"""

import sys

# The bitmap pattern:
bitmap = """
....................................................................
   **************     * *** ** *       ******************************
  ********************* ** ** * * ****************************** *
**        *****************       ******************************
            *************          ** * **** ** ************** *
             *********            *******    **************** * *
              ********           *************************** *
   *         * **** ***         *************** ****** ** *
                 **** *          ***************     *** *** *
                   ******         *************      **   ** *
                   ********        *************      * ** ***
                     ********         ********            * *** ****
                     *********         ****** *           **** ** * **
                     *********         ****** * *             *** *    *
                        ******         ***** **               *****    *
                        *****           **** *              ********
                       *****            ****                *********
                       ****             **                   *******     *
                       ***                                        *      *
                       **      *                   *
....................................................................
"""

print('Bitmap Message, by Al Sweigart al@inventwithpython.com')
print('Enter the message to display with the bitmap.')

message = input('> ')

if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():

    # Loop over each character in the line:
    for i, bit in enumerate(line):

        if bit == ' ':
            # Print an empty space:
            print(' ', end='')

        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')

    print()
