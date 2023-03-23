def pascal_triangle(n):
    # Return empty list if n <= 0
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Iterate over the rows of the triangle, adding new rows one by one
    for i in range(1, n):
        # Each row starts with a 1
        row = [1]
        
        # Calculate the rest of the row using the values from the previous row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        
        # Each row ends with a 1
        row.append(1)
        
        # Add the completed row to the triangle
        triangle.append(row)
    
    return triangle
