'''
# ** Approach **

Step 1.
Sort the corner points by the x values then y values to find the locations of the corner points (e.g., top-left, top-right, etc.).
Store the locations (keys) and x,y coordinates (values) in a dict for easy reference later.

Step 2. 
Subtract the top-left x coordinate from the top-right x coordinate to get the length of the rectangle across the x-axis. 
Divide the value by the ncols-1 to get the width of each pixel.

Step 3. 
Subtract the top-left y coordinate from the bot-right y coordinate to get the height of the rectangle across the y-axis. 
Divide the value by the nrows-1 to get the height of each pixel.

Step 4. 
Create an empty array with m number of rows.
Iterate through the number of columns in each row.
Starting with the top-left corner, append the x,y coordinates to the row, and then increment x by the pixel width.
After running through each column, add the row to the array.
Before moving to the next row, clear the previous row and decrement y by the pixel height.

Step 5.
Return the array.

'''

from operator import itemgetter

class Solution:

    def get_coordinates(self, img_dims: tuple, corner_points: list[tuple]) -> list:

        # Find the locations of the corner points and store in a dict
        sort_pts = sorted(corner_points, key=itemgetter(0,1))        
        d = {
            'bot_left': sort_pts[0],
            'top_left': sort_pts[1],
            'bot_right': sort_pts[2],
            'top_right': sort_pts[3],
            }

        nrows = img_dims[0]
        ncols = img_dims[1]

        # Get width of the rectangle and each pixel
        x_dist = (d['top_right'][0] - d['top_left'][0])
        pix_width = x_dist / (ncols-1)

        # Get height of the rectangle and each pixel
        y_dist = (d['top_right'][1] - d['bot_right'][1])
        pix_height = y_dist / (nrows-1)
        
        # Create an empty array with m number of rows
        row = []
        arr = [row for _ in range(nrows)]

        # Start with the top-left corner
        # Iterate through the number of columns in each row
        y = d['top_left'][1]
        for r in range(nrows):
            
            x = d['top_left'][0]
            for c in range(ncols):
                # Append the x,y coordinates to the row
                row.append([round(float((x)),2), round(float((y)),2)])
                
                # Increment x by the pixel width
                x += pix_width
            
            # Add the complete row to the array
            arr[r] = row
            
            # Clear the row
            row = []
            
            # Decrement y by the pixel height
            y -= pix_height

        # Return the array
        return arr