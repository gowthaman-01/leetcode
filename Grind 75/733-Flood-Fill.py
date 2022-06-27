def floodFill(image, sr, sc, newColor):
    def fill(pixel, old, new):
        r, c = pixel[0], pixel[1]
        if r not in range(len(image)) or c not in range(len(image[0])):
            return
        if pixel in visited:
            return
        visited[pixel] = True
        if image[r][c] != old:
            return
        image[r][c] = new
        fill((r + 1, c), old, new)
        fill((r - 1, c), old, new)
        fill((r, c + 1), old, new)
        fill((r, c - 1), old, new)

    visited = {}
    fill((sr, sc), image[sr][sc], newColor)
    return image
